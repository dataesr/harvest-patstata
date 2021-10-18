#!/usr/bin/env python
# coding: utf-8

import csv_files_querying as cfq
import dtypes_patstat_declaration as types
import numpy as np
import os
import pandas as pd

# directory where the files are
DATA_PATH = "/run/media/julia/DATA/test/"

# set working directory
os.chdir(DATA_PATH)

def get_family_tit_abstract(type_publn: str, pat: pd.DataFrame) -> pd.DataFrame:
    """
    Select the title and abstract attached to each DOCDB family ID. Transform authorities and languages into ordered
    categorical values : WO (0) > EP (1) > FR (2) > rest (3) and German (0) > other Romance languages* (1) >
    English and French (2) > rest (3). Pick which language gets first position for each application and
    create a dataframe with 5 variables : DOCDB family ID, title/abstract in English, title/abstract in French,
    default language and title/abstract in default language
    * Romance languages that have been found in PATSTAT Global since 2010.
    :param type_publn: string ("title" or "abstract")
    :param pat: dataframe (patent df)
    :return: dataframe
    """
    _pat = pat.copy()
    _pat["tri_type_office"] = _pat["appln_auth"].apply(
        lambda x: 0 if x == "WO" else 1 if x == "EP" else 2 if x == "FR" else 3)

    description_lg = f"appln_{type_publn}_lg"
    description_wd = f"appln_{type_publn}"
    description_order = f"tri_{type_publn}_lg"
    var_order = ["appln_filing_date", "tri_type_office"]
    var_to_select = [description_lg, description_wd]

    _pat[description_order] = _pat[description_lg].apply(
        lambda x: 0 if x == "de" else 1 if x in ["es", "it", "pt", "ro"] else 2 if x in ["en", "fr"] else 99)

    def fam_desc_language(tmp: pd.DataFrame, vorder: list) -> pd.DataFrame:
        """
        This function groups on families and gets the first values of the variables in list "var_to_select" after
        ordering by the variables in "var_order" list
        :param tmp: subset of patent dataframe - must have family identifier "docdb_family_id"
        :param vorder: variables which will serve to order data
        :return: ordered dataframe
        """

        fam_desc = tmp[["docdb_family_id"] + vorder + var_to_select] \
            .sort_values(["docdb_family_id"] + vorder) \
            .groupby(["docdb_family_id"], as_index=False).first() \
            .drop(columns=vorder)

        return fam_desc

    # order data for title/abstract in English then French
    desc_en = fam_desc_language(_pat[_pat[description_lg] == "en"], var_order)
    desc_fr = fam_desc_language(_pat[_pat[description_lg] == "fr"], var_order)

    # remove English, French and NA and use "language" order for other languages
    tmpother = _pat[(~_pat[description_lg].isin(["en", "fr"])) & (~pd.isna(_pat[description_lg]))]
    var_order_other = [description_order, "appln_filing_date"]

    # order data for title/abstract in other languages
    desc_other = fam_desc_language(tmpother, var_order_other)

    # keep only DOCDB family IDs in the other languages df if the ID is not found in English AND French df
    desc_other = desc_other[(~desc_other["docdb_family_id"].isin(desc_en["docdb_family_id"])) & (
        ~desc_other["docdb_family_id"].isin(desc_fr["docdb_family_id"]))].dropna()

    # merge all the dataframes to get the title/abstract and main languages attached to each DOCDB family
    desc_col = _pat[["docdb_family_id"]]\
        .merge(desc_en, how="left", on="docdb_family_id").drop(columns=description_lg) \
        .rename(columns={description_wd: "{}_en".format(type_publn)}) \
        .merge(desc_fr, how="left", on="docdb_family_id").drop(columns=description_lg) \
        .rename(columns={description_wd: "{}_fr".format(type_publn)}) \
        .merge(desc_other, how="left", on="docdb_family_id") \
        .rename(columns={description_wd: "{}_default".format(type_publn),
                         description_lg: "{}_default_language".format(type_publn)}) \
        .drop_duplicates()

    return desc_col

# Récupération des codes CPC, à partir du printemps 2020, on les a par famille table 225


def get_cpc_ipc_patent_codes(set_patent, name_table_techno):
    """   This function gets the technologies in the table "name_table_techno" related to the patents in "set_patent"

    param set_patent:  set of application identifiers "appln_id"
    type set_patent: set
    param name_table_techno:  Table with technology informations - must have application identifier "appln_id"
    type name_table_techno: dataframe

    :return: a dataframe with one line for each group : patent/level of technology/technology code

    """

    # cette partie permet de lire des tables de technologies de patstat et en extraire seulement les technos des brevets
    # de notre périmètre (set_patent)
    def lect_patstat_table_from_appln_id(chunk):
        """   This query extracts from any patstat table the informations related to the patent applications in
        "set_patent"

        param chunk:   any dataframe containing the application identifier "appln_id"
        type chunk: dataframe
        param set_patent:  set containing the applications identifiers "appln_id" to keep
        type set_patent: set

        :return: a dataframe, an extract of T204 table for the application identifiers present in patent_table loaded

        """

        query = chunk[chunk["appln_id"].isin(set_patent)]

        return query

    dict_param_load = {"sep": ",", "chunksize": 5000000, "dtype": {"appln_id": str}}

    table_techno = cfq.multi_csv_files_querying(name_table_techno, lect_patstat_table_from_appln_id, dict_param_load)

    # on identifie la variable qui contient les codes et contient "class_symbol"
    # ( ça peut être cpc_class_symbol ou ipc_class_symbol)
    for col in table_techno.columns:
        if "class_symbol" in col:
            col_class_symbol = col

    # on démultiplie l"information sur les codes technos pour l"avoir à tous les niveaux

    table_techno["groupe"] = table_techno[col_class_symbol].str.replace(" ", "")
    table_techno["ss_classe"] = table_techno["groupe"].str[0:4]
    table_techno["classe"] = table_techno["groupe"].str[0:3]
    table_techno["section"] = table_techno["groupe"].str[0:1]

    list_level_data_frames = []
    for level in ["groupe", "ss_classe", "classe", "section"]:
        level_data_frame = table_techno.melt(id_vars=["appln_id"], value_vars=[level], var_name="level",
                                             value_name="code") \
            .drop_duplicates()
        list_level_data_frames.append(level_data_frame.copy())
    cpc_patent_codes = pd.concat(list_level_data_frames)

    return cpc_patent_codes


def unify_cpc_ipc_patent_codes(set_patent):
    """  This function gets the cpc and ipc technology codes in the tables 224 and 209 from a set of patent ("appln_id")

    param set_patent:  Set of application identifiers "appln_id"
    type set_patent: set

    :return: a dataframe with one line for each group :
    patent/ type of classification/ level of technology/ technology code

    """

    # on prend les codes cpc de la table t224 liés aux dépôts de "set_patent"
    cpc_patent_codes = get_cpc_ipc_patent_codes(set_patent, "tls224")
    # puis les codes IPC de la talbe 209
    ipc_patent_codes = get_cpc_ipc_patent_codes(set_patent, "tls209")
    # On ajoute la variable "classif", pour le type de classification,
    # permettant de mettre les codes des 2 classifications dans la même table, qu"on retourne
    cpc_patent_codes["classif"] = "cpc"
    ipc_patent_codes["classif"] = "ipc"
    technos_patent_codes = pd.concat([cpc_patent_codes, ipc_patent_codes])

    return technos_patent_codes


def get_cpc_ipc_from_patent_to_family(patent_table):
    """   This function takes from patents table the technologies by patent and then gets it by family

    param patent_table:  Table with application informations - T201 or part of -
    must have family identifier "docdb_family_id" and application identifier "appln_id"
    type patent_table: dataframe

    :return: a dataframe with technologies by family

    """

    # this first function gets the ipc and cpc codes by application
    cpc_ipc_table = unify_cpc_ipc_patent_codes(set(patent_table["appln_id"]))
    # this function gets these codes by family
    fam_ipc_cpc = pd.merge(patent_table[["docdb_family_id", "appln_id"]], cpc_ipc_table,
                           on="appln_id", how="inner")[["docdb_family_id", "level", "code", "classif"]] \
        .drop_duplicates()
    # à la fin on obtient une table avec le type de classification "classif" (ipc ou cpc),
    # le code et le niveau ("classe", "sous-classe" ...)  pour chaque famille
    # Chaque brevet appartient à une multitude de codes technos, et encore plus la famille
    return fam_ipc_cpc


def get_cpc_family_codes(patent_table):
    """   This function gets the technologies in the table 225 by family from a patent table

    param patent_table:  Table with application informations - T201 or part of - must have family identifier
    "docdb_family_id"
    type patent_table: dataframe

    :return: a dataframe grouped by : family/level of technology/technology code

    """

    _patent = patent_table.copy()

    # A partir de 2020, une nouvelle table enregistre les codes cpc par famille,
    # et non plus par dépôt de brevet : la 225
    # On prend les codes dans cette table pour chaque famille

    def lect_patstat_table_from_docdb_family_id(chunk):
        """   This function creates a query to extract from any patstat table the informations related to the families
         in "set_family"

        param chunk:   any dataframe containing the family identifier "docdb_family_id"
        type chunk: dataframe
        param set_family:  set containing the family identifiers "docdb_family_id" to keep
        type set_family: set

        :return: a query that extracts from the dataframe "chunk" only the values for wich "docdb_family_id"
        belongs to "set_family"

        """

        query = chunk.loc[chunk["docdb_family_id"].isin(_patent["docdb_family_id"])]

        return query

    dict_param_load = {"sep": ",", "chunksize": 5000000, "dtype": types.tls225_types}
    t225 = cfq.multi_csv_files_querying("tls225", lect_patstat_table_from_docdb_family_id, dict_param_load)

    # on démultiplie les codes par niveau
    t225["groupe"] = t225["cpc_class_symbol"].str.replace(" ", "")
    t225["ss_classe"] = t225["groupe"].str[0:4]
    t225["classe"] = t225["groupe"].str[0:3]
    t225["section"] = t225["groupe"].str[0:1]

    list_level_data_frames = []

    for level in ["groupe", "ss_classe", "classe", "section"]:
        level_data_frame = t225.melt(id_vars=["docdb_family_id"], value_vars=[level], var_name="level",
                                     value_name="code") \
            .drop_duplicates()
        list_level_data_frames.append(level_data_frame.copy())

    cpc_family_codes = pd.concat(list_level_data_frames)

    return cpc_family_codes


def get_cpc_names(cpc_codes_table):
    # This function gets the labels corresponding to the cpc technology codes
    #
    # param cpc_codes_table  A table with a variable "code" wich correspond to a cpc technology code
    # type cpc_codes_table dataframe
    #
    # return the same dataframe with the label corresponding to the varaible "code" added

    cpc = cpc_codes_table.copy()

    cpc_libelles = cpc.merge(cpc_category_names, how="left", on="code")
    return cpc_libelles


def unify_technos_family_codes(patent_table):
    """   This function gets from one table with application and family identifiers the technology codes related.

    param patent_table:  Table with application informations - T201 or part of - must have family identifier
    "docdb_family_id"
    type patent_table: dataframe

    :return: a dataframe with families identifiers and : the type of classification, the level,
    the code and the label of technologies related

    """

    # Tout d"abord on récupère les codes technos provenant des table 224 et 209 (qui sont par patent)
    # et on les groupe par famille
    fam_ipc_cpc_from_patents = get_cpc_ipc_from_patent_to_family(patent_table).drop(columns=["classif"]) \
        .drop_duplicates()
    # On récupère ensuite les codes technos déjà par famille dans la table 225
    fam_cpc_from_families = get_cpc_family_codes(patent_table)
    # On fusionne en une table avec tous les codes technos par famille
    fam_technos = pd.concat([fam_ipc_cpc_from_patents, fam_cpc_from_families]).drop_duplicates()

    # Enfin on récupère les libellés liés à ces codes
    # (les libellés IPC sont les mêmes que cpc car la classification est une étendue (beaucoup plus volumineuse)
    # de la classification IPC : elle reprend la même classification de base
    fam_technos_with_names = get_cpc_names(fam_technos)

    return fam_technos_with_names


patent = pd.read_csv("patent.csv", sep="|",
                     parse_dates=["appln_filing_date", "earliest_filing_date", "earliest_publn_date",
                                  "appln_publn_date", "grant_publn_date"], dtype=types.patent_types)

family_appln = patent.groupby("docdb_family_id", as_index=False)[
    ["earliest_filing_date"]].min().rename(columns={"earliest_filing_date": "earliest_application_date"})

family_publn = patent.groupby("docdb_family_id", as_index=False)[["earliest_publn_date"]].min().rename(
    columns={"earliest_publn_date": "earliest_publication_date"})

patent["granted"] = patent["granted"].apply(lambda x: 0 if x == "N" else 1)

family_grant = patent.groupby(["docdb_family_id"]).agg({"granted": max, "grant_publn_date": min}) \
    .rename(columns={"granted": "is_granted", "grant_publn_date": "date_first_granted"})

family_phases = patent.groupby("docdb_family_id", as_index=False)[["oeb", "international"]].max().rename(
    columns={"oeb": "is_oeb", "international": "is_international"})

family_pi_types = patent.groupby(["docdb_family_id", "ipr_type"], as_index=True)[["appln_nr_epodoc"]] \
    .count() \
    .pivot_table(index="docdb_family_id", columns="ipr_type", values="appln_nr_epodoc",
                 aggfunc=np.sum, fill_value=0) \
    .rename(columns={"PI": "patents_count", "UM": "utility_models_count", "DP": "design_patents_count"})


family_titles = get_family_tit_abstract("title", patent)

family_abstracts = get_family_tit_abstract("abstract", patent)

families = pd.merge(patent[["docdb_family_id", "inpadoc_family_id"]].drop_duplicates(),
                    family_publn, how="left",
                    on="docdb_family_id").merge(family_appln, how="left",
                                                on="docdb_family_id").merge(family_phases,
                                                                            how="left",
                                                                            on="docdb_family_id").merge(
    family_pi_types, how="left", on="docdb_family_id").merge(family_grant, how="left", on="docdb_family_id").merge(
    family_titles, how="left", on="docdb_family_id").merge(family_abstracts, how="left",
                                                           on="docdb_family_id").sort_values("docdb_family_id")

families.fillna("", inplace=True)

cpc_category_names = pd.read_csv("/run/media/julia/DATA/DONNEES/PATENTS/NOMENCLATURES/TECHNOS/lib_cpc.csv",
                                 sep=",").rename(columns={"symbol": "code"}).drop(columns=["level", "ref"])

# families.to_csv("families.csv", sep="|", index=False)

family_technos_codes = unify_technos_family_codes(patent)

# family_technos_codes.to_csv("families_technologies.csv", sep="|", index=False)
