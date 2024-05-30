# Ce fichier utilisé tout au long du traitement, permet de déclarer le type des variables présentes dans les tables
# csv  à la lecture. !! évite les erreurs de format
import pandas as pd
from pandas.core.indexers import objects

tls206_types = {"person_id": pd.Int64Dtype(),
                "person_name": object,
                "person_name_orig_lg": object,
                "person_address": object,
                "person_ctry_code": object,
                "nuts": object,
                "nuts_level": pd.Int64Dtype(),
                "doc_std_name_id": pd.Int64Dtype(),
                "doc_std_name": object,
                "psn_id": pd.Int64Dtype(),
                "psn_name": object,
                "psn_level": pd.Int64Dtype(),
                "psn_sector": object,
                "han_id": pd.Int64Dtype(),
                "han_name": object,
                "han_harmonized": pd.Int64Dtype()}

tls207_types = {"applt_seq_nr": pd.Int64Dtype(),
                "invt_seq_nr": pd.Int64Dtype(),
                "appln_id": pd.Int64Dtype(),
                "person_id": pd.Int64Dtype()}

tls201_types = {"appln_id": pd.Int64Dtype(),
                "appln_auth": object,
                "appln_nr": object,
                "appln_kind": object,
                "appln_filing_date": object,
                "appln_filing_year": pd.Int64Dtype(),
                "appln_nr_epodoc": object,
                "appln_nr_original": object,
                "ipr_type": object,
                "receiving_office": object,
                "internat_appln_id": pd.Int64Dtype(),
                "int_phase": object,
                "reg_phase": object,
                "nat_phase": object,
                "earliest_filing_date": object,
                "earliest_filing_year": pd.Int64Dtype(),
                "earliest_filing_id": object,
                "earliest_publn_date": object,
                "earliest_publn_year": pd.Int64Dtype(),
                "earliest_pat_publn_id": pd.Int64Dtype(),
                "granted": object,
                "docdb_family_id": pd.Int64Dtype(),
                "inpadoc_family_id": pd.Int64Dtype(),
                "docdb_family_size": pd.Int64Dtype(),
                "nb_citing_docdb_fam": pd.Int64Dtype(),
                "nb_applicants": pd.Int64Dtype(),
                "nb_inventors": pd.Int64Dtype()}

tls211_types = {"pat_publn_id": pd.Int64Dtype(),
                "publn_auth": object,
                "publn_nr": object,
                "publn_nr_original": object,
                "publn_kind": object,
                "appln_id": pd.Int64Dtype(),
                "publn_date": object,
                "publn_lg": object,
                "publn_first_grant": object,
                "publn_claims": pd.Int64Dtype()}

tls209_types = {"appln_id": pd.Int64Dtype(),
                "ipc_class_symbol": object,
                "ipc_class_level": object,
                "ipc_version": object,
                "ipc_value": object,
                "ipc_position": object,
                "ipc_gener_auth": object}

tls225_types = {"docdb_family_id": pd.Int64Dtype(),
                "cpc_class_symbol": object,
                "cpc_gener_auth": object,
                "cpc_version": object,
                "cpc_position": object,
                "cpc_value": object,
                "cpc_action_date": object,
                "cpc_status": object,
                "cpc_data_source": object}

tls204_types = {"appln_id": pd.Int64Dtype(),
                "prior_appln_id": pd.Int64Dtype(),
                "prior_appln_seq_nr": pd.Int64Dtype()}

tls214_types = {"npl_publn_id": object,
                "xp_nr": pd.Int64Dtype(),
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

patent_types = {"appln_id": pd.Int64Dtype(),
                "appln_auth": object,
                "appln_nr": object,
                "appln_kind": object,
                "appln_filing_date": object,
                "appln_filing_year": pd.Int64Dtype(),
                "appln_nr_epodoc": object,
                "appln_nr_original": object,
                "ipr_type": object,
                "receiving_office": object,
                "internat_appln_id": pd.Int64Dtype(),
                "int_phase": object,
                "reg_phase": pd.Int64Dtype(),
                "nat_phase": pd.Int64Dtype(),
                "earliest_filing_date": object,
                "earliest_filing_year": pd.Int64Dtype(),
                "earliest_filing_id": pd.Int64Dtype(),
                "earliest_publn_date": object,
                "earliest_publn_year": pd.Int64Dtype(),
                "earliest_pat_publn_id": pd.Int64Dtype(),
                "granted": object,
                "docdb_family_id": pd.Int64Dtype(),
                "inpadoc_family_id": pd.Int64Dtype(),
                "docdb_family_size": pd.Int64Dtype(),
                "nb_citing_docdb_fam": pd.Int64Dtype(),
                "nb_applicants": pd.Int64Dtype(),
                "nb_inventors": pd.Int64Dtype(),
                "key_appln_nr": object,
                "oeb": pd.Int64Dtype(),
                "international": pd.Int64Dtype(),
                "appln_publn_id": pd.Int64Dtype(),
                "appln_publn_number": object,
                "appln_publn_date": object,
                "publn_kind": object,
                "grant_publn_id": pd.Int64Dtype(),
                "grant_publn_number": object,
                "grant_publn_date": object,
                "ispriority": pd.Int64Dtype(),
                "appln_title_lg": object,
                "appln_title": object,
                "appln_abstract_lg": object,
                "appln_abstract": object
                }

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

part_init_types = {"id_participant": object,
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
                   "old_name": object,
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
                   "key_appln_nr_person": object,
                   "idref": object,
                   "oc": object,
                   "ror": object,
                   "doc_std_name": object,
                   "doc_std_name_id": pd.Int64Dtype(),
                   "publication_number": str}

part_entp_types = {"id_participant": object,
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
                   "old_name": object,
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
                   "key_appln_nr_person": object,
                   "siren_psn": object,
                   "fam": object,
                   "new_name": object,
                   "name_psn": object,
                   "name_corrected": object,
                   "idref": object,
                   "oc": object,
                   "ror": object}

structures_types = {"siret": pd.Int64Dtype(),
                    "siren": str,
                    "identifiant_pic": pd.Int64Dtype(),
                    "identifiant_cti": pd.Int64Dtype(),
                    "identifiant_rcr": pd.Int64Dtype(),
                    "identifiant_orgref": pd.Int64Dtype(),
                    "element_fundref": pd.Int64Dtype(),
                    "numero_telephone_uai": pd.Int64Dtype(),
                    "rce": pd.Int64Dtype(),
                    "dev_immo": pd.Int64Dtype()}


tls212_types = {'pat_publn_id': pd.Int64Dtype(),
                'citn_replenished': pd.Int64Dtype(),
                'citn_id': pd.Int64Dtype(),
                'citn_origin': object,
                'cited_pat_publn_id': pd.Int64Dtype(),
                'cited_appln_id': pd.Int64Dtype(),
                'pat_citn_seq_nr': pd.Int64Dtype(),
                'cited_npl_publn_id': object,
                'npl_citn_seq_nr': pd.Int64Dtype(),
                'citn_gener_auth': object}
