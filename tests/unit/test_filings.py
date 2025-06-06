# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Test Suite to ensure legal filing schemas are valid.

This suite should have at least 1 test for every filing type allowed.
"""
import copy
from datetime import datetime

import pytest

from registry_schemas import validate
from registry_schemas.example_data import (
    ALTERATION_FILING_TEMPLATE,
    ANNUAL_REPORT,
    CHANGE_OF_ADDRESS,
    CHANGE_OF_DIRECTORS,
    CHANGE_OF_DIRECTORS_MAILING,
    CONSENT_AMALGAMATION_OUT,
    CONSENT_CONTINUATION_OUT,
    CONVERSION_FILING_TEMPLATE,
    COOPERATIVE,
    CORP_CHANGE_OF_ADDRESS,
    COURT_ORDER_FILING_TEMPLATE,
    FILING_HEADER,
    INCORPORATION_FILING_TEMPLATE,
    INTENT_TO_LIQUIDATE,
    REGISTRARS_NOTATION_FILING_TEMPLATE,
    REGISTRARS_ORDER_FILING_TEMPLATE,
    UNMANAGED,
)


def test_invalid_ar_filing():
    """Assert that the schema is performing as expected."""
    iar = {
        'filing': {
            'header': {
                'name': 'annualReport',
                'date': '2019-04-08'
            },
            'business': {
                'cacheId': 1,
                'foundingDate': '2007-04-08T00:00:00+00:00',
                'identifier': 'CP1234567',
                'lastLedgerTimestamp': '2019-04-15T20:05:49.068272+00:00',
                'legalName': 'legal name - CP1234567'
            }
        }
    }
    is_valid, errors = validate(iar, 'filing')

    # if errors:
    #     for err in errors:
    #         print(err.message)
    print(errors)

    assert not is_valid


def test_valid_coa_filing():
    """Assert that the Change of Address filing schema is performing as expected."""
    iar = {
        'filing': {
            'header': {
                'name': 'changeOfAddress',
                'date': '2019-04-08',
                'certifiedBy': 'full legal name',
                'email': 'no_one@never.get'
            },
            'business': {
                'cacheId': 1,
                'foundingDate': '2007-04-08T20:05:49.068272+00:00',
                'identifier': 'CP1234567',
                'lastLedgerTimestamp': '2019-04-15T20:05:49.068272+00:00',
                'lastPreBobFilingTimestamp': '2019-04-15T20:05:49.068272+00:00',
                'legalName': 'legal name - CP1234567'
            },
            'changeOfAddress': CHANGE_OF_ADDRESS
        }
    }
    is_valid, errors = validate(iar, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_coa_filing_bcorp():
    """Assert that the Change of Address filing schema is performing as expected."""
    iar = {
        'filing': {
            'header': {
                'name': 'changeOfAddress',
                'date': '2019-04-08',
                'certifiedBy': 'full legal name',
                'email': 'no_one@never.get'
            },
            'business': {
                'cacheId': 1,
                'foundingDate': '2007-04-08T20:05:49.068272+00:00',
                'identifier': 'CP1234567',
                'lastLedgerTimestamp': '2019-04-15T20:05:49.068272+00:00',
                'legalName': 'legal name - CP1234567'
            },
            'changeOfAddress': CORP_CHANGE_OF_ADDRESS
        }
    }
    is_valid, errors = validate(iar, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_coa_filing_bcorp():
    """Assert that the Change of Address filing schema conditionals are performing as expected."""
    coa_arr = CHANGE_OF_ADDRESS
    coa_arr['legalType'] = 'BC'
    iar = {
        'filing': {
            'header': {
                'name': 'changeOfAddress',
                'date': '',
                'certifiedBy': 'full legal name',
                'email': 'no_one@never.get'
            },
            'business': {
                'cacheId': 1,
                'foundingDate': '2007-04-08T00:00:00+00:00',
                'identifier': 'CP1234567',
                'lastLedgerTimestamp': '2019-04-15T20:05:49.068272+00:00',
                'legalName': 'legal name - CP1234567'
            },
            'changeOfAddress': coa_arr
        }
    }
    is_valid, errors = validate(iar, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_valid_cod_filing():
    """Assert that the Change of Directors filing schema is performing as expected."""
    filing = {
        'filing': {
            'header': {
                'name': 'changeOfDirectors',
                'date': '2019-04-08',
                'certifiedBy': 'full legal name',
                'email': 'no_one@never.get'
            },
            'business': {
                'cacheId': 1,
                'foundingDate': '2007-04-08T00:00:00+00:00',
                'identifier': 'CP1234567',
                'lastLedgerTimestamp': '2019-04-15T20:05:49.068272+00:00',
                'legalName': 'legal name - CP1234567'
            },
            'changeOfDirectors': CHANGE_OF_DIRECTORS
        }
    }

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_cod_filing_with_mailing_address():
    """Assert that the Change of Directors filing schema is performing as expected."""
    filing = {
        'filing': {
            'header': {
                'name': 'changeOfDirectors',
                'date': '2019-04-08',
                'certifiedBy': 'full legal name',
                'email': 'no_one@never.get'
            },
            'business': {
                'cacheId': 1,
                'foundingDate': '2007-04-08T00:00:00+00:00',
                'identifier': 'CP1234567',
                'lastLedgerTimestamp': '2019-04-15T20:05:49.068272+00:00',
                'legalName': 'legal name - CP1234567'
            },
            'changeOfDirectors': CHANGE_OF_DIRECTORS_MAILING
        }
    }

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_cod_filing():
    """Assert that the Change of Directors filing schema is catching invalid data."""
    filing = {
        'filing': {
            'header': {
                'name': 'changeOfDirectors',
                'date': '2019-04-08',
                'email': 'no_one@never.get',
            },
            'business': {
                'cacheId': 1,
                'foundingDate': '2007-04-08T00:00:00+00:00',
                'identifier': 'CP1234567',
                'lastLedgerTimestamp': '2019-04-15T20:05:49.068272+00:00',
                'legalName': 'legal name - CP1234567'
            },
            'changeOfDirectors': {
                'directors': [
                    {
                        'officer': {
                            'firstName': False,  # should be string
                            'lastName': 'Griffin'
                        },
                        'deliveryAddress': {
                            'streetAddress': 'mailing_address - address line one',
                            'addressCity': 'mailing_address city',
                            'addressCountry': 'mailing_address country',
                            'postalCode': 'H0H0H0',
                            'addressRegion': 'BC'
                        },
                        'title': 2  # should be string
                    }
                ]
            }
        }
    }

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_valid_multi_filing():
    """Assert that the filing schema is performing as expected with multiple filings included."""
    filing = {
        'filing': {
            'header': {
                'name': 'annualReport',
                'date': '2019-04-08',
                'certifiedBy': 'full legal name',
                'email': 'no_one@never.get'
            },
            'business': {
                'cacheId': 1,
                'foundingDate': '2007-04-08T00:00:00+00:00',
                'identifier': 'CP1234567',
                'lastLedgerTimestamp': '2019-04-15T20:05:49.068272+00:00',
                'legalName': 'legal name - CP1234567'
            },
            'annualReport': ANNUAL_REPORT,
            'changeOfDirectors': CHANGE_OF_DIRECTORS,
            'changeOfAddress': CHANGE_OF_ADDRESS
        }
    }

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_filing_paper():
    """Assert that a Paper Only filing is valid."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['availableOnPaperOnly'] = True
    filing['filing']['unmanaged'] = UNMANAGED

    # filing['filing']['available'] = 'available on paper only.'
    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_filing_colin_only():
    """Assert that a Colin Only filing is valid."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['unmanaged'] = UNMANAGED
    filing['filing']['header']['inColinOnly'] = True

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_effective_date():
    """Assert that the effective date is working correctly from a structural POV."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['unmanaged'] = UNMANAGED

    filing['filing']['header']['effectiveDate'] = datetime.utcnow().isoformat() + 'Z'

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid

    filing['filing']['header']['effectiveDate'] = 'this should fail'

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_incorporation_filing_schema():
    """Assert that the JSONSchema validator is working."""
    is_valid, errors = validate(INCORPORATION_FILING_TEMPLATE, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_coop_incorporation_filing_schema():
    """Assert that the JSONSchema validator is working."""
    coop_ia_filing = copy.deepcopy(INCORPORATION_FILING_TEMPLATE)
    del coop_ia_filing['filing']['incorporationApplication']['offices']['recordsOffice']
    del coop_ia_filing['filing']['incorporationApplication']['parties'][1]
    del coop_ia_filing['filing']['incorporationApplication']['shareStructure']
    del coop_ia_filing['filing']['incorporationApplication']['incorporationAgreement']
    coop_ia_filing['filing']['incorporationApplication']['cooperative'] = COOPERATIVE

    is_valid, errors = validate(coop_ia_filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_alteration_filing_schema():
    """Assert that the JSONSchema validator is working."""
    is_valid, errors = validate(ALTERATION_FILING_TEMPLATE, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_alteration_filing_schema_with_no_business():
    """Assert that the JSONSchema validator is working."""
    alteration_json = ALTERATION_FILING_TEMPLATE
    del alteration_json['filing']['business']
    is_valid, errors = validate(alteration_json, 'filing')
    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_conversion_filing_schema():
    """Assert that the JSONSchema validator is working."""
    is_valid, errors = validate(CONVERSION_FILING_TEMPLATE, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_conversion_filing_schema_with_no_business():
    """Assert that the JSONSchema validator is working."""
    conversion_json = CONVERSION_FILING_TEMPLATE
    del conversion_json['filing']['business']
    is_valid, errors = validate(conversion_json, 'filing')
    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_court_order_filing_schema():
    """Assert that the JSONSchema validator is working."""
    is_valid, errors = validate(COURT_ORDER_FILING_TEMPLATE, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_registrars_notation_filing_schema():
    """Assert that the JSONSchema validator is working."""
    is_valid, errors = validate(REGISTRARS_NOTATION_FILING_TEMPLATE, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_registrars_order_filing_schema():
    """Assert that the JSONSchema validator is working."""
    is_valid, errors = validate(REGISTRARS_ORDER_FILING_TEMPLATE, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


@pytest.mark.parametrize('filing, filing_type, field_to_empty', [
    (COURT_ORDER_FILING_TEMPLATE, 'courtOrder', 'fileNumber'),
    (REGISTRARS_NOTATION_FILING_TEMPLATE, 'registrarsNotation', 'orderDetails'),
    (REGISTRARS_ORDER_FILING_TEMPLATE, 'registrarsOrder', 'orderDetails'),
])
def test_invalid_order_filing_schema_with_no_order(filing, filing_type, field_to_empty):
    """Assert that the JSONSchema validator is working."""
    filing_json = copy.deepcopy(filing)
    del filing_json['filing'][filing_type]
    is_valid, errors = validate(filing_json, 'filing')
    assert not is_valid
    print(errors)

    filing_json = copy.deepcopy(filing)
    filing_json['filing'][filing_type][field_to_empty] = ''
    is_valid, errors = validate(filing_json, 'filing')
    assert not is_valid
    print(errors)

def test_consent_amalgamation_out_filing_schema():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['consentAmalgamationOut'] = copy.deepcopy(CONSENT_AMALGAMATION_OUT)
    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid

def test_consent_continuation_out_filing_schema():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['consentContinuationOut'] = copy.deepcopy(CONSENT_CONTINUATION_OUT)
    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_intent_to_liquidate_filing_schema():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['intentToLiquidate'] = copy.deepcopy(INTENT_TO_LIQUIDATE)
    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid
