# -*- coding: utf-8  -*-
"""Family module for Wiktionary."""
#
# (C) Pywikibot team, 2005-2016
#
# Distributed under the terms of the MIT license.
#
from __future__ import absolute_import, unicode_literals

from pywikibot import family

__version__ = '$Id$'


# The Wikimedia family that is known as Wiktionary
class Family(family.SubdomainFamily, family.WikimediaFamily):

    """Family class for Wiktionary."""

    name = 'wiktionary'

    closed_wikis = [
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Afar_Wiktionary
        'aa',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Abkhaz_Wiktionary
        'ab',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Akan_Wiktionary
        'ak',
        # https://als.wikipedia.org/wiki/Wikipedia:Stammtisch/Archiv_2008-1#Afterwards.2C_closure_and_deletion_of_Wiktionary.2C_Wikibooks_and_Wikiquote_sites
        'als',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Assamese_Wiktionary
        'as',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Avar_Wiktionary
        'av',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Bashkir_Wiktionary
        'ba',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Bihari_Wiktionary
        'bh',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Bislama_Wiktionary
        'bi',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Bambara_Wiktionary
        'bm',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Tibetan_Wiktionary
        'bo',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Chamorro_Wiktionary
        'ch',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Nehiyaw_Wiktionary
        'cr',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Dzongkha_Wiktionary
        'dz',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Inupiak_Wiktionary
        'ik',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Marshallese_Wiktionary
        'mh',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Moldovan_Wiktionary
        'mo',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Pali_Bhasa_Wiktionary
        'pi',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Rhaetian_Wiktionary
        'rm',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Kirundi_Wiktionary
        'rn',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Sardinian_Wiktionary
        'sc',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Shona_Wiktionary
        'sn',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Tongan_Wiktionary
        'to',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Klingon_Wiktionary
        'tlh',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Twi_Wiktionary
        'tw',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Xhosa_Wiktionary
        'xh',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Yoruba_Wiktionary
        'yo',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Zhuang_Wiktionary
        'za',
    ]

    removed_wikis = [
        'tokipona',
    ]

    def __init__(self):
        """Constructor."""
        self.languages_by_size = [
            'en', 'mg', 'fr', 'sh', 'es', 'zh', 'ru', 'lt', 'de', 'nl', 'sv',
            'pl', 'ku', 'el', 'it', 'ta', 'tr', 'fi', 'hu', 'ko', 'io', 'kn',
            'vi', 'pt', 'ca', 'chr', 'sr', 'hi', 'ja', 'hy', 'ro', 'no', 'ml',
            'th', 'id', 'et', 'uz', 'li', 'my', 'or', 'te', 'cs', 'ar', 'fa',
            'jv', 'eu', 'az', 'gl', 'lo', 'uk', 'br', 'da', 'hr', 'fj', 'eo',
            'oc', 'bg', 'ps', 'simple', 'cy', 'vo', 'is', 'zh-min-nan', 'wa',
            'scn', 'ast', 'he', 'tg', 'af', 'tl', 'sk', 'sw', 'fy', 'la', 'nn',
            'ky', 'co', 'pnb', 'lv', 'mn', 'ka', 'sl', 'sq', 'nah', 'lb', 'nds',
            'bs', 'kk', 'sm', 'tk', 'sa', 'hsb', 'mk', 'km', 'bn', 'be', 'ms',
            'ga', 'ur', 'an', 'wo', 'ang', 'vec', 'tt', 'gn', 'mr', 'sd', 'so',
            'csb', 'ug', 'gd', 'st', 'mt', 'pa', 'roa-rup', 'si', 'ia', 'ie',
            'mi', 'ay', 'kl', 'jbo', 'fo', 'ln', 'zu', 'na', 'gv', 'kw', 'gu',
            'rw', 'ts', 'ne', 'om', 'qu', 'ss', 'su', 'ha', 'iu', 'am', 'dv',
            'tpi', 'yi', 'ti', 'sg', 'tn', 'ks',
        ]

        super(Family, self).__init__()

        # Global bot allowed languages on
        # https://meta.wikimedia.org/wiki/Bot_policy/Implementation#Current_implementation
        self.cross_allowed = [
            'am', 'an', 'ang', 'ast', 'ay', 'az', 'be', 'bg', 'bn', 'br', 'bs',
            'ca', 'chr', 'co', 'cy', 'da', 'dv', 'eo', 'es', 'et', 'eu', 'fa',
            'fi', 'fj', 'fo', 'fy', 'ga', 'gd', 'gl', 'gn', 'gv', 'hu', 'ia',
            'id', 'ie', 'io', 'jv', 'ka', 'kl', 'kn', 'ku', 'ky', 'lb', 'lo',
            'lt', 'lv', 'mg', 'mk', 'ml', 'mn', 'my', 'ne', 'nl', 'no', 'oc',
            'or', 'pt', 'sh', 'simple', 'sk', 'sl', 'sm', 'su', 'tg', 'th',
            'ti', 'tk', 'tn', 'tpi', 'ts', 'ug', 'uk', 'vo', 'wa', 'wo', 'zh',
            'zh-min-nan', 'zu',
        ]

        # Other than most Wikipedias, page names must not start with a capital
        # letter on ALL Wiktionaries.
        self.nocapitalize = list(self.langs.keys())

        # Which languages have a special order for putting interlanguage links,
        # and what order is it? If a language is not in interwiki_putfirst,
        # alphabetical order on language code is used. For languages that are in
        # interwiki_putfirst, interwiki_putfirst is checked first, and
        # languages are put in the order given there. All other languages are
        # put after those, in code-alphabetical order.

        self.alphabetic_sv = [
            'aa', 'af', 'ak', 'als', 'an', 'roa-rup', 'ast', 'gn', 'ay', 'az',
            'id', 'ms', 'bm', 'zh-min-nan', 'jv', 'su', 'mt', 'bi', 'bo', 'bs',
            'br', 'ca', 'cs', 'ch', 'sn', 'co', 'za', 'cy', 'da', 'de', 'na',
            'mh', 'et', 'ang', 'en', 'es', 'eo', 'eu', 'to', 'fr', 'fy', 'fo',
            'ga', 'gv', 'sm', 'gd', 'gl', 'hr', 'io', 'ia', 'ie', 'ik', 'xh',
            'is', 'zu', 'it', 'kl', 'csb', 'kw', 'rw', 'rn', 'sw', 'ky', 'ku',
            'la', 'lv', 'lb', 'lt', 'li', 'ln', 'jbo', 'hu', 'mg', 'mi', 'mo',
            'my', 'fj', 'nah', 'nl', 'cr', 'no', 'nn', 'hsb', 'oc', 'om', 'ug',
            'uz', 'nds', 'pl', 'pt', 'ro', 'rm', 'qu', 'sg', 'sc', 'st', 'tn',
            'sq', 'scn', 'simple', 'ss', 'sk', 'sl', 'so', 'sh', 'fi', 'sv',
            'tl', 'tt', 'vi', 'tpi', 'tr', 'tw', 'vo', 'wa', 'wo', 'ts', 'yo',
            'el', 'av', 'ab', 'ba', 'be', 'bg', 'mk', 'mn', 'ru', 'sr', 'tg',
            'uk', 'kk', 'hy', 'yi', 'he', 'ur', 'ar', 'tk', 'sd', 'fa', 'ha',
            'ps', 'dv', 'ks', 'ne', 'pi', 'bh', 'mr', 'sa', 'hi', 'as', 'bn',
            'pa', 'pnb', 'gu', 'or', 'ta', 'te', 'kn', 'ml', 'si', 'th', 'lo',
            'dz', 'ka', 'ti', 'am', 'chr', 'iu', 'km', 'zh', 'ja', 'ko',
        ]

        self.interwiki_putfirst = {
            'da': self.alphabetic,
            'en': self.alphabetic,
            'et': self.alphabetic,
            'fi': self.alphabetic,
            'fy': self.fyinterwiki,
            'he': ['en'],
            'hu': ['en'],
            'ms': self.alphabetic_revised,
            'pl': self.alphabetic_revised,
            'sv': self.alphabetic_sv,
            'simple': self.alphabetic,
        }

        self.interwiki_on_one_line = ['pl']

        self.interwiki_attop = ['pl']

        # Subpages for documentation.
        # TODO: List is incomplete, to be completed for missing languages.
        self.doc_subpages = {
            '_default': ((u'/doc', ),
                         ['en']
                         ),
        }
