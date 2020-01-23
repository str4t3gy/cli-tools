# Stubs for cryptography.x509.oid (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class ExtensionOID:
    SUBJECT_DIRECTORY_ATTRIBUTES: Any = ...
    SUBJECT_KEY_IDENTIFIER: Any = ...
    KEY_USAGE: Any = ...
    SUBJECT_ALTERNATIVE_NAME: Any = ...
    ISSUER_ALTERNATIVE_NAME: Any = ...
    BASIC_CONSTRAINTS: Any = ...
    NAME_CONSTRAINTS: Any = ...
    CRL_DISTRIBUTION_POINTS: Any = ...
    CERTIFICATE_POLICIES: Any = ...
    POLICY_MAPPINGS: Any = ...
    AUTHORITY_KEY_IDENTIFIER: Any = ...
    POLICY_CONSTRAINTS: Any = ...
    EXTENDED_KEY_USAGE: Any = ...
    FRESHEST_CRL: Any = ...
    INHIBIT_ANY_POLICY: Any = ...
    ISSUING_DISTRIBUTION_POINT: Any = ...
    AUTHORITY_INFORMATION_ACCESS: Any = ...
    SUBJECT_INFORMATION_ACCESS: Any = ...
    OCSP_NO_CHECK: Any = ...
    TLS_FEATURE: Any = ...
    CRL_NUMBER: Any = ...
    DELTA_CRL_INDICATOR: Any = ...
    PRECERT_SIGNED_CERTIFICATE_TIMESTAMPS: Any = ...
    PRECERT_POISON: Any = ...

class OCSPExtensionOID:
    NONCE: Any = ...

class CRLEntryExtensionOID:
    CERTIFICATE_ISSUER: Any = ...
    CRL_REASON: Any = ...
    INVALIDITY_DATE: Any = ...

class NameOID:
    COMMON_NAME: Any = ...
    COUNTRY_NAME: Any = ...
    LOCALITY_NAME: Any = ...
    STATE_OR_PROVINCE_NAME: Any = ...
    STREET_ADDRESS: Any = ...
    ORGANIZATION_NAME: Any = ...
    ORGANIZATIONAL_UNIT_NAME: Any = ...
    SERIAL_NUMBER: Any = ...
    SURNAME: Any = ...
    GIVEN_NAME: Any = ...
    TITLE: Any = ...
    GENERATION_QUALIFIER: Any = ...
    X500_UNIQUE_IDENTIFIER: Any = ...
    DN_QUALIFIER: Any = ...
    PSEUDONYM: Any = ...
    USER_ID: Any = ...
    DOMAIN_COMPONENT: Any = ...
    EMAIL_ADDRESS: Any = ...
    JURISDICTION_COUNTRY_NAME: Any = ...
    JURISDICTION_LOCALITY_NAME: Any = ...
    JURISDICTION_STATE_OR_PROVINCE_NAME: Any = ...
    BUSINESS_CATEGORY: Any = ...
    POSTAL_ADDRESS: Any = ...
    POSTAL_CODE: Any = ...

class SignatureAlgorithmOID:
    RSA_WITH_MD5: Any = ...
    RSA_WITH_SHA1: Any = ...
    RSA_WITH_SHA224: Any = ...
    RSA_WITH_SHA256: Any = ...
    RSA_WITH_SHA384: Any = ...
    RSA_WITH_SHA512: Any = ...
    RSASSA_PSS: Any = ...
    ECDSA_WITH_SHA1: Any = ...
    ECDSA_WITH_SHA224: Any = ...
    ECDSA_WITH_SHA256: Any = ...
    ECDSA_WITH_SHA384: Any = ...
    ECDSA_WITH_SHA512: Any = ...
    DSA_WITH_SHA1: Any = ...
    DSA_WITH_SHA224: Any = ...
    DSA_WITH_SHA256: Any = ...
    ED25519: Any = ...
    ED448: Any = ...

class ExtendedKeyUsageOID:
    SERVER_AUTH: Any = ...
    CLIENT_AUTH: Any = ...
    CODE_SIGNING: Any = ...
    EMAIL_PROTECTION: Any = ...
    TIME_STAMPING: Any = ...
    OCSP_SIGNING: Any = ...
    ANY_EXTENDED_KEY_USAGE: Any = ...

class AuthorityInformationAccessOID:
    CA_ISSUERS: Any = ...
    OCSP: Any = ...

class CertificatePoliciesOID:
    CPS_QUALIFIER: Any = ...
    CPS_USER_NOTICE: Any = ...
    ANY_POLICY: Any = ...

ObjectIdentifier: Any
_SIG_OIDS_TO_HASH: Any