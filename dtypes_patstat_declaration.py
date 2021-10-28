# Ce fichier utilisé tout au long du traitement, permet de déclarer le type des variables présentes dans les tables
# csv  à la lecture. !! évite les erreurs de format
import numpy as np
import pandas as pd

tls206_types = {"person_id": np.int64,
                "person_name": object,
                "person_name_orig_lg": object,
                "person_address": object,
                "person_ctry_code": object,
                "nuts": object,
                "nuts_level": np.int64,
                "doc_std_name_id": np.int64,
                "doc_std_name": object,
                "psn_id": np.int64,
                "psn_name": object,
                "psn_level": np.int64,
                "psn_sector": object,
                "han_id": np.int64,
                "han_name": object,
                "han_harmonized": np.int64}

tls207_types = {"applt_seq_nr": np.int64,
                "invt_seq_nr": np.int64,
                "appln_id": np.int64,
                "person_id": np.int64}

tls201_types = {"appln_id": np.int64,
                "appln_auth": object,
                "appln_nr": object,
                "appln_kind": object,
                "appln_filing_date": object,
                "appln_filing_year": np.int64,
                "appln_nr_epodoc": object,
                "appln_nr_original": object,
                "ipr_type": object,
                "receiving_office": object,
                "internat_appln_id": np.int64,
                "int_phase": object,
                "reg_phase": object,
                "nat_phase": object,
                "earliest_filing_date": object,
                "earliest_filing_year": np.int64,
                "earliest_filing_id": object,
                "earliest_publn_date": object,
                "earliest_publn_year": np.int64,
                "earliest_pat_publn_id": np.int64,
                "granted": object,
                "docdb_family_id": np.int64,
                "inpadoc_family_id": np.int64,
                "docdb_family_size": np.int64,
                "nb_citing_docdb_fam": np.int64,
                "nb_applicants": np.int64,
                "nb_inventors": np.int64}

tls211_types = {"pat_publn_id": np.int64,
                "publn_auth": object,
                "publn_nr": object,
                "publn_nr_original": object,
                "publn_kind": object,
                "appln_id": np.int64,
                "publn_date": object,
                "publn_lg": object,
                "publn_first_grant": object,
                "publn_claims": np.int64}

tls209_types = {"appln_id": np.int64,
                "ipc_class_symbol": object,
                "ipc_class_level": object,
                "ipc_version": object,
                "ipc_value": object,
                "ipc_position": object,
                "ipc_gener_auth": object}

tls225_types = {"docdb_family_id": np.int64,
                "cpc_class_symbol": object,
                "cpc_gener_auth": object,
                "cpc_version": object,
                "cpc_position": object,
                "cpc_value": object,
                "cpc_action_date": object,
                "cpc_status": object,
                "cpc_data_source": object}

tls204_types = {"appln_id": np.int64,
                "prior_appln_id": np.int64,
                "prior_appln_seq_nr": np.int64}

tls214_types = {"npl_publn_id": object,
                "xp_nr": np.int64,
                "npl_type": object,
                "npl_biblio": object,
                "npl_author": object,
                "npl_title1": object,
                "npl_title2": object,
                "npl_editor": object,
                "npl_volume": object,
                "npl_issue": object,
                "npl_publn_date": object,
                "npl_publn_end_date": object,
                "npl_publisher": object,
                "npl_page_first": object,
                "npl_page_last": object,
                "npl_abobjectact_nr": object,
                "npl_doi": object,
                "npl_isbn": object,
                "npl_issn": object,
                "online_availability": object,
                "online_classification": object,
                "online_search_date": object}

patent_types = {"appln_id": np.int64, "appln_auth": object, "appln_nr": object, "appln_kind": object,
                "appln_filing_date": object,
                "appln_filing_year": np.int64, "appln_nr_epodoc": object, "appln_nr_original": object,
                "ipr_type": object,
                "receiving_office": object, "internat_appln_id": np.int64, "int_phase": object,
                "reg_phase": np.int64,
                "nat_phase": np.int64, "earliest_filing_date": object, "earliest_filing_year": np.int64,
                "earliest_filing_id": np.int64, "earliest_publn_date": object, "earliest_publn_year": np.int64,
                "earliest_pat_publn_id": np.int64, "granted": object, "docdb_family_id": np.int64,
                "inpadoc_family_id": np.int64, "docdb_family_size": np.int64, "nb_citing_docdb_fam": np.int64,
                "nb_applicants": np.int64, "nb_inventors": np.int64, "key_appln_nr": object, "oeb": np.int64,
                "international": np.int64,
                "appln_publn_id": np.int64,
                "appln_publn_number": object, "appln_publn_date": object, "publn_kind": object,
                "grant_publn_id": object,
                "grant_publn_number": object,
                "grant_publn_date": object, "ispriority": np.int64}

partfin_types = {"id_participant": object,
                 "person_id": pd.Int64Dtype(),
                 "id_patent": object,
                 "docdb_family_id": pd.Int64Dtype(),
                 "inpadoc_family_id": pd.Int64Dtype(),
                 "applt_seq_nr": pd.Int64Dtype(),
                 "invt_seq_nr": pd.Int64Dtype(),
                 "earliest_filing_date": object,
                 "name_source": object,
                 "address_source": object,
                 "country_source": object,
                 "appln_auth": object,
                 "type": object,
                 "isascii": bool,
                 "name_corrected": object,
                 "country_corrected": object,
                 "siren": object,
                 "siret": object,
                 "id_paysage": object,
                 "rnsr": object,
                 "grid": object,
                 "sexe": object,
                 "id_personne": object,
                 "appln_id": pd.Int64Dtype(),
                 "appln_nr": object,
                 "appln_kind": object,
                 "receiving_office": object,
                 "key_appln_nr": object,
                 "key_appln_nr_person": object}

part_init_types = {"id_patent": np.int64, "person_id": np.int64, "docdb_family_id": np.int64,
                   "inpadoc_family_id": np.int64,
                   "appln_auth": object, "earliest_filing_date": object,
                   "publication_number": str, "type": str, "name_source": str, "address_source": str,
                   "country_source": str, "psn_sector": str,
                   "psn_id": str, "psn_name": str, "old_name": str, "country_corrected": str, "siren": str,
                   "siret": str, "id_paysage": str,
                   "rnsr": str, "grid": str, "sexe": str, "id_personne": str}
