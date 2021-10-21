# ./amelding_v2_2.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ff1e93e748f12b1371860156cff289fecac7c6a8
# Generated 2021-01-19 16:44:10.877263 by PyXB version 1.2.6 using Python 3.6.9.final.0
# Namespace urn:ske:fastsetting:innsamling:a-meldingen:v2_2

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:2c5526b2-5a6d-11eb-82b0-9c3dcfc2d5b3')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:ske:fastsetting:innsamling:a-meldingen:v2_2', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}InternasjonalIdentifikatortype
class InternasjonalIdentifikatortype (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InternasjonalIdentifikatortype')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 90, 2)
    _Documentation = None
InternasjonalIdentifikatortype._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'InternasjonalIdentifikatortype', InternasjonalIdentifikatortype)
_module_typeBindings.InternasjonalIdentifikatortype = InternasjonalIdentifikatortype

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Landkode
class Landkode (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Landkode')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 93, 2)
    _Documentation = None
Landkode._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Landkode', Landkode)
_module_typeBindings.Landkode = Landkode

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Arbeidsforholdstype
class Arbeidsforholdstype (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Arbeidsforholdstype')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 124, 2)
    _Documentation = None
Arbeidsforholdstype._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Arbeidsforholdstype', Arbeidsforholdstype)
_module_typeBindings.Arbeidsforholdstype = Arbeidsforholdstype

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Avloenningstype
class Avloenningstype (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Avloenningstype')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 127, 2)
    _Documentation = None
Avloenningstype._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Avloenningstype', Avloenningstype)
_module_typeBindings.Avloenningstype = Avloenningstype

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Yrke
class Yrke (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Yrke')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 130, 2)
    _Documentation = None
Yrke._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Yrke', Yrke)
_module_typeBindings.Yrke = Yrke

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Arbeidstidsordning
class Arbeidstidsordning (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Arbeidstidsordning')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 133, 2)
    _Documentation = None
Arbeidstidsordning._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Arbeidstidsordning', Arbeidstidsordning)
_module_typeBindings.Arbeidstidsordning = Arbeidstidsordning

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}AarsakSluttdato
class AarsakSluttdato (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AarsakSluttdato')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 136, 2)
    _Documentation = None
AarsakSluttdato._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'AarsakSluttdato', AarsakSluttdato)
_module_typeBindings.AarsakSluttdato = AarsakSluttdato

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Ansettelsesform
class Ansettelsesform (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Ansettelsesform')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 139, 2)
    _Documentation = None
Ansettelsesform._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Ansettelsesform', Ansettelsesform)
_module_typeBindings.Ansettelsesform = Ansettelsesform

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Skipsregister
class Skipsregister (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Skipsregister')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 149, 2)
    _Documentation = None
Skipsregister._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Skipsregister', Skipsregister)
_module_typeBindings.Skipsregister = Skipsregister

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Skipstype
class Skipstype (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Skipstype')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 152, 2)
    _Documentation = None
Skipstype._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Skipstype', Skipstype)
_module_typeBindings.Skipstype = Skipstype

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Fartsomraade
class Fartsomraade (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Fartsomraade')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 155, 2)
    _Documentation = None
Fartsomraade._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Fartsomraade', Fartsomraade)
_module_typeBindings.Fartsomraade = Fartsomraade

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}PermisjonsOgPermitteringsBeskrivelse
class PermisjonsOgPermitteringsBeskrivelse (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PermisjonsOgPermitteringsBeskrivelse')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 158, 2)
    _Documentation = None
PermisjonsOgPermitteringsBeskrivelse._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'PermisjonsOgPermitteringsBeskrivelse', PermisjonsOgPermitteringsBeskrivelse)
_module_typeBindings.PermisjonsOgPermitteringsBeskrivelse = PermisjonsOgPermitteringsBeskrivelse

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Fradragsbeskrivelse
class Fradragsbeskrivelse (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Fradragsbeskrivelse')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 176, 2)
    _Documentation = None
Fradragsbeskrivelse._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Fradragsbeskrivelse', Fradragsbeskrivelse)
_module_typeBindings.Fradragsbeskrivelse = Fradragsbeskrivelse

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Forskuddstrekksbeskrivelse
class Forskuddstrekksbeskrivelse (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Forskuddstrekksbeskrivelse')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 185, 2)
    _Documentation = None
Forskuddstrekksbeskrivelse._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Forskuddstrekksbeskrivelse', Forskuddstrekksbeskrivelse)
_module_typeBindings.Forskuddstrekksbeskrivelse = Forskuddstrekksbeskrivelse

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}SkatteOgAvgiftsregel
class SkatteOgAvgiftsregel (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SkatteOgAvgiftsregel')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 206, 2)
    _Documentation = None
SkatteOgAvgiftsregel._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'SkatteOgAvgiftsregel', SkatteOgAvgiftsregel)
_module_typeBindings.SkatteOgAvgiftsregel = SkatteOgAvgiftsregel

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Fordel
class Fordel (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Fordel')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 209, 2)
    _Documentation = None
Fordel._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Fordel', Fordel)
_module_typeBindings.Fordel = Fordel

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Loennsbeskrivelse
class Loennsbeskrivelse (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Loennsbeskrivelse')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 220, 2)
    _Documentation = None
Loennsbeskrivelse._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Loennsbeskrivelse', Loennsbeskrivelse)
_module_typeBindings.Loennsbeskrivelse = Loennsbeskrivelse

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}PersontypeForReiseKostLosji
class PersontypeForReiseKostLosji (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PersontypeForReiseKostLosji')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 258, 2)
    _Documentation = None
PersontypeForReiseKostLosji._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'PersontypeForReiseKostLosji', PersontypeForReiseKostLosji)
_module_typeBindings.PersontypeForReiseKostLosji = PersontypeForReiseKostLosji

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}SpesielleInntjeningsforhold
class SpesielleInntjeningsforhold (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpesielleInntjeningsforhold')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 273, 2)
    _Documentation = None
SpesielleInntjeningsforhold._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'SpesielleInntjeningsforhold', SpesielleInntjeningsforhold)
_module_typeBindings.SpesielleInntjeningsforhold = SpesielleInntjeningsforhold

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}YtelseFraOffentligeBeskrivelse
class YtelseFraOffentligeBeskrivelse (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'YtelseFraOffentligeBeskrivelse')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 335, 2)
    _Documentation = None
YtelseFraOffentligeBeskrivelse._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'YtelseFraOffentligeBeskrivelse', YtelseFraOffentligeBeskrivelse)
_module_typeBindings.YtelseFraOffentligeBeskrivelse = YtelseFraOffentligeBeskrivelse

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}PensjonEllerTrygdebeskrivelse
class PensjonEllerTrygdebeskrivelse (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PensjonEllerTrygdebeskrivelse')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 344, 2)
    _Documentation = None
PensjonEllerTrygdebeskrivelse._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'PensjonEllerTrygdebeskrivelse', PensjonEllerTrygdebeskrivelse)
_module_typeBindings.PensjonEllerTrygdebeskrivelse = PensjonEllerTrygdebeskrivelse

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Naeringsinntektsbeskrivelse
class Naeringsinntektsbeskrivelse (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Naeringsinntektsbeskrivelse')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 353, 2)
    _Documentation = None
Naeringsinntektsbeskrivelse._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Naeringsinntektsbeskrivelse', Naeringsinntektsbeskrivelse)
_module_typeBindings.Naeringsinntektsbeskrivelse = Naeringsinntektsbeskrivelse

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}OppholdsbeskrivelseForSvalbardJanMayenOgBilandene
class OppholdsbeskrivelseForSvalbardJanMayenOgBilandene (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OppholdsbeskrivelseForSvalbardJanMayenOgBilandene')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 356, 2)
    _Documentation = None
OppholdsbeskrivelseForSvalbardJanMayenOgBilandene._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'OppholdsbeskrivelseForSvalbardJanMayenOgBilandene', OppholdsbeskrivelseForSvalbardJanMayenOgBilandene)
_module_typeBindings.OppholdsbeskrivelseForSvalbardJanMayenOgBilandene = OppholdsbeskrivelseForSvalbardJanMayenOgBilandene

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Utleggstrekkbeskrivelse
class Utleggstrekkbeskrivelse (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Utleggstrekkbeskrivelse')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 379, 2)
    _Documentation = None
Utleggstrekkbeskrivelse._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Utleggstrekkbeskrivelse', Utleggstrekkbeskrivelse)
_module_typeBindings.Utleggstrekkbeskrivelse = Utleggstrekkbeskrivelse

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}BeregningskodeForArbeidsgiveravgift
class BeregningskodeForArbeidsgiveravgift (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BeregningskodeForArbeidsgiveravgift')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 400, 2)
    _Documentation = None
BeregningskodeForArbeidsgiveravgift._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'BeregningskodeForArbeidsgiveravgift', BeregningskodeForArbeidsgiveravgift)
_module_typeBindings.BeregningskodeForArbeidsgiveravgift = BeregningskodeForArbeidsgiveravgift

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Arbeidsgiveravgiftsone
class Arbeidsgiveravgiftsone (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Arbeidsgiveravgiftsone')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 403, 2)
    _Documentation = None
Arbeidsgiveravgiftsone._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Arbeidsgiveravgiftsone', Arbeidsgiveravgiftsone)
_module_typeBindings.Arbeidsgiveravgiftsone = Arbeidsgiveravgiftsone

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Grunnlagsprosent
class Grunnlagsprosent (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Grunnlagsprosent')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 406, 2)
    _Documentation = None
Grunnlagsprosent._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Grunnlagsprosent', Grunnlagsprosent)
_module_typeBindings.Grunnlagsprosent = Grunnlagsprosent

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}GrunnlagsprosentForUtenlandske
class GrunnlagsprosentForUtenlandske (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GrunnlagsprosentForUtenlandske')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 409, 2)
    _Documentation = None
GrunnlagsprosentForUtenlandske._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'GrunnlagsprosentForUtenlandske', GrunnlagsprosentForUtenlandske)
_module_typeBindings.GrunnlagsprosentForUtenlandske = GrunnlagsprosentForUtenlandske

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}GrunnlagsbeloepForUtenlandske
class GrunnlagsbeloepForUtenlandske (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GrunnlagsbeloepForUtenlandske')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 412, 2)
    _Documentation = None
GrunnlagsbeloepForUtenlandske._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'GrunnlagsbeloepForUtenlandske', GrunnlagsbeloepForUtenlandske)
_module_typeBindings.GrunnlagsbeloepForUtenlandske = GrunnlagsbeloepForUtenlandske

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}DatoTid
class DatoTid (pyxb.binding.datatypes.dateTime):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoTid')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 441, 2)
    _Documentation = None
DatoTid._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'DatoTid', DatoTid)
_module_typeBindings.DatoTid = DatoTid

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}AArOgMaaned
class AArOgMaaned (pyxb.binding.datatypes.gYearMonth):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AArOgMaaned')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 444, 2)
    _Documentation = None
AArOgMaaned._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'AArOgMaaned', AArOgMaaned)
_module_typeBindings.AArOgMaaned = AArOgMaaned

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Tekst
class Tekst (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Tekst')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 447, 2)
    _Documentation = None
Tekst._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Tekst', Tekst)
_module_typeBindings.Tekst = Tekst

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}NorskIdentifikator
class NorskIdentifikator (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NorskIdentifikator')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 450, 2)
    _Documentation = None
NorskIdentifikator._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'NorskIdentifikator', NorskIdentifikator)
_module_typeBindings.NorskIdentifikator = NorskIdentifikator

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}BeloepSomHeltall
class BeloepSomHeltall (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BeloepSomHeltall')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 453, 2)
    _Documentation = None
BeloepSomHeltall._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'BeloepSomHeltall', BeloepSomHeltall)
_module_typeBindings.BeloepSomHeltall = BeloepSomHeltall

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Beloep
class Beloep (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Beloep')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 456, 2)
    _Documentation = None
Beloep._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Beloep', Beloep)
_module_typeBindings.Beloep = Beloep

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Dato
class Dato (pyxb.binding.datatypes.date):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Dato')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 459, 2)
    _Documentation = None
Dato._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Dato', Dato)
_module_typeBindings.Dato = Dato

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Desimaltall
class Desimaltall (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Desimaltall')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 462, 2)
    _Documentation = None
Desimaltall._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Desimaltall', Desimaltall)
_module_typeBindings.Desimaltall = Desimaltall

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Boolsk
class Boolsk (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Boolsk')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 465, 2)
    _Documentation = None
Boolsk._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Boolsk', Boolsk)
_module_typeBindings.Boolsk = Boolsk

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Heltall
class Heltall (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Heltall')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 468, 2)
    _Documentation = None
Heltall._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Heltall', Heltall)
_module_typeBindings.Heltall = Heltall

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}AArstall
class AArstall (pyxb.binding.datatypes.gYear):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AArstall')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 471, 2)
    _Documentation = None
AArstall._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'AArstall', AArstall)
_module_typeBindings.AArstall = AArstall

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Spraak
class Spraak (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Spraak')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 474, 2)
    _Documentation = None
Spraak._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Spraak, enum_prefix=None)
Spraak.bokmaal = Spraak._CF_enumeration.addEnumeration(unicode_value='bokmaal', tag='bokmaal')
Spraak.nynorsk = Spraak._CF_enumeration.addEnumeration(unicode_value='nynorsk', tag='nynorsk')
Spraak.engelsk = Spraak._CF_enumeration.addEnumeration(unicode_value='engelsk', tag='engelsk')
Spraak._InitializeFacetMap(Spraak._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Spraak', Spraak)
_module_typeBindings.Spraak = Spraak

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}RestriksjonTekstfelt
class RestriksjonTekstfelt (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RestriksjonTekstfelt')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 484, 2)
    _Documentation = None
RestriksjonTekstfelt._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
RestriksjonTekstfelt._InitializeFacetMap(RestriksjonTekstfelt._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'RestriksjonTekstfelt', RestriksjonTekstfelt)
_module_typeBindings.RestriksjonTekstfelt = RestriksjonTekstfelt

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}RestriksjonIdentifikator
class RestriksjonIdentifikator (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RestriksjonIdentifikator')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 492, 2)
    _Documentation = None
RestriksjonIdentifikator._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(150))
RestriksjonIdentifikator._CF_pattern = pyxb.binding.facets.CF_pattern()
RestriksjonIdentifikator._CF_pattern.addPattern(pattern='([0-9a-zA-Z_.-])*')
RestriksjonIdentifikator._InitializeFacetMap(RestriksjonIdentifikator._CF_maxLength,
   RestriksjonIdentifikator._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RestriksjonIdentifikator', RestriksjonIdentifikator)
_module_typeBindings.RestriksjonIdentifikator = RestriksjonIdentifikator

# Atomic simple type: [anonymous]
class STD_ANON (AArOgMaaned):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 13, 8)
    _Documentation = None
STD_ANON._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.gYearMonth('2014-01'))
STD_ANON._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.gYearMonth('2099-12'))
STD_ANON._InitializeFacetMap(STD_ANON._CF_minInclusive,
   STD_ANON._CF_maxInclusive)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}TekstMedRestriksjon
class TekstMedRestriksjon (RestriksjonTekstfelt):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TekstMedRestriksjon')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 481, 2)
    _Documentation = None
TekstMedRestriksjon._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'TekstMedRestriksjon', TekstMedRestriksjon)
_module_typeBindings.TekstMedRestriksjon = TekstMedRestriksjon

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Identifikator
class Identifikator (RestriksjonIdentifikator):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Identifikator')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 489, 2)
    _Documentation = None
Identifikator._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Identifikator', Identifikator)
_module_typeBindings.Identifikator = Identifikator

# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}EDAG_M with content type ELEMENT_ONLY
class EDAG_M (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}EDAG_M with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EDAG_M')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 4, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Leveranse uses Python identifier Leveranse
    __Leveranse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Leveranse'), 'Leveranse', '__urnskefastsettinginnsamlinga_meldingenv2_2_EDAG_M_urnskefastsettinginnsamlinga_meldingenv2_2Leveranse', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 6, 6), )

    
    Leveranse = property(__Leveranse.value, __Leveranse.set, None, None)

    _ElementMap.update({
        __Leveranse.name() : __Leveranse
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.EDAG_M = EDAG_M
Namespace.addCategoryObject('typeBinding', 'EDAG_M', EDAG_M)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Leveranse with content type ELEMENT_ONLY
class Leveranse (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Leveranse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Leveranse')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 9, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}leveringstidspunkt uses Python identifier leveringstidspunkt
    __leveringstidspunkt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'leveringstidspunkt'), 'leveringstidspunkt', '__urnskefastsettinginnsamlinga_meldingenv2_2_Leveranse_urnskefastsettinginnsamlinga_meldingenv2_2leveringstidspunkt', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 11, 6), )

    
    leveringstidspunkt = property(__leveringstidspunkt.value, __leveringstidspunkt.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}kalendermaaned uses Python identifier kalendermaaned
    __kalendermaaned = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'kalendermaaned'), 'kalendermaaned', '__urnskefastsettinginnsamlinga_meldingenv2_2_Leveranse_urnskefastsettinginnsamlinga_meldingenv2_2kalendermaaned', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 12, 6), )

    
    kalendermaaned = property(__kalendermaaned.value, __kalendermaaned.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}kildesystem uses Python identifier kildesystem
    __kildesystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'kildesystem'), 'kildesystem', '__urnskefastsettinginnsamlinga_meldingenv2_2_Leveranse_urnskefastsettinginnsamlinga_meldingenv2_2kildesystem', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 20, 6), )

    
    kildesystem = property(__kildesystem.value, __kildesystem.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}erstatterMeldingsId uses Python identifier erstatterMeldingsId
    __erstatterMeldingsId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'erstatterMeldingsId'), 'erstatterMeldingsId', '__urnskefastsettinginnsamlinga_meldingenv2_2_Leveranse_urnskefastsettinginnsamlinga_meldingenv2_2erstatterMeldingsId', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 21, 6), )

    
    erstatterMeldingsId = property(__erstatterMeldingsId.value, __erstatterMeldingsId.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}meldingsId uses Python identifier meldingsId
    __meldingsId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'meldingsId'), 'meldingsId', '__urnskefastsettinginnsamlinga_meldingenv2_2_Leveranse_urnskefastsettinginnsamlinga_meldingenv2_2meldingsId', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 22, 6), )

    
    meldingsId = property(__meldingsId.value, __meldingsId.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}opplysningspliktig uses Python identifier opplysningspliktig
    __opplysningspliktig = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'opplysningspliktig'), 'opplysningspliktig', '__urnskefastsettinginnsamlinga_meldingenv2_2_Leveranse_urnskefastsettinginnsamlinga_meldingenv2_2opplysningspliktig', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 23, 6), )

    
    opplysningspliktig = property(__opplysningspliktig.value, __opplysningspliktig.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}oppgave uses Python identifier oppgave
    __oppgave = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'oppgave'), 'oppgave', '__urnskefastsettinginnsamlinga_meldingenv2_2_Leveranse_urnskefastsettinginnsamlinga_meldingenv2_2oppgave', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 24, 6), )

    
    oppgave = property(__oppgave.value, __oppgave.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}spraakForTilbakemelding uses Python identifier spraakForTilbakemelding
    __spraakForTilbakemelding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'spraakForTilbakemelding'), 'spraakForTilbakemelding', '__urnskefastsettinginnsamlinga_meldingenv2_2_Leveranse_urnskefastsettinginnsamlinga_meldingenv2_2spraakForTilbakemelding', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 25, 6), )

    
    spraakForTilbakemelding = property(__spraakForTilbakemelding.value, __spraakForTilbakemelding.set, None, None)

    _ElementMap.update({
        __leveringstidspunkt.name() : __leveringstidspunkt,
        __kalendermaaned.name() : __kalendermaaned,
        __kildesystem.name() : __kildesystem,
        __erstatterMeldingsId.name() : __erstatterMeldingsId,
        __meldingsId.name() : __meldingsId,
        __opplysningspliktig.name() : __opplysningspliktig,
        __oppgave.name() : __oppgave,
        __spraakForTilbakemelding.name() : __spraakForTilbakemelding
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Leveranse = Leveranse
Namespace.addCategoryObject('typeBinding', 'Leveranse', Leveranse)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Opplysningspliktig with content type ELEMENT_ONLY
class Opplysningspliktig (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Opplysningspliktig with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Opplysningspliktig')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 28, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}norskIdentifikator uses Python identifier norskIdentifikator
    __norskIdentifikator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'norskIdentifikator'), 'norskIdentifikator', '__urnskefastsettinginnsamlinga_meldingenv2_2_Opplysningspliktig_urnskefastsettinginnsamlinga_meldingenv2_2norskIdentifikator', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 30, 6), )

    
    norskIdentifikator = property(__norskIdentifikator.value, __norskIdentifikator.set, None, None)

    _ElementMap.update({
        __norskIdentifikator.name() : __norskIdentifikator
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Opplysningspliktig = Opplysningspliktig
Namespace.addCategoryObject('typeBinding', 'Opplysningspliktig', Opplysningspliktig)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}JuridiskEntitet with content type ELEMENT_ONLY
class JuridiskEntitet (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}JuridiskEntitet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'JuridiskEntitet')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 33, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}betalingsinformasjon uses Python identifier betalingsinformasjon
    __betalingsinformasjon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'betalingsinformasjon'), 'betalingsinformasjon', '__urnskefastsettinginnsamlinga_meldingenv2_2_JuridiskEntitet_urnskefastsettinginnsamlinga_meldingenv2_2betalingsinformasjon', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 35, 6), )

    
    betalingsinformasjon = property(__betalingsinformasjon.value, __betalingsinformasjon.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}betalingsinformasjonForForenkletOrdning uses Python identifier betalingsinformasjonForForenkletOrdning
    __betalingsinformasjonForForenkletOrdning = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'betalingsinformasjonForForenkletOrdning'), 'betalingsinformasjonForForenkletOrdning', '__urnskefastsettinginnsamlinga_meldingenv2_2_JuridiskEntitet_urnskefastsettinginnsamlinga_meldingenv2_2betalingsinformasjonForForenkletOrdning', True, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 36, 6), )

    
    betalingsinformasjonForForenkletOrdning = property(__betalingsinformasjonForForenkletOrdning.value, __betalingsinformasjonForForenkletOrdning.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}annenBagatellmessigStoette uses Python identifier annenBagatellmessigStoette
    __annenBagatellmessigStoette = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annenBagatellmessigStoette'), 'annenBagatellmessigStoette', '__urnskefastsettinginnsamlinga_meldingenv2_2_JuridiskEntitet_urnskefastsettinginnsamlinga_meldingenv2_2annenBagatellmessigStoette', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 37, 6), )

    
    annenBagatellmessigStoette = property(__annenBagatellmessigStoette.value, __annenBagatellmessigStoette.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}virksomhet uses Python identifier virksomhet
    __virksomhet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'virksomhet'), 'virksomhet', '__urnskefastsettinginnsamlinga_meldingenv2_2_JuridiskEntitet_urnskefastsettinginnsamlinga_meldingenv2_2virksomhet', True, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 38, 6), )

    
    virksomhet = property(__virksomhet.value, __virksomhet.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}pensjonsinnretning uses Python identifier pensjonsinnretning
    __pensjonsinnretning = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pensjonsinnretning'), 'pensjonsinnretning', '__urnskefastsettinginnsamlinga_meldingenv2_2_JuridiskEntitet_urnskefastsettinginnsamlinga_meldingenv2_2pensjonsinnretning', True, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 39, 6), )

    
    pensjonsinnretning = property(__pensjonsinnretning.value, __pensjonsinnretning.set, None, None)

    _ElementMap.update({
        __betalingsinformasjon.name() : __betalingsinformasjon,
        __betalingsinformasjonForForenkletOrdning.name() : __betalingsinformasjonForForenkletOrdning,
        __annenBagatellmessigStoette.name() : __annenBagatellmessigStoette,
        __virksomhet.name() : __virksomhet,
        __pensjonsinnretning.name() : __pensjonsinnretning
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.JuridiskEntitet = JuridiskEntitet
Namespace.addCategoryObject('typeBinding', 'JuridiskEntitet', JuridiskEntitet)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Betalingsinformasjon with content type ELEMENT_ONLY
class Betalingsinformasjon (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Betalingsinformasjon with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Betalingsinformasjon')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 42, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}sumForskuddstrekk uses Python identifier sumForskuddstrekk
    __sumForskuddstrekk = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sumForskuddstrekk'), 'sumForskuddstrekk', '__urnskefastsettinginnsamlinga_meldingenv2_2_Betalingsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_2sumForskuddstrekk', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 44, 6), )

    
    sumForskuddstrekk = property(__sumForskuddstrekk.value, __sumForskuddstrekk.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}sumArbeidsgiveravgift uses Python identifier sumArbeidsgiveravgift
    __sumArbeidsgiveravgift = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sumArbeidsgiveravgift'), 'sumArbeidsgiveravgift', '__urnskefastsettinginnsamlinga_meldingenv2_2_Betalingsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_2sumArbeidsgiveravgift', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 45, 6), )

    
    sumArbeidsgiveravgift = property(__sumArbeidsgiveravgift.value, __sumArbeidsgiveravgift.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}sumFinansskattLoenn uses Python identifier sumFinansskattLoenn
    __sumFinansskattLoenn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sumFinansskattLoenn'), 'sumFinansskattLoenn', '__urnskefastsettinginnsamlinga_meldingenv2_2_Betalingsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_2sumFinansskattLoenn', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 46, 6), )

    
    sumFinansskattLoenn = property(__sumFinansskattLoenn.value, __sumFinansskattLoenn.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}sumUtleggstrekk uses Python identifier sumUtleggstrekk
    __sumUtleggstrekk = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sumUtleggstrekk'), 'sumUtleggstrekk', '__urnskefastsettinginnsamlinga_meldingenv2_2_Betalingsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_2sumUtleggstrekk', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 47, 6), )

    
    sumUtleggstrekk = property(__sumUtleggstrekk.value, __sumUtleggstrekk.set, None, None)

    _ElementMap.update({
        __sumForskuddstrekk.name() : __sumForskuddstrekk,
        __sumArbeidsgiveravgift.name() : __sumArbeidsgiveravgift,
        __sumFinansskattLoenn.name() : __sumFinansskattLoenn,
        __sumUtleggstrekk.name() : __sumUtleggstrekk
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Betalingsinformasjon = Betalingsinformasjon
Namespace.addCategoryObject('typeBinding', 'Betalingsinformasjon', Betalingsinformasjon)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}BetalingsinformasjonForForenkletOrdning with content type ELEMENT_ONLY
class BetalingsinformasjonForForenkletOrdning (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}BetalingsinformasjonForForenkletOrdning with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BetalingsinformasjonForForenkletOrdning')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 50, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}sumForskuddstrekk uses Python identifier sumForskuddstrekk
    __sumForskuddstrekk = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sumForskuddstrekk'), 'sumForskuddstrekk', '__urnskefastsettinginnsamlinga_meldingenv2_2_BetalingsinformasjonForForenkletOrdning_urnskefastsettinginnsamlinga_meldingenv2_2sumForskuddstrekk', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 52, 6), )

    
    sumForskuddstrekk = property(__sumForskuddstrekk.value, __sumForskuddstrekk.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}sumArbeidsgiveravgift uses Python identifier sumArbeidsgiveravgift
    __sumArbeidsgiveravgift = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sumArbeidsgiveravgift'), 'sumArbeidsgiveravgift', '__urnskefastsettinginnsamlinga_meldingenv2_2_BetalingsinformasjonForForenkletOrdning_urnskefastsettinginnsamlinga_meldingenv2_2sumArbeidsgiveravgift', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 53, 6), )

    
    sumArbeidsgiveravgift = property(__sumArbeidsgiveravgift.value, __sumArbeidsgiveravgift.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}loennsutbetalingsdato uses Python identifier loennsutbetalingsdato
    __loennsutbetalingsdato = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'loennsutbetalingsdato'), 'loennsutbetalingsdato', '__urnskefastsettinginnsamlinga_meldingenv2_2_BetalingsinformasjonForForenkletOrdning_urnskefastsettinginnsamlinga_meldingenv2_2loennsutbetalingsdato', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 54, 6), )

    
    loennsutbetalingsdato = property(__loennsutbetalingsdato.value, __loennsutbetalingsdato.set, None, None)

    _ElementMap.update({
        __sumForskuddstrekk.name() : __sumForskuddstrekk,
        __sumArbeidsgiveravgift.name() : __sumArbeidsgiveravgift,
        __loennsutbetalingsdato.name() : __loennsutbetalingsdato
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BetalingsinformasjonForForenkletOrdning = BetalingsinformasjonForForenkletOrdning
Namespace.addCategoryObject('typeBinding', 'BetalingsinformasjonForForenkletOrdning', BetalingsinformasjonForForenkletOrdning)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Virksomhet with content type ELEMENT_ONLY
class Virksomhet (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Virksomhet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Virksomhet')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 57, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}norskIdentifikator uses Python identifier norskIdentifikator
    __norskIdentifikator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'norskIdentifikator'), 'norskIdentifikator', '__urnskefastsettinginnsamlinga_meldingenv2_2_Virksomhet_urnskefastsettinginnsamlinga_meldingenv2_2norskIdentifikator', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 59, 6), )

    
    norskIdentifikator = property(__norskIdentifikator.value, __norskIdentifikator.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}inntektsmottaker uses Python identifier inntektsmottaker
    __inntektsmottaker = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inntektsmottaker'), 'inntektsmottaker', '__urnskefastsettinginnsamlinga_meldingenv2_2_Virksomhet_urnskefastsettinginnsamlinga_meldingenv2_2inntektsmottaker', True, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 60, 6), )

    
    inntektsmottaker = property(__inntektsmottaker.value, __inntektsmottaker.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}arbeidsgiveravgift uses Python identifier arbeidsgiveravgift
    __arbeidsgiveravgift = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'arbeidsgiveravgift'), 'arbeidsgiveravgift', '__urnskefastsettinginnsamlinga_meldingenv2_2_Virksomhet_urnskefastsettinginnsamlinga_meldingenv2_2arbeidsgiveravgift', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 61, 6), )

    
    arbeidsgiveravgift = property(__arbeidsgiveravgift.value, __arbeidsgiveravgift.set, None, None)

    _ElementMap.update({
        __norskIdentifikator.name() : __norskIdentifikator,
        __inntektsmottaker.name() : __inntektsmottaker,
        __arbeidsgiveravgift.name() : __arbeidsgiveravgift
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Virksomhet = Virksomhet
Namespace.addCategoryObject('typeBinding', 'Virksomhet', Virksomhet)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Pensjonsinnretning with content type ELEMENT_ONLY
class Pensjonsinnretning (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Pensjonsinnretning with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Pensjonsinnretning')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 64, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}identifikator uses Python identifier identifikator
    __identifikator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'identifikator'), 'identifikator', '__urnskefastsettinginnsamlinga_meldingenv2_2_Pensjonsinnretning_urnskefastsettinginnsamlinga_meldingenv2_2identifikator', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 66, 6), )

    
    identifikator = property(__identifikator.value, __identifikator.set, None, None)

    _ElementMap.update({
        __identifikator.name() : __identifikator
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Pensjonsinnretning = Pensjonsinnretning
Namespace.addCategoryObject('typeBinding', 'Pensjonsinnretning', Pensjonsinnretning)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Inntektsmottaker with content type ELEMENT_ONLY
class Inntektsmottaker (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Inntektsmottaker with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Inntektsmottaker')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 69, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}norskIdentifikator uses Python identifier norskIdentifikator
    __norskIdentifikator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'norskIdentifikator'), 'norskIdentifikator', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntektsmottaker_urnskefastsettinginnsamlinga_meldingenv2_2norskIdentifikator', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 71, 6), )

    
    norskIdentifikator = property(__norskIdentifikator.value, __norskIdentifikator.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}internasjonalIdentifikator uses Python identifier internasjonalIdentifikator
    __internasjonalIdentifikator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'internasjonalIdentifikator'), 'internasjonalIdentifikator', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntektsmottaker_urnskefastsettinginnsamlinga_meldingenv2_2internasjonalIdentifikator', True, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 72, 6), )

    
    internasjonalIdentifikator = property(__internasjonalIdentifikator.value, __internasjonalIdentifikator.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}identifiserendeInformasjon uses Python identifier identifiserendeInformasjon
    __identifiserendeInformasjon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'identifiserendeInformasjon'), 'identifiserendeInformasjon', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntektsmottaker_urnskefastsettinginnsamlinga_meldingenv2_2identifiserendeInformasjon', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 73, 6), )

    
    identifiserendeInformasjon = property(__identifiserendeInformasjon.value, __identifiserendeInformasjon.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}arbeidsforhold uses Python identifier arbeidsforhold
    __arbeidsforhold = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'arbeidsforhold'), 'arbeidsforhold', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntektsmottaker_urnskefastsettinginnsamlinga_meldingenv2_2arbeidsforhold', True, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 74, 6), )

    
    arbeidsforhold = property(__arbeidsforhold.value, __arbeidsforhold.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}fradrag uses Python identifier fradrag
    __fradrag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fradrag'), 'fradrag', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntektsmottaker_urnskefastsettinginnsamlinga_meldingenv2_2fradrag', True, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 75, 6), )

    
    fradrag = property(__fradrag.value, __fradrag.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}forskuddstrekk uses Python identifier forskuddstrekk
    __forskuddstrekk = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'forskuddstrekk'), 'forskuddstrekk', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntektsmottaker_urnskefastsettinginnsamlinga_meldingenv2_2forskuddstrekk', True, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 76, 6), )

    
    forskuddstrekk = property(__forskuddstrekk.value, __forskuddstrekk.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}inntekt uses Python identifier inntekt
    __inntekt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inntekt'), 'inntekt', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntektsmottaker_urnskefastsettinginnsamlinga_meldingenv2_2inntekt', True, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 77, 6), )

    
    inntekt = property(__inntekt.value, __inntekt.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}sjoefolksrelatertInformasjon uses Python identifier sjoefolksrelatertInformasjon
    __sjoefolksrelatertInformasjon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sjoefolksrelatertInformasjon'), 'sjoefolksrelatertInformasjon', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntektsmottaker_urnskefastsettinginnsamlinga_meldingenv2_2sjoefolksrelatertInformasjon', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 78, 6), )

    
    sjoefolksrelatertInformasjon = property(__sjoefolksrelatertInformasjon.value, __sjoefolksrelatertInformasjon.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}oppholdPaaSvalbardJanMayenOgBilandene uses Python identifier oppholdPaaSvalbardJanMayenOgBilandene
    __oppholdPaaSvalbardJanMayenOgBilandene = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'oppholdPaaSvalbardJanMayenOgBilandene'), 'oppholdPaaSvalbardJanMayenOgBilandene', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntektsmottaker_urnskefastsettinginnsamlinga_meldingenv2_2oppholdPaaSvalbardJanMayenOgBilandene', True, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 79, 6), )

    
    oppholdPaaSvalbardJanMayenOgBilandene = property(__oppholdPaaSvalbardJanMayenOgBilandene.value, __oppholdPaaSvalbardJanMayenOgBilandene.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}utleggstrekk uses Python identifier utleggstrekk
    __utleggstrekk = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'utleggstrekk'), 'utleggstrekk', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntektsmottaker_urnskefastsettinginnsamlinga_meldingenv2_2utleggstrekk', True, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 80, 6), )

    
    utleggstrekk = property(__utleggstrekk.value, __utleggstrekk.set, None, None)

    _ElementMap.update({
        __norskIdentifikator.name() : __norskIdentifikator,
        __internasjonalIdentifikator.name() : __internasjonalIdentifikator,
        __identifiserendeInformasjon.name() : __identifiserendeInformasjon,
        __arbeidsforhold.name() : __arbeidsforhold,
        __fradrag.name() : __fradrag,
        __forskuddstrekk.name() : __forskuddstrekk,
        __inntekt.name() : __inntekt,
        __sjoefolksrelatertInformasjon.name() : __sjoefolksrelatertInformasjon,
        __oppholdPaaSvalbardJanMayenOgBilandene.name() : __oppholdPaaSvalbardJanMayenOgBilandene,
        __utleggstrekk.name() : __utleggstrekk
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Inntektsmottaker = Inntektsmottaker
Namespace.addCategoryObject('typeBinding', 'Inntektsmottaker', Inntektsmottaker)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}InternasjonalIdentifikator with content type ELEMENT_ONLY
class InternasjonalIdentifikator (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}InternasjonalIdentifikator with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InternasjonalIdentifikator')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 83, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}identifikator uses Python identifier identifikator
    __identifikator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'identifikator'), 'identifikator', '__urnskefastsettinginnsamlinga_meldingenv2_2_InternasjonalIdentifikator_urnskefastsettinginnsamlinga_meldingenv2_2identifikator', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 85, 6), )

    
    identifikator = property(__identifikator.value, __identifikator.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}identifikatortype uses Python identifier identifikatortype
    __identifikatortype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'identifikatortype'), 'identifikatortype', '__urnskefastsettinginnsamlinga_meldingenv2_2_InternasjonalIdentifikator_urnskefastsettinginnsamlinga_meldingenv2_2identifikatortype', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 86, 6), )

    
    identifikatortype = property(__identifikatortype.value, __identifikatortype.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}land uses Python identifier land
    __land = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'land'), 'land', '__urnskefastsettinginnsamlinga_meldingenv2_2_InternasjonalIdentifikator_urnskefastsettinginnsamlinga_meldingenv2_2land', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 87, 6), )

    
    land = property(__land.value, __land.set, None, None)

    _ElementMap.update({
        __identifikator.name() : __identifikator,
        __identifikatortype.name() : __identifikatortype,
        __land.name() : __land
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InternasjonalIdentifikator = InternasjonalIdentifikator
Namespace.addCategoryObject('typeBinding', 'InternasjonalIdentifikator', InternasjonalIdentifikator)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}IdentifiserendeInformasjon with content type ELEMENT_ONLY
class IdentifiserendeInformasjon (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}IdentifiserendeInformasjon with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IdentifiserendeInformasjon')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 96, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}navn uses Python identifier navn
    __navn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'navn'), 'navn', '__urnskefastsettinginnsamlinga_meldingenv2_2_IdentifiserendeInformasjon_urnskefastsettinginnsamlinga_meldingenv2_2navn', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 98, 6), )

    
    navn = property(__navn.value, __navn.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}foedselsdato uses Python identifier foedselsdato
    __foedselsdato = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'foedselsdato'), 'foedselsdato', '__urnskefastsettinginnsamlinga_meldingenv2_2_IdentifiserendeInformasjon_urnskefastsettinginnsamlinga_meldingenv2_2foedselsdato', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 99, 6), )

    
    foedselsdato = property(__foedselsdato.value, __foedselsdato.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}ansattnummer uses Python identifier ansattnummer
    __ansattnummer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ansattnummer'), 'ansattnummer', '__urnskefastsettinginnsamlinga_meldingenv2_2_IdentifiserendeInformasjon_urnskefastsettinginnsamlinga_meldingenv2_2ansattnummer', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 100, 6), )

    
    ansattnummer = property(__ansattnummer.value, __ansattnummer.set, None, None)

    _ElementMap.update({
        __navn.name() : __navn,
        __foedselsdato.name() : __foedselsdato,
        __ansattnummer.name() : __ansattnummer
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.IdentifiserendeInformasjon = IdentifiserendeInformasjon
Namespace.addCategoryObject('typeBinding', 'IdentifiserendeInformasjon', IdentifiserendeInformasjon)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Arbeidsforhold with content type ELEMENT_ONLY
class Arbeidsforhold (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Arbeidsforhold with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Arbeidsforhold')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 103, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}arbeidsforholdId uses Python identifier arbeidsforholdId
    __arbeidsforholdId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'arbeidsforholdId'), 'arbeidsforholdId', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_2arbeidsforholdId', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 105, 6), )

    
    arbeidsforholdId = property(__arbeidsforholdId.value, __arbeidsforholdId.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}typeArbeidsforhold uses Python identifier typeArbeidsforhold
    __typeArbeidsforhold = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'typeArbeidsforhold'), 'typeArbeidsforhold', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_2typeArbeidsforhold', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 106, 6), )

    
    typeArbeidsforhold = property(__typeArbeidsforhold.value, __typeArbeidsforhold.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}startdato uses Python identifier startdato
    __startdato = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startdato'), 'startdato', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_2startdato', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 107, 6), )

    
    startdato = property(__startdato.value, __startdato.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}sluttdato uses Python identifier sluttdato
    __sluttdato = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sluttdato'), 'sluttdato', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_2sluttdato', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 108, 6), )

    
    sluttdato = property(__sluttdato.value, __sluttdato.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}antallTimerPerUkeSomEnFullStillingTilsvarer uses Python identifier antallTimerPerUkeSomEnFullStillingTilsvarer
    __antallTimerPerUkeSomEnFullStillingTilsvarer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'antallTimerPerUkeSomEnFullStillingTilsvarer'), 'antallTimerPerUkeSomEnFullStillingTilsvarer', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_2antallTimerPerUkeSomEnFullStillingTilsvarer', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 109, 6), )

    
    antallTimerPerUkeSomEnFullStillingTilsvarer = property(__antallTimerPerUkeSomEnFullStillingTilsvarer.value, __antallTimerPerUkeSomEnFullStillingTilsvarer.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}avloenningstype uses Python identifier avloenningstype
    __avloenningstype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avloenningstype'), 'avloenningstype', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_2avloenningstype', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 110, 6), )

    
    avloenningstype = property(__avloenningstype.value, __avloenningstype.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}yrke uses Python identifier yrke
    __yrke = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'yrke'), 'yrke', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_2yrke', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 111, 6), )

    
    yrke = property(__yrke.value, __yrke.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}arbeidstidsordning uses Python identifier arbeidstidsordning
    __arbeidstidsordning = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'arbeidstidsordning'), 'arbeidstidsordning', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_2arbeidstidsordning', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 112, 6), )

    
    arbeidstidsordning = property(__arbeidstidsordning.value, __arbeidstidsordning.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}stillingsprosent uses Python identifier stillingsprosent
    __stillingsprosent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stillingsprosent'), 'stillingsprosent', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_2stillingsprosent', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 113, 6), )

    
    stillingsprosent = property(__stillingsprosent.value, __stillingsprosent.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}sisteLoennsendringsdato uses Python identifier sisteLoennsendringsdato
    __sisteLoennsendringsdato = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sisteLoennsendringsdato'), 'sisteLoennsendringsdato', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_2sisteLoennsendringsdato', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 114, 6), )

    
    sisteLoennsendringsdato = property(__sisteLoennsendringsdato.value, __sisteLoennsendringsdato.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}loennsansiennitet uses Python identifier loennsansiennitet
    __loennsansiennitet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'loennsansiennitet'), 'loennsansiennitet', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_2loennsansiennitet', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 115, 6), )

    
    loennsansiennitet = property(__loennsansiennitet.value, __loennsansiennitet.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}loennstrinn uses Python identifier loennstrinn
    __loennstrinn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'loennstrinn'), 'loennstrinn', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_2loennstrinn', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 116, 6), )

    
    loennstrinn = property(__loennstrinn.value, __loennstrinn.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}fartoey uses Python identifier fartoey
    __fartoey = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fartoey'), 'fartoey', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_2fartoey', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 117, 6), )

    
    fartoey = property(__fartoey.value, __fartoey.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}permisjon uses Python identifier permisjon
    __permisjon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'permisjon'), 'permisjon', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_2permisjon', True, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 118, 6), )

    
    permisjon = property(__permisjon.value, __permisjon.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}sisteDatoForStillingsprosentendring uses Python identifier sisteDatoForStillingsprosentendring
    __sisteDatoForStillingsprosentendring = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sisteDatoForStillingsprosentendring'), 'sisteDatoForStillingsprosentendring', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_2sisteDatoForStillingsprosentendring', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 119, 6), )

    
    sisteDatoForStillingsprosentendring = property(__sisteDatoForStillingsprosentendring.value, __sisteDatoForStillingsprosentendring.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}aarsakTilSluttdato uses Python identifier aarsakTilSluttdato
    __aarsakTilSluttdato = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'aarsakTilSluttdato'), 'aarsakTilSluttdato', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_2aarsakTilSluttdato', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 120, 6), )

    
    aarsakTilSluttdato = property(__aarsakTilSluttdato.value, __aarsakTilSluttdato.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}formForAnsettelse uses Python identifier formForAnsettelse
    __formForAnsettelse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'formForAnsettelse'), 'formForAnsettelse', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_2formForAnsettelse', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 121, 6), )

    
    formForAnsettelse = property(__formForAnsettelse.value, __formForAnsettelse.set, None, None)

    _ElementMap.update({
        __arbeidsforholdId.name() : __arbeidsforholdId,
        __typeArbeidsforhold.name() : __typeArbeidsforhold,
        __startdato.name() : __startdato,
        __sluttdato.name() : __sluttdato,
        __antallTimerPerUkeSomEnFullStillingTilsvarer.name() : __antallTimerPerUkeSomEnFullStillingTilsvarer,
        __avloenningstype.name() : __avloenningstype,
        __yrke.name() : __yrke,
        __arbeidstidsordning.name() : __arbeidstidsordning,
        __stillingsprosent.name() : __stillingsprosent,
        __sisteLoennsendringsdato.name() : __sisteLoennsendringsdato,
        __loennsansiennitet.name() : __loennsansiennitet,
        __loennstrinn.name() : __loennstrinn,
        __fartoey.name() : __fartoey,
        __permisjon.name() : __permisjon,
        __sisteDatoForStillingsprosentendring.name() : __sisteDatoForStillingsprosentendring,
        __aarsakTilSluttdato.name() : __aarsakTilSluttdato,
        __formForAnsettelse.name() : __formForAnsettelse
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Arbeidsforhold = Arbeidsforhold
Namespace.addCategoryObject('typeBinding', 'Arbeidsforhold', Arbeidsforhold)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Fartoey with content type ELEMENT_ONLY
class Fartoey (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Fartoey with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Fartoey')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 142, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}skipsregister uses Python identifier skipsregister
    __skipsregister = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'skipsregister'), 'skipsregister', '__urnskefastsettinginnsamlinga_meldingenv2_2_Fartoey_urnskefastsettinginnsamlinga_meldingenv2_2skipsregister', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 144, 6), )

    
    skipsregister = property(__skipsregister.value, __skipsregister.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}skipstype uses Python identifier skipstype
    __skipstype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'skipstype'), 'skipstype', '__urnskefastsettinginnsamlinga_meldingenv2_2_Fartoey_urnskefastsettinginnsamlinga_meldingenv2_2skipstype', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 145, 6), )

    
    skipstype = property(__skipstype.value, __skipstype.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}fartsomraade uses Python identifier fartsomraade
    __fartsomraade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fartsomraade'), 'fartsomraade', '__urnskefastsettinginnsamlinga_meldingenv2_2_Fartoey_urnskefastsettinginnsamlinga_meldingenv2_2fartsomraade', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 146, 6), )

    
    fartsomraade = property(__fartsomraade.value, __fartsomraade.set, None, None)

    _ElementMap.update({
        __skipsregister.name() : __skipsregister,
        __skipstype.name() : __skipstype,
        __fartsomraade.name() : __fartsomraade
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Fartoey = Fartoey
Namespace.addCategoryObject('typeBinding', 'Fartoey', Fartoey)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Permisjon with content type ELEMENT_ONLY
class Permisjon (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Permisjon with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Permisjon')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 161, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}startdato uses Python identifier startdato
    __startdato = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startdato'), 'startdato', '__urnskefastsettinginnsamlinga_meldingenv2_2_Permisjon_urnskefastsettinginnsamlinga_meldingenv2_2startdato', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 163, 6), )

    
    startdato = property(__startdato.value, __startdato.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}sluttdato uses Python identifier sluttdato
    __sluttdato = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sluttdato'), 'sluttdato', '__urnskefastsettinginnsamlinga_meldingenv2_2_Permisjon_urnskefastsettinginnsamlinga_meldingenv2_2sluttdato', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 164, 6), )

    
    sluttdato = property(__sluttdato.value, __sluttdato.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}permisjonsprosent uses Python identifier permisjonsprosent
    __permisjonsprosent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'permisjonsprosent'), 'permisjonsprosent', '__urnskefastsettinginnsamlinga_meldingenv2_2_Permisjon_urnskefastsettinginnsamlinga_meldingenv2_2permisjonsprosent', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 165, 6), )

    
    permisjonsprosent = property(__permisjonsprosent.value, __permisjonsprosent.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}permisjonId uses Python identifier permisjonId
    __permisjonId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'permisjonId'), 'permisjonId', '__urnskefastsettinginnsamlinga_meldingenv2_2_Permisjon_urnskefastsettinginnsamlinga_meldingenv2_2permisjonId', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 166, 6), )

    
    permisjonId = property(__permisjonId.value, __permisjonId.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse'), 'beskrivelse', '__urnskefastsettinginnsamlinga_meldingenv2_2_Permisjon_urnskefastsettinginnsamlinga_meldingenv2_2beskrivelse', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 167, 6), )

    
    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    _ElementMap.update({
        __startdato.name() : __startdato,
        __sluttdato.name() : __sluttdato,
        __permisjonsprosent.name() : __permisjonsprosent,
        __permisjonId.name() : __permisjonId,
        __beskrivelse.name() : __beskrivelse
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Permisjon = Permisjon
Namespace.addCategoryObject('typeBinding', 'Permisjon', Permisjon)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Fradrag with content type ELEMENT_ONLY
class Fradrag (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Fradrag with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Fradrag')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 170, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse'), 'beskrivelse', '__urnskefastsettinginnsamlinga_meldingenv2_2_Fradrag_urnskefastsettinginnsamlinga_meldingenv2_2beskrivelse', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 172, 6), )

    
    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}beloep uses Python identifier beloep
    __beloep = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'beloep'), 'beloep', '__urnskefastsettinginnsamlinga_meldingenv2_2_Fradrag_urnskefastsettinginnsamlinga_meldingenv2_2beloep', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 173, 6), )

    
    beloep = property(__beloep.value, __beloep.set, None, None)

    _ElementMap.update({
        __beskrivelse.name() : __beskrivelse,
        __beloep.name() : __beloep
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Fradrag = Fradrag
Namespace.addCategoryObject('typeBinding', 'Fradrag', Fradrag)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Forskuddstrekk with content type ELEMENT_ONLY
class Forskuddstrekk (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Forskuddstrekk with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Forskuddstrekk')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 179, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse'), 'beskrivelse', '__urnskefastsettinginnsamlinga_meldingenv2_2_Forskuddstrekk_urnskefastsettinginnsamlinga_meldingenv2_2beskrivelse', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 181, 6), )

    
    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}beloep uses Python identifier beloep
    __beloep = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'beloep'), 'beloep', '__urnskefastsettinginnsamlinga_meldingenv2_2_Forskuddstrekk_urnskefastsettinginnsamlinga_meldingenv2_2beloep', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 182, 6), )

    
    beloep = property(__beloep.value, __beloep.set, None, None)

    _ElementMap.update({
        __beskrivelse.name() : __beskrivelse,
        __beloep.name() : __beloep
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Forskuddstrekk = Forskuddstrekk
Namespace.addCategoryObject('typeBinding', 'Forskuddstrekk', Forskuddstrekk)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Inntekt with content type ELEMENT_ONLY
class Inntekt (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Inntekt with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Inntekt')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 188, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}skatteOgAvgiftsregel uses Python identifier skatteOgAvgiftsregel
    __skatteOgAvgiftsregel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'skatteOgAvgiftsregel'), 'skatteOgAvgiftsregel', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_2skatteOgAvgiftsregel', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 190, 6), )

    
    skatteOgAvgiftsregel = property(__skatteOgAvgiftsregel.value, __skatteOgAvgiftsregel.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}startdatoOpptjeningsperiode uses Python identifier startdatoOpptjeningsperiode
    __startdatoOpptjeningsperiode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startdatoOpptjeningsperiode'), 'startdatoOpptjeningsperiode', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_2startdatoOpptjeningsperiode', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 191, 6), )

    
    startdatoOpptjeningsperiode = property(__startdatoOpptjeningsperiode.value, __startdatoOpptjeningsperiode.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}sluttdatoOpptjeningsperiode uses Python identifier sluttdatoOpptjeningsperiode
    __sluttdatoOpptjeningsperiode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sluttdatoOpptjeningsperiode'), 'sluttdatoOpptjeningsperiode', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_2sluttdatoOpptjeningsperiode', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 192, 6), )

    
    sluttdatoOpptjeningsperiode = property(__sluttdatoOpptjeningsperiode.value, __sluttdatoOpptjeningsperiode.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}fordel uses Python identifier fordel
    __fordel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fordel'), 'fordel', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_2fordel', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 193, 6), )

    
    fordel = property(__fordel.value, __fordel.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}utloeserArbeidsgiveravgift uses Python identifier utloeserArbeidsgiveravgift
    __utloeserArbeidsgiveravgift = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'utloeserArbeidsgiveravgift'), 'utloeserArbeidsgiveravgift', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_2utloeserArbeidsgiveravgift', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 194, 6), )

    
    utloeserArbeidsgiveravgift = property(__utloeserArbeidsgiveravgift.value, __utloeserArbeidsgiveravgift.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}inngaarIGrunnlagForTrekk uses Python identifier inngaarIGrunnlagForTrekk
    __inngaarIGrunnlagForTrekk = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inngaarIGrunnlagForTrekk'), 'inngaarIGrunnlagForTrekk', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_2inngaarIGrunnlagForTrekk', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 195, 6), )

    
    inngaarIGrunnlagForTrekk = property(__inngaarIGrunnlagForTrekk.value, __inngaarIGrunnlagForTrekk.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}beloep uses Python identifier beloep
    __beloep = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'beloep'), 'beloep', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_2beloep', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 196, 6), )

    
    beloep = property(__beloep.value, __beloep.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}arbeidsforholdId uses Python identifier arbeidsforholdId
    __arbeidsforholdId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'arbeidsforholdId'), 'arbeidsforholdId', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_2arbeidsforholdId', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 197, 6), )

    
    arbeidsforholdId = property(__arbeidsforholdId.value, __arbeidsforholdId.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}loennsinntekt uses Python identifier loennsinntekt
    __loennsinntekt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'loennsinntekt'), 'loennsinntekt', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_2loennsinntekt', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 199, 8), )

    
    loennsinntekt = property(__loennsinntekt.value, __loennsinntekt.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}ytelseFraOffentlige uses Python identifier ytelseFraOffentlige
    __ytelseFraOffentlige = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ytelseFraOffentlige'), 'ytelseFraOffentlige', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_2ytelseFraOffentlige', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 200, 8), )

    
    ytelseFraOffentlige = property(__ytelseFraOffentlige.value, __ytelseFraOffentlige.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}pensjonEllerTrygd uses Python identifier pensjonEllerTrygd
    __pensjonEllerTrygd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pensjonEllerTrygd'), 'pensjonEllerTrygd', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_2pensjonEllerTrygd', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 201, 8), )

    
    pensjonEllerTrygd = property(__pensjonEllerTrygd.value, __pensjonEllerTrygd.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}naeringsinntekt uses Python identifier naeringsinntekt
    __naeringsinntekt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'naeringsinntekt'), 'naeringsinntekt', '__urnskefastsettinginnsamlinga_meldingenv2_2_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_2naeringsinntekt', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 202, 8), )

    
    naeringsinntekt = property(__naeringsinntekt.value, __naeringsinntekt.set, None, None)

    _ElementMap.update({
        __skatteOgAvgiftsregel.name() : __skatteOgAvgiftsregel,
        __startdatoOpptjeningsperiode.name() : __startdatoOpptjeningsperiode,
        __sluttdatoOpptjeningsperiode.name() : __sluttdatoOpptjeningsperiode,
        __fordel.name() : __fordel,
        __utloeserArbeidsgiveravgift.name() : __utloeserArbeidsgiveravgift,
        __inngaarIGrunnlagForTrekk.name() : __inngaarIGrunnlagForTrekk,
        __beloep.name() : __beloep,
        __arbeidsforholdId.name() : __arbeidsforholdId,
        __loennsinntekt.name() : __loennsinntekt,
        __ytelseFraOffentlige.name() : __ytelseFraOffentlige,
        __pensjonEllerTrygd.name() : __pensjonEllerTrygd,
        __naeringsinntekt.name() : __naeringsinntekt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Inntekt = Inntekt
Namespace.addCategoryObject('typeBinding', 'Inntekt', Inntekt)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Loennsinntekt with content type ELEMENT_ONLY
class Loennsinntekt (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Loennsinntekt with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Loennsinntekt')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 212, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse'), 'beskrivelse', '__urnskefastsettinginnsamlinga_meldingenv2_2_Loennsinntekt_urnskefastsettinginnsamlinga_meldingenv2_2beskrivelse', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 214, 6), )

    
    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}tilleggsinformasjon uses Python identifier tilleggsinformasjon
    __tilleggsinformasjon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tilleggsinformasjon'), 'tilleggsinformasjon', '__urnskefastsettinginnsamlinga_meldingenv2_2_Loennsinntekt_urnskefastsettinginnsamlinga_meldingenv2_2tilleggsinformasjon', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 215, 6), )

    
    tilleggsinformasjon = property(__tilleggsinformasjon.value, __tilleggsinformasjon.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}spesifikasjon uses Python identifier spesifikasjon
    __spesifikasjon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'spesifikasjon'), 'spesifikasjon', '__urnskefastsettinginnsamlinga_meldingenv2_2_Loennsinntekt_urnskefastsettinginnsamlinga_meldingenv2_2spesifikasjon', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 216, 6), )

    
    spesifikasjon = property(__spesifikasjon.value, __spesifikasjon.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}antall uses Python identifier antall
    __antall = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'antall'), 'antall', '__urnskefastsettinginnsamlinga_meldingenv2_2_Loennsinntekt_urnskefastsettinginnsamlinga_meldingenv2_2antall', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 217, 6), )

    
    antall = property(__antall.value, __antall.set, None, None)

    _ElementMap.update({
        __beskrivelse.name() : __beskrivelse,
        __tilleggsinformasjon.name() : __tilleggsinformasjon,
        __spesifikasjon.name() : __spesifikasjon,
        __antall.name() : __antall
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Loennsinntekt = Loennsinntekt
Namespace.addCategoryObject('typeBinding', 'Loennsinntekt', Loennsinntekt)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Tilleggsinformasjon with content type ELEMENT_ONLY
class Tilleggsinformasjon (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Tilleggsinformasjon with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Tilleggsinformasjon')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 223, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}bilOgBaat uses Python identifier bilOgBaat
    __bilOgBaat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bilOgBaat'), 'bilOgBaat', '__urnskefastsettinginnsamlinga_meldingenv2_2_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_2bilOgBaat', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 225, 6), )

    
    bilOgBaat = property(__bilOgBaat.value, __bilOgBaat.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}dagmammaIEgenBolig uses Python identifier dagmammaIEgenBolig
    __dagmammaIEgenBolig = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dagmammaIEgenBolig'), 'dagmammaIEgenBolig', '__urnskefastsettinginnsamlinga_meldingenv2_2_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_2dagmammaIEgenBolig', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 226, 6), )

    
    dagmammaIEgenBolig = property(__dagmammaIEgenBolig.value, __dagmammaIEgenBolig.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}etterbetalingsperiode uses Python identifier etterbetalingsperiode
    __etterbetalingsperiode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'etterbetalingsperiode'), 'etterbetalingsperiode', '__urnskefastsettinginnsamlinga_meldingenv2_2_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_2etterbetalingsperiode', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 227, 6), )

    
    etterbetalingsperiode = property(__etterbetalingsperiode.value, __etterbetalingsperiode.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}inntektPaaNorskKontinentalsokkel uses Python identifier inntektPaaNorskKontinentalsokkel
    __inntektPaaNorskKontinentalsokkel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inntektPaaNorskKontinentalsokkel'), 'inntektPaaNorskKontinentalsokkel', '__urnskefastsettinginnsamlinga_meldingenv2_2_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_2inntektPaaNorskKontinentalsokkel', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 228, 6), )

    
    inntektPaaNorskKontinentalsokkel = property(__inntektPaaNorskKontinentalsokkel.value, __inntektPaaNorskKontinentalsokkel.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}inntjeningsforhold uses Python identifier inntjeningsforhold
    __inntjeningsforhold = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inntjeningsforhold'), 'inntjeningsforhold', '__urnskefastsettinginnsamlinga_meldingenv2_2_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_2inntjeningsforhold', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 229, 6), )

    
    inntjeningsforhold = property(__inntjeningsforhold.value, __inntjeningsforhold.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}livrente uses Python identifier livrente
    __livrente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'livrente'), 'livrente', '__urnskefastsettinginnsamlinga_meldingenv2_2_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_2livrente', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 230, 6), )

    
    livrente = property(__livrente.value, __livrente.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}lottOgPart uses Python identifier lottOgPart
    __lottOgPart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lottOgPart'), 'lottOgPart', '__urnskefastsettinginnsamlinga_meldingenv2_2_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_2lottOgPart', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 231, 6), )

    
    lottOgPart = property(__lottOgPart.value, __lottOgPart.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}nettoloenn uses Python identifier nettoloenn
    __nettoloenn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nettoloenn'), 'nettoloenn', '__urnskefastsettinginnsamlinga_meldingenv2_2_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_2nettoloenn', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 232, 6), )

    
    nettoloenn = property(__nettoloenn.value, __nettoloenn.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}pensjon uses Python identifier pensjon
    __pensjon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pensjon'), 'pensjon', '__urnskefastsettinginnsamlinga_meldingenv2_2_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_2pensjon', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 233, 6), )

    
    pensjon = property(__pensjon.value, __pensjon.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}reiseKostOgLosji uses Python identifier reiseKostOgLosji
    __reiseKostOgLosji = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'reiseKostOgLosji'), 'reiseKostOgLosji', '__urnskefastsettinginnsamlinga_meldingenv2_2_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_2reiseKostOgLosji', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 234, 6), )

    
    reiseKostOgLosji = property(__reiseKostOgLosji.value, __reiseKostOgLosji.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}utenlandskArtist uses Python identifier utenlandskArtist
    __utenlandskArtist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'utenlandskArtist'), 'utenlandskArtist', '__urnskefastsettinginnsamlinga_meldingenv2_2_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_2utenlandskArtist', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 235, 6), )

    
    utenlandskArtist = property(__utenlandskArtist.value, __utenlandskArtist.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}bonusFraForsvaret uses Python identifier bonusFraForsvaret
    __bonusFraForsvaret = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bonusFraForsvaret'), 'bonusFraForsvaret', '__urnskefastsettinginnsamlinga_meldingenv2_2_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_2bonusFraForsvaret', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 236, 6), )

    
    bonusFraForsvaret = property(__bonusFraForsvaret.value, __bonusFraForsvaret.set, None, None)

    _ElementMap.update({
        __bilOgBaat.name() : __bilOgBaat,
        __dagmammaIEgenBolig.name() : __dagmammaIEgenBolig,
        __etterbetalingsperiode.name() : __etterbetalingsperiode,
        __inntektPaaNorskKontinentalsokkel.name() : __inntektPaaNorskKontinentalsokkel,
        __inntjeningsforhold.name() : __inntjeningsforhold,
        __livrente.name() : __livrente,
        __lottOgPart.name() : __lottOgPart,
        __nettoloenn.name() : __nettoloenn,
        __pensjon.name() : __pensjon,
        __reiseKostOgLosji.name() : __reiseKostOgLosji,
        __utenlandskArtist.name() : __utenlandskArtist,
        __bonusFraForsvaret.name() : __bonusFraForsvaret
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Tilleggsinformasjon = Tilleggsinformasjon
Namespace.addCategoryObject('typeBinding', 'Tilleggsinformasjon', Tilleggsinformasjon)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Periode with content type ELEMENT_ONLY
class Periode (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Periode with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Periode')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 239, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}startdato uses Python identifier startdato
    __startdato = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startdato'), 'startdato', '__urnskefastsettinginnsamlinga_meldingenv2_2_Periode_urnskefastsettinginnsamlinga_meldingenv2_2startdato', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 241, 6), )

    
    startdato = property(__startdato.value, __startdato.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}sluttdato uses Python identifier sluttdato
    __sluttdato = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sluttdato'), 'sluttdato', '__urnskefastsettinginnsamlinga_meldingenv2_2_Periode_urnskefastsettinginnsamlinga_meldingenv2_2sluttdato', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 242, 6), )

    
    sluttdato = property(__sluttdato.value, __sluttdato.set, None, None)

    _ElementMap.update({
        __startdato.name() : __startdato,
        __sluttdato.name() : __sluttdato
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Periode = Periode
Namespace.addCategoryObject('typeBinding', 'Periode', Periode)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}BilOgBaat with content type ELEMENT_ONLY
class BilOgBaat (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}BilOgBaat with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BilOgBaat')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 245, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}antallKilometer uses Python identifier antallKilometer
    __antallKilometer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'antallKilometer'), 'antallKilometer', '__urnskefastsettinginnsamlinga_meldingenv2_2_BilOgBaat_urnskefastsettinginnsamlinga_meldingenv2_2antallKilometer', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 247, 6), )

    
    antallKilometer = property(__antallKilometer.value, __antallKilometer.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}antallReiser uses Python identifier antallReiser
    __antallReiser = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'antallReiser'), 'antallReiser', '__urnskefastsettinginnsamlinga_meldingenv2_2_BilOgBaat_urnskefastsettinginnsamlinga_meldingenv2_2antallReiser', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 248, 6), )

    
    antallReiser = property(__antallReiser.value, __antallReiser.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}heravAntallKilometerMellomHjemOgArbeid uses Python identifier heravAntallKilometerMellomHjemOgArbeid
    __heravAntallKilometerMellomHjemOgArbeid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heravAntallKilometerMellomHjemOgArbeid'), 'heravAntallKilometerMellomHjemOgArbeid', '__urnskefastsettinginnsamlinga_meldingenv2_2_BilOgBaat_urnskefastsettinginnsamlinga_meldingenv2_2heravAntallKilometerMellomHjemOgArbeid', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 249, 6), )

    
    heravAntallKilometerMellomHjemOgArbeid = property(__heravAntallKilometerMellomHjemOgArbeid.value, __heravAntallKilometerMellomHjemOgArbeid.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}listeprisForBil uses Python identifier listeprisForBil
    __listeprisForBil = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'listeprisForBil'), 'listeprisForBil', '__urnskefastsettinginnsamlinga_meldingenv2_2_BilOgBaat_urnskefastsettinginnsamlinga_meldingenv2_2listeprisForBil', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 250, 6), )

    
    listeprisForBil = property(__listeprisForBil.value, __listeprisForBil.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}bilregistreringsnummer uses Python identifier bilregistreringsnummer
    __bilregistreringsnummer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bilregistreringsnummer'), 'bilregistreringsnummer', '__urnskefastsettinginnsamlinga_meldingenv2_2_BilOgBaat_urnskefastsettinginnsamlinga_meldingenv2_2bilregistreringsnummer', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 251, 6), )

    
    bilregistreringsnummer = property(__bilregistreringsnummer.value, __bilregistreringsnummer.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}erBilpool uses Python identifier erBilpool
    __erBilpool = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'erBilpool'), 'erBilpool', '__urnskefastsettinginnsamlinga_meldingenv2_2_BilOgBaat_urnskefastsettinginnsamlinga_meldingenv2_2erBilpool', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 252, 6), )

    
    erBilpool = property(__erBilpool.value, __erBilpool.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}erAnnenBil uses Python identifier erAnnenBil
    __erAnnenBil = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'erAnnenBil'), 'erAnnenBil', '__urnskefastsettinginnsamlinga_meldingenv2_2_BilOgBaat_urnskefastsettinginnsamlinga_meldingenv2_2erAnnenBil', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 253, 6), )

    
    erAnnenBil = property(__erAnnenBil.value, __erAnnenBil.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}erBilUtenforStandardregelen uses Python identifier erBilUtenforStandardregelen
    __erBilUtenforStandardregelen = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'erBilUtenforStandardregelen'), 'erBilUtenforStandardregelen', '__urnskefastsettinginnsamlinga_meldingenv2_2_BilOgBaat_urnskefastsettinginnsamlinga_meldingenv2_2erBilUtenforStandardregelen', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 254, 6), )

    
    erBilUtenforStandardregelen = property(__erBilUtenforStandardregelen.value, __erBilUtenforStandardregelen.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}personklassifiseringAvBilbruker uses Python identifier personklassifiseringAvBilbruker
    __personklassifiseringAvBilbruker = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'personklassifiseringAvBilbruker'), 'personklassifiseringAvBilbruker', '__urnskefastsettinginnsamlinga_meldingenv2_2_BilOgBaat_urnskefastsettinginnsamlinga_meldingenv2_2personklassifiseringAvBilbruker', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 255, 6), )

    
    personklassifiseringAvBilbruker = property(__personklassifiseringAvBilbruker.value, __personklassifiseringAvBilbruker.set, None, None)

    _ElementMap.update({
        __antallKilometer.name() : __antallKilometer,
        __antallReiser.name() : __antallReiser,
        __heravAntallKilometerMellomHjemOgArbeid.name() : __heravAntallKilometerMellomHjemOgArbeid,
        __listeprisForBil.name() : __listeprisForBil,
        __bilregistreringsnummer.name() : __bilregistreringsnummer,
        __erBilpool.name() : __erBilpool,
        __erAnnenBil.name() : __erAnnenBil,
        __erBilUtenforStandardregelen.name() : __erBilUtenforStandardregelen,
        __personklassifiseringAvBilbruker.name() : __personklassifiseringAvBilbruker
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BilOgBaat = BilOgBaat
Namespace.addCategoryObject('typeBinding', 'BilOgBaat', BilOgBaat)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}DagmammaIEgenBolig with content type ELEMENT_ONLY
class DagmammaIEgenBolig (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}DagmammaIEgenBolig with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DagmammaIEgenBolig')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 261, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}antallBarn uses Python identifier antallBarn
    __antallBarn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'antallBarn'), 'antallBarn', '__urnskefastsettinginnsamlinga_meldingenv2_2_DagmammaIEgenBolig_urnskefastsettinginnsamlinga_meldingenv2_2antallBarn', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 263, 6), )

    
    antallBarn = property(__antallBarn.value, __antallBarn.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}antallMaaneder uses Python identifier antallMaaneder
    __antallMaaneder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'antallMaaneder'), 'antallMaaneder', '__urnskefastsettinginnsamlinga_meldingenv2_2_DagmammaIEgenBolig_urnskefastsettinginnsamlinga_meldingenv2_2antallMaaneder', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 264, 6), )

    
    antallMaaneder = property(__antallMaaneder.value, __antallMaaneder.set, None, None)

    _ElementMap.update({
        __antallBarn.name() : __antallBarn,
        __antallMaaneder.name() : __antallMaaneder
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DagmammaIEgenBolig = DagmammaIEgenBolig
Namespace.addCategoryObject('typeBinding', 'DagmammaIEgenBolig', DagmammaIEgenBolig)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}NorskKontinentalsokkel with content type ELEMENT_ONLY
class NorskKontinentalsokkel (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}NorskKontinentalsokkel with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NorskKontinentalsokkel')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 267, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}tidsrom uses Python identifier tidsrom
    __tidsrom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tidsrom'), 'tidsrom', '__urnskefastsettinginnsamlinga_meldingenv2_2_NorskKontinentalsokkel_urnskefastsettinginnsamlinga_meldingenv2_2tidsrom', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 269, 6), )

    
    tidsrom = property(__tidsrom.value, __tidsrom.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}gjelderLoennFoerste60Dager uses Python identifier gjelderLoennFoerste60Dager
    __gjelderLoennFoerste60Dager = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gjelderLoennFoerste60Dager'), 'gjelderLoennFoerste60Dager', '__urnskefastsettinginnsamlinga_meldingenv2_2_NorskKontinentalsokkel_urnskefastsettinginnsamlinga_meldingenv2_2gjelderLoennFoerste60Dager', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 270, 6), )

    
    gjelderLoennFoerste60Dager = property(__gjelderLoennFoerste60Dager.value, __gjelderLoennFoerste60Dager.set, None, None)

    _ElementMap.update({
        __tidsrom.name() : __tidsrom,
        __gjelderLoennFoerste60Dager.name() : __gjelderLoennFoerste60Dager
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NorskKontinentalsokkel = NorskKontinentalsokkel
Namespace.addCategoryObject('typeBinding', 'NorskKontinentalsokkel', NorskKontinentalsokkel)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Livrente with content type ELEMENT_ONLY
class Livrente (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Livrente with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Livrente')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 276, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}totaltUtbetaltBeloep uses Python identifier totaltUtbetaltBeloep
    __totaltUtbetaltBeloep = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'totaltUtbetaltBeloep'), 'totaltUtbetaltBeloep', '__urnskefastsettinginnsamlinga_meldingenv2_2_Livrente_urnskefastsettinginnsamlinga_meldingenv2_2totaltUtbetaltBeloep', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 278, 6), )

    
    totaltUtbetaltBeloep = property(__totaltUtbetaltBeloep.value, __totaltUtbetaltBeloep.set, None, None)

    _ElementMap.update({
        __totaltUtbetaltBeloep.name() : __totaltUtbetaltBeloep
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Livrente = Livrente
Namespace.addCategoryObject('typeBinding', 'Livrente', Livrente)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}LottOgPartInnenFiske with content type ELEMENT_ONLY
class LottOgPartInnenFiske (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}LottOgPartInnenFiske with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LottOgPartInnenFiske')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 281, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}antallDager uses Python identifier antallDager
    __antallDager = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'antallDager'), 'antallDager', '__urnskefastsettinginnsamlinga_meldingenv2_2_LottOgPartInnenFiske_urnskefastsettinginnsamlinga_meldingenv2_2antallDager', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 283, 6), )

    
    antallDager = property(__antallDager.value, __antallDager.set, None, None)

    _ElementMap.update({
        __antallDager.name() : __antallDager
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LottOgPartInnenFiske = LottOgPartInnenFiske
Namespace.addCategoryObject('typeBinding', 'LottOgPartInnenFiske', LottOgPartInnenFiske)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Nettoloennsordning with content type ELEMENT_ONLY
class Nettoloennsordning (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Nettoloennsordning with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Nettoloennsordning')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 286, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}oppgrossingstabellnummer uses Python identifier oppgrossingstabellnummer
    __oppgrossingstabellnummer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'oppgrossingstabellnummer'), 'oppgrossingstabellnummer', '__urnskefastsettinginnsamlinga_meldingenv2_2_Nettoloennsordning_urnskefastsettinginnsamlinga_meldingenv2_2oppgrossingstabellnummer', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 288, 6), )

    
    oppgrossingstabellnummer = property(__oppgrossingstabellnummer.value, __oppgrossingstabellnummer.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}bilinformasjon uses Python identifier bilinformasjon
    __bilinformasjon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bilinformasjon'), 'bilinformasjon', '__urnskefastsettinginnsamlinga_meldingenv2_2_Nettoloennsordning_urnskefastsettinginnsamlinga_meldingenv2_2bilinformasjon', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 289, 6), )

    
    bilinformasjon = property(__bilinformasjon.value, __bilinformasjon.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}betaltSkattebeloepIUtlandet uses Python identifier betaltSkattebeloepIUtlandet
    __betaltSkattebeloepIUtlandet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'betaltSkattebeloepIUtlandet'), 'betaltSkattebeloepIUtlandet', '__urnskefastsettinginnsamlinga_meldingenv2_2_Nettoloennsordning_urnskefastsettinginnsamlinga_meldingenv2_2betaltSkattebeloepIUtlandet', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 290, 6), )

    
    betaltSkattebeloepIUtlandet = property(__betaltSkattebeloepIUtlandet.value, __betaltSkattebeloepIUtlandet.set, None, None)

    _ElementMap.update({
        __oppgrossingstabellnummer.name() : __oppgrossingstabellnummer,
        __bilinformasjon.name() : __bilinformasjon,
        __betaltSkattebeloepIUtlandet.name() : __betaltSkattebeloepIUtlandet
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Nettoloennsordning = Nettoloennsordning
Namespace.addCategoryObject('typeBinding', 'Nettoloennsordning', Nettoloennsordning)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}AldersUfoereEtterlatteAvtalefestetOgKrigspensjon with content type ELEMENT_ONLY
class AldersUfoereEtterlatteAvtalefestetOgKrigspensjon (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}AldersUfoereEtterlatteAvtalefestetOgKrigspensjon with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AldersUfoereEtterlatteAvtalefestetOgKrigspensjon')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 293, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}grunnpensjonsbeloep uses Python identifier grunnpensjonsbeloep
    __grunnpensjonsbeloep = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'grunnpensjonsbeloep'), 'grunnpensjonsbeloep', '__urnskefastsettinginnsamlinga_meldingenv2_2_AldersUfoereEtterlatteAvtalefestetOgKrigspensjon_urnskefastsettinginnsamlinga_meldingenv2_2grunnpensjonsbeloep', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 295, 6), )

    
    grunnpensjonsbeloep = property(__grunnpensjonsbeloep.value, __grunnpensjonsbeloep.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}tilleggspensjonsbeloep uses Python identifier tilleggspensjonsbeloep
    __tilleggspensjonsbeloep = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tilleggspensjonsbeloep'), 'tilleggspensjonsbeloep', '__urnskefastsettinginnsamlinga_meldingenv2_2_AldersUfoereEtterlatteAvtalefestetOgKrigspensjon_urnskefastsettinginnsamlinga_meldingenv2_2tilleggspensjonsbeloep', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 296, 6), )

    
    tilleggspensjonsbeloep = property(__tilleggspensjonsbeloep.value, __tilleggspensjonsbeloep.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}ufoeregrad uses Python identifier ufoeregrad
    __ufoeregrad = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ufoeregrad'), 'ufoeregrad', '__urnskefastsettinginnsamlinga_meldingenv2_2_AldersUfoereEtterlatteAvtalefestetOgKrigspensjon_urnskefastsettinginnsamlinga_meldingenv2_2ufoeregrad', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 297, 6), )

    
    ufoeregrad = property(__ufoeregrad.value, __ufoeregrad.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}pensjonsgrad uses Python identifier pensjonsgrad
    __pensjonsgrad = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pensjonsgrad'), 'pensjonsgrad', '__urnskefastsettinginnsamlinga_meldingenv2_2_AldersUfoereEtterlatteAvtalefestetOgKrigspensjon_urnskefastsettinginnsamlinga_meldingenv2_2pensjonsgrad', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 298, 6), )

    
    pensjonsgrad = property(__pensjonsgrad.value, __pensjonsgrad.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}heravEtterlattepensjon uses Python identifier heravEtterlattepensjon
    __heravEtterlattepensjon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heravEtterlattepensjon'), 'heravEtterlattepensjon', '__urnskefastsettinginnsamlinga_meldingenv2_2_AldersUfoereEtterlatteAvtalefestetOgKrigspensjon_urnskefastsettinginnsamlinga_meldingenv2_2heravEtterlattepensjon', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 299, 6), )

    
    heravEtterlattepensjon = property(__heravEtterlattepensjon.value, __heravEtterlattepensjon.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}tidsrom uses Python identifier tidsrom
    __tidsrom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tidsrom'), 'tidsrom', '__urnskefastsettinginnsamlinga_meldingenv2_2_AldersUfoereEtterlatteAvtalefestetOgKrigspensjon_urnskefastsettinginnsamlinga_meldingenv2_2tidsrom', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 300, 6), )

    
    tidsrom = property(__tidsrom.value, __tidsrom.set, None, None)

    _ElementMap.update({
        __grunnpensjonsbeloep.name() : __grunnpensjonsbeloep,
        __tilleggspensjonsbeloep.name() : __tilleggspensjonsbeloep,
        __ufoeregrad.name() : __ufoeregrad,
        __pensjonsgrad.name() : __pensjonsgrad,
        __heravEtterlattepensjon.name() : __heravEtterlattepensjon,
        __tidsrom.name() : __tidsrom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AldersUfoereEtterlatteAvtalefestetOgKrigspensjon = AldersUfoereEtterlatteAvtalefestetOgKrigspensjon
Namespace.addCategoryObject('typeBinding', 'AldersUfoereEtterlatteAvtalefestetOgKrigspensjon', AldersUfoereEtterlatteAvtalefestetOgKrigspensjon)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}ReiseKostOgLosji with content type ELEMENT_ONLY
class ReiseKostOgLosji (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}ReiseKostOgLosji with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReiseKostOgLosji')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 303, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}persontype uses Python identifier persontype
    __persontype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'persontype'), 'persontype', '__urnskefastsettinginnsamlinga_meldingenv2_2_ReiseKostOgLosji_urnskefastsettinginnsamlinga_meldingenv2_2persontype', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 305, 6), )

    
    persontype = property(__persontype.value, __persontype.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}antallReiser uses Python identifier antallReiser
    __antallReiser = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'antallReiser'), 'antallReiser', '__urnskefastsettinginnsamlinga_meldingenv2_2_ReiseKostOgLosji_urnskefastsettinginnsamlinga_meldingenv2_2antallReiser', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 306, 6), )

    
    antallReiser = property(__antallReiser.value, __antallReiser.set, None, None)

    _ElementMap.update({
        __persontype.name() : __persontype,
        __antallReiser.name() : __antallReiser
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ReiseKostOgLosji = ReiseKostOgLosji
Namespace.addCategoryObject('typeBinding', 'ReiseKostOgLosji', ReiseKostOgLosji)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}UtenlandskArtist with content type ELEMENT_ONLY
class UtenlandskArtist (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}UtenlandskArtist with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UtenlandskArtist')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 309, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}inntektsaar uses Python identifier inntektsaar
    __inntektsaar = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inntektsaar'), 'inntektsaar', '__urnskefastsettinginnsamlinga_meldingenv2_2_UtenlandskArtist_urnskefastsettinginnsamlinga_meldingenv2_2inntektsaar', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 311, 6), )

    
    inntektsaar = property(__inntektsaar.value, __inntektsaar.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}oppgrossingsgrunnlag uses Python identifier oppgrossingsgrunnlag
    __oppgrossingsgrunnlag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'oppgrossingsgrunnlag'), 'oppgrossingsgrunnlag', '__urnskefastsettinginnsamlinga_meldingenv2_2_UtenlandskArtist_urnskefastsettinginnsamlinga_meldingenv2_2oppgrossingsgrunnlag', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 312, 6), )

    
    oppgrossingsgrunnlag = property(__oppgrossingsgrunnlag.value, __oppgrossingsgrunnlag.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}trukketArtistskatt uses Python identifier trukketArtistskatt
    __trukketArtistskatt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'trukketArtistskatt'), 'trukketArtistskatt', '__urnskefastsettinginnsamlinga_meldingenv2_2_UtenlandskArtist_urnskefastsettinginnsamlinga_meldingenv2_2trukketArtistskatt', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 313, 6), )

    
    trukketArtistskatt = property(__trukketArtistskatt.value, __trukketArtistskatt.set, None, None)

    _ElementMap.update({
        __inntektsaar.name() : __inntektsaar,
        __oppgrossingsgrunnlag.name() : __oppgrossingsgrunnlag,
        __trukketArtistskatt.name() : __trukketArtistskatt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.UtenlandskArtist = UtenlandskArtist
Namespace.addCategoryObject('typeBinding', 'UtenlandskArtist', UtenlandskArtist)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}BonusFraForsvaret with content type ELEMENT_ONLY
class BonusFraForsvaret (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}BonusFraForsvaret with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BonusFraForsvaret')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 316, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}aaretUtbetalingenGjelderFor uses Python identifier aaretUtbetalingenGjelderFor
    __aaretUtbetalingenGjelderFor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'aaretUtbetalingenGjelderFor'), 'aaretUtbetalingenGjelderFor', '__urnskefastsettinginnsamlinga_meldingenv2_2_BonusFraForsvaret_urnskefastsettinginnsamlinga_meldingenv2_2aaretUtbetalingenGjelderFor', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 318, 6), )

    
    aaretUtbetalingenGjelderFor = property(__aaretUtbetalingenGjelderFor.value, __aaretUtbetalingenGjelderFor.set, None, None)

    _ElementMap.update({
        __aaretUtbetalingenGjelderFor.name() : __aaretUtbetalingenGjelderFor
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BonusFraForsvaret = BonusFraForsvaret
Namespace.addCategoryObject('typeBinding', 'BonusFraForsvaret', BonusFraForsvaret)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Spesifikasjon with content type ELEMENT_ONLY
class Spesifikasjon (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Spesifikasjon with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Spesifikasjon')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 321, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}skattemessigBosattILand uses Python identifier skattemessigBosattILand
    __skattemessigBosattILand = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'skattemessigBosattILand'), 'skattemessigBosattILand', '__urnskefastsettinginnsamlinga_meldingenv2_2_Spesifikasjon_urnskefastsettinginnsamlinga_meldingenv2_2skattemessigBosattILand', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 323, 6), )

    
    skattemessigBosattILand = property(__skattemessigBosattILand.value, __skattemessigBosattILand.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}opptjeningsland uses Python identifier opptjeningsland
    __opptjeningsland = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'opptjeningsland'), 'opptjeningsland', '__urnskefastsettinginnsamlinga_meldingenv2_2_Spesifikasjon_urnskefastsettinginnsamlinga_meldingenv2_2opptjeningsland', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 324, 6), )

    
    opptjeningsland = property(__opptjeningsland.value, __opptjeningsland.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}erOpptjentPaaHjelpefartoey uses Python identifier erOpptjentPaaHjelpefartoey
    __erOpptjentPaaHjelpefartoey = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'erOpptjentPaaHjelpefartoey'), 'erOpptjentPaaHjelpefartoey', '__urnskefastsettinginnsamlinga_meldingenv2_2_Spesifikasjon_urnskefastsettinginnsamlinga_meldingenv2_2erOpptjentPaaHjelpefartoey', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 325, 6), )

    
    erOpptjentPaaHjelpefartoey = property(__erOpptjentPaaHjelpefartoey.value, __erOpptjentPaaHjelpefartoey.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}erOpptjentPaaKontinentalsokkel uses Python identifier erOpptjentPaaKontinentalsokkel
    __erOpptjentPaaKontinentalsokkel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'erOpptjentPaaKontinentalsokkel'), 'erOpptjentPaaKontinentalsokkel', '__urnskefastsettinginnsamlinga_meldingenv2_2_Spesifikasjon_urnskefastsettinginnsamlinga_meldingenv2_2erOpptjentPaaKontinentalsokkel', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 326, 6), )

    
    erOpptjentPaaKontinentalsokkel = property(__erOpptjentPaaKontinentalsokkel.value, __erOpptjentPaaKontinentalsokkel.set, None, None)

    _ElementMap.update({
        __skattemessigBosattILand.name() : __skattemessigBosattILand,
        __opptjeningsland.name() : __opptjeningsland,
        __erOpptjentPaaHjelpefartoey.name() : __erOpptjentPaaHjelpefartoey,
        __erOpptjentPaaKontinentalsokkel.name() : __erOpptjentPaaKontinentalsokkel
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Spesifikasjon = Spesifikasjon
Namespace.addCategoryObject('typeBinding', 'Spesifikasjon', Spesifikasjon)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}YtelseFraOffentlige with content type ELEMENT_ONLY
class YtelseFraOffentlige (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}YtelseFraOffentlige with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'YtelseFraOffentlige')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 329, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse'), 'beskrivelse', '__urnskefastsettinginnsamlinga_meldingenv2_2_YtelseFraOffentlige_urnskefastsettinginnsamlinga_meldingenv2_2beskrivelse', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 331, 6), )

    
    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}tilleggsinformasjon uses Python identifier tilleggsinformasjon
    __tilleggsinformasjon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tilleggsinformasjon'), 'tilleggsinformasjon', '__urnskefastsettinginnsamlinga_meldingenv2_2_YtelseFraOffentlige_urnskefastsettinginnsamlinga_meldingenv2_2tilleggsinformasjon', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 332, 6), )

    
    tilleggsinformasjon = property(__tilleggsinformasjon.value, __tilleggsinformasjon.set, None, None)

    _ElementMap.update({
        __beskrivelse.name() : __beskrivelse,
        __tilleggsinformasjon.name() : __tilleggsinformasjon
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.YtelseFraOffentlige = YtelseFraOffentlige
Namespace.addCategoryObject('typeBinding', 'YtelseFraOffentlige', YtelseFraOffentlige)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}PensjonEllerTrygd with content type ELEMENT_ONLY
class PensjonEllerTrygd (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}PensjonEllerTrygd with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PensjonEllerTrygd')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 338, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse'), 'beskrivelse', '__urnskefastsettinginnsamlinga_meldingenv2_2_PensjonEllerTrygd_urnskefastsettinginnsamlinga_meldingenv2_2beskrivelse', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 340, 6), )

    
    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}tilleggsinformasjon uses Python identifier tilleggsinformasjon
    __tilleggsinformasjon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tilleggsinformasjon'), 'tilleggsinformasjon', '__urnskefastsettinginnsamlinga_meldingenv2_2_PensjonEllerTrygd_urnskefastsettinginnsamlinga_meldingenv2_2tilleggsinformasjon', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 341, 6), )

    
    tilleggsinformasjon = property(__tilleggsinformasjon.value, __tilleggsinformasjon.set, None, None)

    _ElementMap.update({
        __beskrivelse.name() : __beskrivelse,
        __tilleggsinformasjon.name() : __tilleggsinformasjon
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PensjonEllerTrygd = PensjonEllerTrygd
Namespace.addCategoryObject('typeBinding', 'PensjonEllerTrygd', PensjonEllerTrygd)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Naeringsinntekt with content type ELEMENT_ONLY
class Naeringsinntekt (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Naeringsinntekt with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Naeringsinntekt')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 347, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse'), 'beskrivelse', '__urnskefastsettinginnsamlinga_meldingenv2_2_Naeringsinntekt_urnskefastsettinginnsamlinga_meldingenv2_2beskrivelse', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 349, 6), )

    
    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}tilleggsinformasjon uses Python identifier tilleggsinformasjon
    __tilleggsinformasjon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tilleggsinformasjon'), 'tilleggsinformasjon', '__urnskefastsettinginnsamlinga_meldingenv2_2_Naeringsinntekt_urnskefastsettinginnsamlinga_meldingenv2_2tilleggsinformasjon', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 350, 6), )

    
    tilleggsinformasjon = property(__tilleggsinformasjon.value, __tilleggsinformasjon.set, None, None)

    _ElementMap.update({
        __beskrivelse.name() : __beskrivelse,
        __tilleggsinformasjon.name() : __tilleggsinformasjon
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Naeringsinntekt = Naeringsinntekt
Namespace.addCategoryObject('typeBinding', 'Naeringsinntekt', Naeringsinntekt)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}SjoefolksrelatertInformasjon with content type ELEMENT_ONLY
class SjoefolksrelatertInformasjon (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}SjoefolksrelatertInformasjon with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SjoefolksrelatertInformasjon')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 359, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}antallDoegnOmbord uses Python identifier antallDoegnOmbord
    __antallDoegnOmbord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'antallDoegnOmbord'), 'antallDoegnOmbord', '__urnskefastsettinginnsamlinga_meldingenv2_2_SjoefolksrelatertInformasjon_urnskefastsettinginnsamlinga_meldingenv2_2antallDoegnOmbord', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 361, 6), )

    
    antallDoegnOmbord = property(__antallDoegnOmbord.value, __antallDoegnOmbord.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}antallDoegnOmbordUtenDekkedeSmaautgifter uses Python identifier antallDoegnOmbordUtenDekkedeSmaautgifter
    __antallDoegnOmbordUtenDekkedeSmaautgifter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'antallDoegnOmbordUtenDekkedeSmaautgifter'), 'antallDoegnOmbordUtenDekkedeSmaautgifter', '__urnskefastsettinginnsamlinga_meldingenv2_2_SjoefolksrelatertInformasjon_urnskefastsettinginnsamlinga_meldingenv2_2antallDoegnOmbordUtenDekkedeSmaautgifter', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 362, 6), )

    
    antallDoegnOmbordUtenDekkedeSmaautgifter = property(__antallDoegnOmbordUtenDekkedeSmaautgifter.value, __antallDoegnOmbordUtenDekkedeSmaautgifter.set, None, None)

    _ElementMap.update({
        __antallDoegnOmbord.name() : __antallDoegnOmbord,
        __antallDoegnOmbordUtenDekkedeSmaautgifter.name() : __antallDoegnOmbordUtenDekkedeSmaautgifter
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SjoefolksrelatertInformasjon = SjoefolksrelatertInformasjon
Namespace.addCategoryObject('typeBinding', 'SjoefolksrelatertInformasjon', SjoefolksrelatertInformasjon)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}OppholdPaaSvalbardJanMayenOgBilandene with content type ELEMENT_ONLY
class OppholdPaaSvalbardJanMayenOgBilandene (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}OppholdPaaSvalbardJanMayenOgBilandene with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OppholdPaaSvalbardJanMayenOgBilandene')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 365, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}oppholdsId uses Python identifier oppholdsId
    __oppholdsId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'oppholdsId'), 'oppholdsId', '__urnskefastsettinginnsamlinga_meldingenv2_2_OppholdPaaSvalbardJanMayenOgBilandene_urnskefastsettinginnsamlinga_meldingenv2_2oppholdsId', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 367, 6), )

    
    oppholdsId = property(__oppholdsId.value, __oppholdsId.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}startdato uses Python identifier startdato
    __startdato = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startdato'), 'startdato', '__urnskefastsettinginnsamlinga_meldingenv2_2_OppholdPaaSvalbardJanMayenOgBilandene_urnskefastsettinginnsamlinga_meldingenv2_2startdato', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 368, 6), )

    
    startdato = property(__startdato.value, __startdato.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}sluttdato uses Python identifier sluttdato
    __sluttdato = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sluttdato'), 'sluttdato', '__urnskefastsettinginnsamlinga_meldingenv2_2_OppholdPaaSvalbardJanMayenOgBilandene_urnskefastsettinginnsamlinga_meldingenv2_2sluttdato', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 369, 6), )

    
    sluttdato = property(__sluttdato.value, __sluttdato.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse'), 'beskrivelse', '__urnskefastsettinginnsamlinga_meldingenv2_2_OppholdPaaSvalbardJanMayenOgBilandene_urnskefastsettinginnsamlinga_meldingenv2_2beskrivelse', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 370, 6), )

    
    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    _ElementMap.update({
        __oppholdsId.name() : __oppholdsId,
        __startdato.name() : __startdato,
        __sluttdato.name() : __sluttdato,
        __beskrivelse.name() : __beskrivelse
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OppholdPaaSvalbardJanMayenOgBilandene = OppholdPaaSvalbardJanMayenOgBilandene
Namespace.addCategoryObject('typeBinding', 'OppholdPaaSvalbardJanMayenOgBilandene', OppholdPaaSvalbardJanMayenOgBilandene)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Utleggstrekk with content type ELEMENT_ONLY
class Utleggstrekk (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Utleggstrekk with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Utleggstrekk')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 373, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse'), 'beskrivelse', '__urnskefastsettinginnsamlinga_meldingenv2_2_Utleggstrekk_urnskefastsettinginnsamlinga_meldingenv2_2beskrivelse', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 375, 6), )

    
    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}beloep uses Python identifier beloep
    __beloep = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'beloep'), 'beloep', '__urnskefastsettinginnsamlinga_meldingenv2_2_Utleggstrekk_urnskefastsettinginnsamlinga_meldingenv2_2beloep', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 376, 6), )

    
    beloep = property(__beloep.value, __beloep.set, None, None)

    _ElementMap.update({
        __beskrivelse.name() : __beskrivelse,
        __beloep.name() : __beloep
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Utleggstrekk = Utleggstrekk
Namespace.addCategoryObject('typeBinding', 'Utleggstrekk', Utleggstrekk)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Arbeidsgiveravgift with content type ELEMENT_ONLY
class Arbeidsgiveravgift (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Arbeidsgiveravgift with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Arbeidsgiveravgift')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 382, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}loennOgGodtgjoerelse uses Python identifier loennOgGodtgjoerelse
    __loennOgGodtgjoerelse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'loennOgGodtgjoerelse'), 'loennOgGodtgjoerelse', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsgiveravgift_urnskefastsettinginnsamlinga_meldingenv2_2loennOgGodtgjoerelse', True, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 384, 6), )

    
    loennOgGodtgjoerelse = property(__loennOgGodtgjoerelse.value, __loennOgGodtgjoerelse.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}tilskuddOgPremieTilPensjon uses Python identifier tilskuddOgPremieTilPensjon
    __tilskuddOgPremieTilPensjon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tilskuddOgPremieTilPensjon'), 'tilskuddOgPremieTilPensjon', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsgiveravgift_urnskefastsettinginnsamlinga_meldingenv2_2tilskuddOgPremieTilPensjon', True, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 385, 6), )

    
    tilskuddOgPremieTilPensjon = property(__tilskuddOgPremieTilPensjon.value, __tilskuddOgPremieTilPensjon.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}utenlandskeMedSaerskiltProsentsats uses Python identifier utenlandskeMedSaerskiltProsentsats
    __utenlandskeMedSaerskiltProsentsats = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'utenlandskeMedSaerskiltProsentsats'), 'utenlandskeMedSaerskiltProsentsats', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsgiveravgift_urnskefastsettinginnsamlinga_meldingenv2_2utenlandskeMedSaerskiltProsentsats', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 386, 6), )

    
    utenlandskeMedSaerskiltProsentsats = property(__utenlandskeMedSaerskiltProsentsats.value, __utenlandskeMedSaerskiltProsentsats.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}utenlandskeMedFastAvgiftsbeloep uses Python identifier utenlandskeMedFastAvgiftsbeloep
    __utenlandskeMedFastAvgiftsbeloep = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'utenlandskeMedFastAvgiftsbeloep'), 'utenlandskeMedFastAvgiftsbeloep', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsgiveravgift_urnskefastsettinginnsamlinga_meldingenv2_2utenlandskeMedFastAvgiftsbeloep', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 387, 6), )

    
    utenlandskeMedFastAvgiftsbeloep = property(__utenlandskeMedFastAvgiftsbeloep.value, __utenlandskeMedFastAvgiftsbeloep.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}fradragIGrunnlagetForSone uses Python identifier fradragIGrunnlagetForSone
    __fradragIGrunnlagetForSone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fradragIGrunnlagetForSone'), 'fradragIGrunnlagetForSone', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsgiveravgift_urnskefastsettinginnsamlinga_meldingenv2_2fradragIGrunnlagetForSone', True, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 388, 6), )

    
    fradragIGrunnlagetForSone = property(__fradragIGrunnlagetForSone.value, __fradragIGrunnlagetForSone.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}fradragIGrunnlagetForUtenlandsk uses Python identifier fradragIGrunnlagetForUtenlandsk
    __fradragIGrunnlagetForUtenlandsk = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fradragIGrunnlagetForUtenlandsk'), 'fradragIGrunnlagetForUtenlandsk', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsgiveravgift_urnskefastsettinginnsamlinga_meldingenv2_2fradragIGrunnlagetForUtenlandsk', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 389, 6), )

    
    fradragIGrunnlagetForUtenlandsk = property(__fradragIGrunnlagetForUtenlandsk.value, __fradragIGrunnlagetForUtenlandsk.set, None, None)

    _ElementMap.update({
        __loennOgGodtgjoerelse.name() : __loennOgGodtgjoerelse,
        __tilskuddOgPremieTilPensjon.name() : __tilskuddOgPremieTilPensjon,
        __utenlandskeMedSaerskiltProsentsats.name() : __utenlandskeMedSaerskiltProsentsats,
        __utenlandskeMedFastAvgiftsbeloep.name() : __utenlandskeMedFastAvgiftsbeloep,
        __fradragIGrunnlagetForSone.name() : __fradragIGrunnlagetForSone,
        __fradragIGrunnlagetForUtenlandsk.name() : __fradragIGrunnlagetForUtenlandsk
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Arbeidsgiveravgift = Arbeidsgiveravgift
Namespace.addCategoryObject('typeBinding', 'Arbeidsgiveravgift', Arbeidsgiveravgift)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Arbeidsgiveravgiftsgrunnlag with content type ELEMENT_ONLY
class Arbeidsgiveravgiftsgrunnlag (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}Arbeidsgiveravgiftsgrunnlag with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Arbeidsgiveravgiftsgrunnlag')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 392, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}beregningskodeForArbeidsgiveravgift uses Python identifier beregningskodeForArbeidsgiveravgift
    __beregningskodeForArbeidsgiveravgift = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'beregningskodeForArbeidsgiveravgift'), 'beregningskodeForArbeidsgiveravgift', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsgiveravgiftsgrunnlag_urnskefastsettinginnsamlinga_meldingenv2_2beregningskodeForArbeidsgiveravgift', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 394, 6), )

    
    beregningskodeForArbeidsgiveravgift = property(__beregningskodeForArbeidsgiveravgift.value, __beregningskodeForArbeidsgiveravgift.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}sone uses Python identifier sone
    __sone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sone'), 'sone', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsgiveravgiftsgrunnlag_urnskefastsettinginnsamlinga_meldingenv2_2sone', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 395, 6), )

    
    sone = property(__sone.value, __sone.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}avgiftsgrunnlagBeloep uses Python identifier avgiftsgrunnlagBeloep
    __avgiftsgrunnlagBeloep = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avgiftsgrunnlagBeloep'), 'avgiftsgrunnlagBeloep', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsgiveravgiftsgrunnlag_urnskefastsettinginnsamlinga_meldingenv2_2avgiftsgrunnlagBeloep', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 396, 6), )

    
    avgiftsgrunnlagBeloep = property(__avgiftsgrunnlagBeloep.value, __avgiftsgrunnlagBeloep.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}prosentsatsForAvgiftsberegning uses Python identifier prosentsatsForAvgiftsberegning
    __prosentsatsForAvgiftsberegning = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'prosentsatsForAvgiftsberegning'), 'prosentsatsForAvgiftsberegning', '__urnskefastsettinginnsamlinga_meldingenv2_2_Arbeidsgiveravgiftsgrunnlag_urnskefastsettinginnsamlinga_meldingenv2_2prosentsatsForAvgiftsberegning', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 397, 6), )

    
    prosentsatsForAvgiftsberegning = property(__prosentsatsForAvgiftsberegning.value, __prosentsatsForAvgiftsberegning.set, None, None)

    _ElementMap.update({
        __beregningskodeForArbeidsgiveravgift.name() : __beregningskodeForArbeidsgiveravgift,
        __sone.name() : __sone,
        __avgiftsgrunnlagBeloep.name() : __avgiftsgrunnlagBeloep,
        __prosentsatsForAvgiftsberegning.name() : __prosentsatsForAvgiftsberegning
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Arbeidsgiveravgiftsgrunnlag = Arbeidsgiveravgiftsgrunnlag
Namespace.addCategoryObject('typeBinding', 'Arbeidsgiveravgiftsgrunnlag', Arbeidsgiveravgiftsgrunnlag)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}UtenlandskeMedSaerskiltProsentsats with content type ELEMENT_ONLY
class UtenlandskeMedSaerskiltProsentsats (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}UtenlandskeMedSaerskiltProsentsats with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UtenlandskeMedSaerskiltProsentsats')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 415, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}avgiftsgrunnlagBeloep uses Python identifier avgiftsgrunnlagBeloep
    __avgiftsgrunnlagBeloep = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avgiftsgrunnlagBeloep'), 'avgiftsgrunnlagBeloep', '__urnskefastsettinginnsamlinga_meldingenv2_2_UtenlandskeMedSaerskiltProsentsats_urnskefastsettinginnsamlinga_meldingenv2_2avgiftsgrunnlagBeloep', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 417, 6), )

    
    avgiftsgrunnlagBeloep = property(__avgiftsgrunnlagBeloep.value, __avgiftsgrunnlagBeloep.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}prosentsatsForAvgiftsberegning uses Python identifier prosentsatsForAvgiftsberegning
    __prosentsatsForAvgiftsberegning = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'prosentsatsForAvgiftsberegning'), 'prosentsatsForAvgiftsberegning', '__urnskefastsettinginnsamlinga_meldingenv2_2_UtenlandskeMedSaerskiltProsentsats_urnskefastsettinginnsamlinga_meldingenv2_2prosentsatsForAvgiftsberegning', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 418, 6), )

    
    prosentsatsForAvgiftsberegning = property(__prosentsatsForAvgiftsberegning.value, __prosentsatsForAvgiftsberegning.set, None, None)

    _ElementMap.update({
        __avgiftsgrunnlagBeloep.name() : __avgiftsgrunnlagBeloep,
        __prosentsatsForAvgiftsberegning.name() : __prosentsatsForAvgiftsberegning
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.UtenlandskeMedSaerskiltProsentsats = UtenlandskeMedSaerskiltProsentsats
Namespace.addCategoryObject('typeBinding', 'UtenlandskeMedSaerskiltProsentsats', UtenlandskeMedSaerskiltProsentsats)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}UtenlandskeMedFastAvgiftsbeloep with content type ELEMENT_ONLY
class UtenlandskeMedFastAvgiftsbeloep (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}UtenlandskeMedFastAvgiftsbeloep with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UtenlandskeMedFastAvgiftsbeloep')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 421, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}antallAvgiftsgrunnlagPersoner uses Python identifier antallAvgiftsgrunnlagPersoner
    __antallAvgiftsgrunnlagPersoner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'antallAvgiftsgrunnlagPersoner'), 'antallAvgiftsgrunnlagPersoner', '__urnskefastsettinginnsamlinga_meldingenv2_2_UtenlandskeMedFastAvgiftsbeloep_urnskefastsettinginnsamlinga_meldingenv2_2antallAvgiftsgrunnlagPersoner', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 423, 6), )

    
    antallAvgiftsgrunnlagPersoner = property(__antallAvgiftsgrunnlagPersoner.value, __antallAvgiftsgrunnlagPersoner.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}beloepssatsForAvgiftsberegning uses Python identifier beloepssatsForAvgiftsberegning
    __beloepssatsForAvgiftsberegning = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'beloepssatsForAvgiftsberegning'), 'beloepssatsForAvgiftsberegning', '__urnskefastsettinginnsamlinga_meldingenv2_2_UtenlandskeMedFastAvgiftsbeloep_urnskefastsettinginnsamlinga_meldingenv2_2beloepssatsForAvgiftsberegning', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 424, 6), )

    
    beloepssatsForAvgiftsberegning = property(__beloepssatsForAvgiftsberegning.value, __beloepssatsForAvgiftsberegning.set, None, None)

    _ElementMap.update({
        __antallAvgiftsgrunnlagPersoner.name() : __antallAvgiftsgrunnlagPersoner,
        __beloepssatsForAvgiftsberegning.name() : __beloepssatsForAvgiftsberegning
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.UtenlandskeMedFastAvgiftsbeloep = UtenlandskeMedFastAvgiftsbeloep
Namespace.addCategoryObject('typeBinding', 'UtenlandskeMedFastAvgiftsbeloep', UtenlandskeMedFastAvgiftsbeloep)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}FradragIGrunnlaget with content type ELEMENT_ONLY
class FradragIGrunnlaget (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}FradragIGrunnlaget with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FradragIGrunnlaget')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 427, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}beregningskodeForArbeidsgiveravgift uses Python identifier beregningskodeForArbeidsgiveravgift
    __beregningskodeForArbeidsgiveravgift = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'beregningskodeForArbeidsgiveravgift'), 'beregningskodeForArbeidsgiveravgift', '__urnskefastsettinginnsamlinga_meldingenv2_2_FradragIGrunnlaget_urnskefastsettinginnsamlinga_meldingenv2_2beregningskodeForArbeidsgiveravgift', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 429, 6), )

    
    beregningskodeForArbeidsgiveravgift = property(__beregningskodeForArbeidsgiveravgift.value, __beregningskodeForArbeidsgiveravgift.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}sone uses Python identifier sone
    __sone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sone'), 'sone', '__urnskefastsettinginnsamlinga_meldingenv2_2_FradragIGrunnlaget_urnskefastsettinginnsamlinga_meldingenv2_2sone', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 430, 6), )

    
    sone = property(__sone.value, __sone.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}avgiftsfradragBeloep uses Python identifier avgiftsfradragBeloep
    __avgiftsfradragBeloep = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avgiftsfradragBeloep'), 'avgiftsfradragBeloep', '__urnskefastsettinginnsamlinga_meldingenv2_2_FradragIGrunnlaget_urnskefastsettinginnsamlinga_meldingenv2_2avgiftsfradragBeloep', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 431, 6), )

    
    avgiftsfradragBeloep = property(__avgiftsfradragBeloep.value, __avgiftsfradragBeloep.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}prosentsatsForAvgiftsberegning uses Python identifier prosentsatsForAvgiftsberegning
    __prosentsatsForAvgiftsberegning = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'prosentsatsForAvgiftsberegning'), 'prosentsatsForAvgiftsberegning', '__urnskefastsettinginnsamlinga_meldingenv2_2_FradragIGrunnlaget_urnskefastsettinginnsamlinga_meldingenv2_2prosentsatsForAvgiftsberegning', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 432, 6), )

    
    prosentsatsForAvgiftsberegning = property(__prosentsatsForAvgiftsberegning.value, __prosentsatsForAvgiftsberegning.set, None, None)

    _ElementMap.update({
        __beregningskodeForArbeidsgiveravgift.name() : __beregningskodeForArbeidsgiveravgift,
        __sone.name() : __sone,
        __avgiftsfradragBeloep.name() : __avgiftsfradragBeloep,
        __prosentsatsForAvgiftsberegning.name() : __prosentsatsForAvgiftsberegning
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FradragIGrunnlaget = FradragIGrunnlaget
Namespace.addCategoryObject('typeBinding', 'FradragIGrunnlaget', FradragIGrunnlaget)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}FradragIGrunnlagetForUtenlandsk with content type ELEMENT_ONLY
class FradragIGrunnlagetForUtenlandsk (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}FradragIGrunnlagetForUtenlandsk with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FradragIGrunnlagetForUtenlandsk')
    _XSDLocation = pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 435, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}avgiftsfradragBeloep uses Python identifier avgiftsfradragBeloep
    __avgiftsfradragBeloep = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avgiftsfradragBeloep'), 'avgiftsfradragBeloep', '__urnskefastsettinginnsamlinga_meldingenv2_2_FradragIGrunnlagetForUtenlandsk_urnskefastsettinginnsamlinga_meldingenv2_2avgiftsfradragBeloep', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 437, 6), )

    
    avgiftsfradragBeloep = property(__avgiftsfradragBeloep.value, __avgiftsfradragBeloep.set, None, None)

    
    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_2}prosentsatsForAvgiftsberegning uses Python identifier prosentsatsForAvgiftsberegning
    __prosentsatsForAvgiftsberegning = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'prosentsatsForAvgiftsberegning'), 'prosentsatsForAvgiftsberegning', '__urnskefastsettinginnsamlinga_meldingenv2_2_FradragIGrunnlagetForUtenlandsk_urnskefastsettinginnsamlinga_meldingenv2_2prosentsatsForAvgiftsberegning', False, pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 438, 6), )

    
    prosentsatsForAvgiftsberegning = property(__prosentsatsForAvgiftsberegning.value, __prosentsatsForAvgiftsberegning.set, None, None)

    _ElementMap.update({
        __avgiftsfradragBeloep.name() : __avgiftsfradragBeloep,
        __prosentsatsForAvgiftsberegning.name() : __prosentsatsForAvgiftsberegning
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FradragIGrunnlagetForUtenlandsk = FradragIGrunnlagetForUtenlandsk
Namespace.addCategoryObject('typeBinding', 'FradragIGrunnlagetForUtenlandsk', FradragIGrunnlagetForUtenlandsk)


melding = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'melding'), EDAG_M, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', melding.name().localName(), melding)



EDAG_M._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Leveranse'), Leveranse, scope=EDAG_M, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 6, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EDAG_M._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Leveranse')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 6, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
EDAG_M._Automaton = _BuildAutomaton()




Leveranse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'leveringstidspunkt'), DatoTid, scope=Leveranse, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 11, 6)))

Leveranse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'kalendermaaned'), STD_ANON, scope=Leveranse, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 12, 6)))

Leveranse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'kildesystem'), TekstMedRestriksjon, scope=Leveranse, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 20, 6)))

Leveranse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'erstatterMeldingsId'), Identifikator, scope=Leveranse, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 21, 6)))

Leveranse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'meldingsId'), Identifikator, scope=Leveranse, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 22, 6)))

Leveranse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'opplysningspliktig'), Opplysningspliktig, scope=Leveranse, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 23, 6)))

Leveranse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'oppgave'), JuridiskEntitet, scope=Leveranse, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 24, 6)))

Leveranse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'spraakForTilbakemelding'), Spraak, scope=Leveranse, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 25, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 21, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 25, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Leveranse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'leveringstidspunkt')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 11, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Leveranse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'kalendermaaned')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 12, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Leveranse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'kildesystem')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 20, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Leveranse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'erstatterMeldingsId')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 21, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Leveranse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'meldingsId')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 22, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Leveranse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'opplysningspliktig')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 23, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Leveranse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'oppgave')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 24, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Leveranse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'spraakForTilbakemelding')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 25, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Leveranse._Automaton = _BuildAutomaton_()




Opplysningspliktig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'norskIdentifikator'), NorskIdentifikator, scope=Opplysningspliktig, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 30, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Opplysningspliktig._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'norskIdentifikator')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 30, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Opplysningspliktig._Automaton = _BuildAutomaton_2()




JuridiskEntitet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'betalingsinformasjon'), Betalingsinformasjon, scope=JuridiskEntitet, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 35, 6)))

JuridiskEntitet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'betalingsinformasjonForForenkletOrdning'), BetalingsinformasjonForForenkletOrdning, scope=JuridiskEntitet, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 36, 6)))

JuridiskEntitet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annenBagatellmessigStoette'), Beloep, scope=JuridiskEntitet, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 37, 6)))

JuridiskEntitet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'virksomhet'), Virksomhet, scope=JuridiskEntitet, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 38, 6)))

JuridiskEntitet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pensjonsinnretning'), Pensjonsinnretning, scope=JuridiskEntitet, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 39, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 35, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 36, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 37, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 38, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 39, 6))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(JuridiskEntitet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'betalingsinformasjon')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 35, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(JuridiskEntitet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'betalingsinformasjonForForenkletOrdning')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 36, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(JuridiskEntitet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annenBagatellmessigStoette')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 37, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(JuridiskEntitet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'virksomhet')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 38, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(JuridiskEntitet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pensjonsinnretning')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 39, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
JuridiskEntitet._Automaton = _BuildAutomaton_3()




Betalingsinformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sumForskuddstrekk'), BeloepSomHeltall, scope=Betalingsinformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 44, 6)))

Betalingsinformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sumArbeidsgiveravgift'), BeloepSomHeltall, scope=Betalingsinformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 45, 6)))

Betalingsinformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sumFinansskattLoenn'), BeloepSomHeltall, scope=Betalingsinformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 46, 6)))

Betalingsinformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sumUtleggstrekk'), BeloepSomHeltall, scope=Betalingsinformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 47, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 44, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 45, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 46, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 47, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Betalingsinformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sumForskuddstrekk')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 44, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Betalingsinformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sumArbeidsgiveravgift')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 45, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Betalingsinformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sumFinansskattLoenn')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 46, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Betalingsinformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sumUtleggstrekk')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 47, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Betalingsinformasjon._Automaton = _BuildAutomaton_4()




BetalingsinformasjonForForenkletOrdning._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sumForskuddstrekk'), BeloepSomHeltall, scope=BetalingsinformasjonForForenkletOrdning, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 52, 6)))

BetalingsinformasjonForForenkletOrdning._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sumArbeidsgiveravgift'), BeloepSomHeltall, scope=BetalingsinformasjonForForenkletOrdning, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 53, 6)))

BetalingsinformasjonForForenkletOrdning._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'loennsutbetalingsdato'), Dato, scope=BetalingsinformasjonForForenkletOrdning, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 54, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 52, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 53, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BetalingsinformasjonForForenkletOrdning._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sumForskuddstrekk')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 52, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BetalingsinformasjonForForenkletOrdning._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sumArbeidsgiveravgift')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 53, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BetalingsinformasjonForForenkletOrdning._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'loennsutbetalingsdato')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 54, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BetalingsinformasjonForForenkletOrdning._Automaton = _BuildAutomaton_5()




Virksomhet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'norskIdentifikator'), NorskIdentifikator, scope=Virksomhet, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 59, 6)))

Virksomhet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inntektsmottaker'), Inntektsmottaker, scope=Virksomhet, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 60, 6)))

Virksomhet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'arbeidsgiveravgift'), Arbeidsgiveravgift, scope=Virksomhet, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 61, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 60, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 61, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Virksomhet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'norskIdentifikator')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 59, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Virksomhet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inntektsmottaker')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 60, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Virksomhet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'arbeidsgiveravgift')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 61, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Virksomhet._Automaton = _BuildAutomaton_6()




Pensjonsinnretning._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'identifikator'), TekstMedRestriksjon, scope=Pensjonsinnretning, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 66, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Pensjonsinnretning._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'identifikator')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 66, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Pensjonsinnretning._Automaton = _BuildAutomaton_7()




Inntektsmottaker._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'norskIdentifikator'), NorskIdentifikator, scope=Inntektsmottaker, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 71, 6)))

Inntektsmottaker._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'internasjonalIdentifikator'), InternasjonalIdentifikator, scope=Inntektsmottaker, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 72, 6)))

Inntektsmottaker._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'identifiserendeInformasjon'), IdentifiserendeInformasjon, scope=Inntektsmottaker, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 73, 6)))

Inntektsmottaker._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'arbeidsforhold'), Arbeidsforhold, scope=Inntektsmottaker, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 74, 6)))

Inntektsmottaker._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fradrag'), Fradrag, scope=Inntektsmottaker, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 75, 6)))

Inntektsmottaker._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'forskuddstrekk'), Forskuddstrekk, scope=Inntektsmottaker, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 76, 6)))

Inntektsmottaker._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inntekt'), Inntekt, scope=Inntektsmottaker, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 77, 6)))

Inntektsmottaker._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sjoefolksrelatertInformasjon'), SjoefolksrelatertInformasjon, scope=Inntektsmottaker, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 78, 6)))

Inntektsmottaker._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'oppholdPaaSvalbardJanMayenOgBilandene'), OppholdPaaSvalbardJanMayenOgBilandene, scope=Inntektsmottaker, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 79, 6)))

Inntektsmottaker._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'utleggstrekk'), Utleggstrekk, scope=Inntektsmottaker, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 80, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 71, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 72, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 73, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 74, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 75, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 76, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 77, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 78, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 79, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 80, 6))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Inntektsmottaker._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'norskIdentifikator')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 71, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Inntektsmottaker._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'internasjonalIdentifikator')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 72, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Inntektsmottaker._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'identifiserendeInformasjon')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 73, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Inntektsmottaker._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'arbeidsforhold')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 74, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Inntektsmottaker._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fradrag')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 75, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Inntektsmottaker._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'forskuddstrekk')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 76, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Inntektsmottaker._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inntekt')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 77, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Inntektsmottaker._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sjoefolksrelatertInformasjon')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 78, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Inntektsmottaker._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'oppholdPaaSvalbardJanMayenOgBilandene')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 79, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Inntektsmottaker._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'utleggstrekk')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 80, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Inntektsmottaker._Automaton = _BuildAutomaton_8()




InternasjonalIdentifikator._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'identifikator'), TekstMedRestriksjon, scope=InternasjonalIdentifikator, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 85, 6)))

InternasjonalIdentifikator._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'identifikatortype'), InternasjonalIdentifikatortype, scope=InternasjonalIdentifikator, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 86, 6)))

InternasjonalIdentifikator._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'land'), Landkode, scope=InternasjonalIdentifikator, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 87, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InternasjonalIdentifikator._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'identifikator')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 85, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InternasjonalIdentifikator._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'identifikatortype')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 86, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InternasjonalIdentifikator._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'land')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 87, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InternasjonalIdentifikator._Automaton = _BuildAutomaton_9()




IdentifiserendeInformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'navn'), TekstMedRestriksjon, scope=IdentifiserendeInformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 98, 6)))

IdentifiserendeInformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'foedselsdato'), Dato, scope=IdentifiserendeInformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 99, 6)))

IdentifiserendeInformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ansattnummer'), TekstMedRestriksjon, scope=IdentifiserendeInformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 100, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 100, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(IdentifiserendeInformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'navn')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 98, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(IdentifiserendeInformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'foedselsdato')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 99, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IdentifiserendeInformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ansattnummer')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 100, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
IdentifiserendeInformasjon._Automaton = _BuildAutomaton_10()




Arbeidsforhold._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'arbeidsforholdId'), Identifikator, scope=Arbeidsforhold, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 105, 6)))

Arbeidsforhold._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'typeArbeidsforhold'), Arbeidsforholdstype, scope=Arbeidsforhold, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 106, 6)))

Arbeidsforhold._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startdato'), Dato, scope=Arbeidsforhold, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 107, 6)))

Arbeidsforhold._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sluttdato'), Dato, scope=Arbeidsforhold, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 108, 6)))

Arbeidsforhold._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'antallTimerPerUkeSomEnFullStillingTilsvarer'), Desimaltall, scope=Arbeidsforhold, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 109, 6)))

Arbeidsforhold._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avloenningstype'), Avloenningstype, scope=Arbeidsforhold, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 110, 6)))

Arbeidsforhold._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'yrke'), Yrke, scope=Arbeidsforhold, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 111, 6)))

Arbeidsforhold._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'arbeidstidsordning'), Arbeidstidsordning, scope=Arbeidsforhold, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 112, 6)))

Arbeidsforhold._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stillingsprosent'), Desimaltall, scope=Arbeidsforhold, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 113, 6)))

Arbeidsforhold._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sisteLoennsendringsdato'), Dato, scope=Arbeidsforhold, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 114, 6)))

Arbeidsforhold._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'loennsansiennitet'), Dato, scope=Arbeidsforhold, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 115, 6)))

Arbeidsforhold._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'loennstrinn'), TekstMedRestriksjon, scope=Arbeidsforhold, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 116, 6)))

Arbeidsforhold._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fartoey'), Fartoey, scope=Arbeidsforhold, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 117, 6)))

Arbeidsforhold._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'permisjon'), Permisjon, scope=Arbeidsforhold, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 118, 6)))

Arbeidsforhold._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sisteDatoForStillingsprosentendring'), Dato, scope=Arbeidsforhold, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 119, 6)))

Arbeidsforhold._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aarsakTilSluttdato'), AarsakSluttdato, scope=Arbeidsforhold, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 120, 6)))

Arbeidsforhold._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'formForAnsettelse'), Ansettelsesform, scope=Arbeidsforhold, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 121, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 105, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 107, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 108, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 109, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 110, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 111, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 112, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 113, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 114, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 115, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 116, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 117, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 118, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 119, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 120, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 121, 6))
    counters.add(cc_15)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'arbeidsforholdId')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 105, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'typeArbeidsforhold')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 106, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startdato')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 107, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sluttdato')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 108, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'antallTimerPerUkeSomEnFullStillingTilsvarer')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 109, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avloenningstype')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 110, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'yrke')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 111, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'arbeidstidsordning')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 112, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stillingsprosent')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 113, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sisteLoennsendringsdato')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 114, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'loennsansiennitet')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 115, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'loennstrinn')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 116, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fartoey')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 117, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'permisjon')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 118, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sisteDatoForStillingsprosentendring')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 119, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'aarsakTilSluttdato')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 120, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'formForAnsettelse')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 121, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Arbeidsforhold._Automaton = _BuildAutomaton_11()




Fartoey._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'skipsregister'), Skipsregister, scope=Fartoey, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 144, 6)))

Fartoey._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'skipstype'), Skipstype, scope=Fartoey, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 145, 6)))

Fartoey._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fartsomraade'), Fartsomraade, scope=Fartoey, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 146, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Fartoey._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'skipsregister')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 144, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Fartoey._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'skipstype')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 145, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Fartoey._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fartsomraade')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 146, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Fartoey._Automaton = _BuildAutomaton_12()




Permisjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startdato'), Dato, scope=Permisjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 163, 6)))

Permisjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sluttdato'), Dato, scope=Permisjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 164, 6)))

Permisjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'permisjonsprosent'), Desimaltall, scope=Permisjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 165, 6)))

Permisjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'permisjonId'), Identifikator, scope=Permisjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 166, 6)))

Permisjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse'), PermisjonsOgPermitteringsBeskrivelse, scope=Permisjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 167, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 164, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Permisjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startdato')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 163, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Permisjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sluttdato')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 164, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Permisjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'permisjonsprosent')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 165, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Permisjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'permisjonId')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 166, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Permisjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 167, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Permisjon._Automaton = _BuildAutomaton_13()




Fradrag._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse'), Fradragsbeskrivelse, scope=Fradrag, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 172, 6)))

Fradrag._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'beloep'), Beloep, scope=Fradrag, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 173, 6)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Fradrag._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 172, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Fradrag._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'beloep')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 173, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Fradrag._Automaton = _BuildAutomaton_14()




Forskuddstrekk._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse'), Forskuddstrekksbeskrivelse, scope=Forskuddstrekk, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 181, 6)))

Forskuddstrekk._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'beloep'), BeloepSomHeltall, scope=Forskuddstrekk, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 182, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 181, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Forskuddstrekk._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 181, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Forskuddstrekk._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'beloep')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 182, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Forskuddstrekk._Automaton = _BuildAutomaton_15()




Inntekt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'skatteOgAvgiftsregel'), SkatteOgAvgiftsregel, scope=Inntekt, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 190, 6)))

Inntekt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startdatoOpptjeningsperiode'), Dato, scope=Inntekt, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 191, 6)))

Inntekt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sluttdatoOpptjeningsperiode'), Dato, scope=Inntekt, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 192, 6)))

Inntekt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fordel'), Fordel, scope=Inntekt, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 193, 6)))

Inntekt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'utloeserArbeidsgiveravgift'), Boolsk, scope=Inntekt, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 194, 6)))

Inntekt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inngaarIGrunnlagForTrekk'), Boolsk, scope=Inntekt, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 195, 6)))

Inntekt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'beloep'), Beloep, scope=Inntekt, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 196, 6)))

Inntekt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'arbeidsforholdId'), Identifikator, scope=Inntekt, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 197, 6)))

Inntekt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'loennsinntekt'), Loennsinntekt, scope=Inntekt, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 199, 8)))

Inntekt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ytelseFraOffentlige'), YtelseFraOffentlige, scope=Inntekt, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 200, 8)))

Inntekt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pensjonEllerTrygd'), PensjonEllerTrygd, scope=Inntekt, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 201, 8)))

Inntekt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'naeringsinntekt'), Naeringsinntekt, scope=Inntekt, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 202, 8)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 190, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 191, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 192, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 197, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Inntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'skatteOgAvgiftsregel')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 190, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Inntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startdatoOpptjeningsperiode')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 191, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Inntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sluttdatoOpptjeningsperiode')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 192, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Inntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fordel')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 193, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Inntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'utloeserArbeidsgiveravgift')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 194, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Inntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inngaarIGrunnlagForTrekk')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 195, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Inntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'beloep')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 196, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Inntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'arbeidsforholdId')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 197, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Inntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'loennsinntekt')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 199, 8))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Inntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ytelseFraOffentlige')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 200, 8))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Inntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pensjonEllerTrygd')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 201, 8))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Inntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'naeringsinntekt')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 202, 8))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    transitions = []
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Inntekt._Automaton = _BuildAutomaton_16()




Loennsinntekt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse'), Loennsbeskrivelse, scope=Loennsinntekt, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 214, 6)))

Loennsinntekt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tilleggsinformasjon'), Tilleggsinformasjon, scope=Loennsinntekt, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 215, 6)))

Loennsinntekt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'spesifikasjon'), Spesifikasjon, scope=Loennsinntekt, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 216, 6)))

Loennsinntekt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'antall'), Desimaltall, scope=Loennsinntekt, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 217, 6)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 215, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 216, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 217, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Loennsinntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 214, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Loennsinntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tilleggsinformasjon')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 215, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Loennsinntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'spesifikasjon')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 216, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Loennsinntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'antall')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 217, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Loennsinntekt._Automaton = _BuildAutomaton_17()




Tilleggsinformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bilOgBaat'), BilOgBaat, scope=Tilleggsinformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 225, 6)))

Tilleggsinformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dagmammaIEgenBolig'), DagmammaIEgenBolig, scope=Tilleggsinformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 226, 6)))

Tilleggsinformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'etterbetalingsperiode'), Periode, scope=Tilleggsinformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 227, 6)))

Tilleggsinformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inntektPaaNorskKontinentalsokkel'), NorskKontinentalsokkel, scope=Tilleggsinformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 228, 6)))

Tilleggsinformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inntjeningsforhold'), SpesielleInntjeningsforhold, scope=Tilleggsinformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 229, 6)))

Tilleggsinformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'livrente'), Livrente, scope=Tilleggsinformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 230, 6)))

Tilleggsinformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lottOgPart'), LottOgPartInnenFiske, scope=Tilleggsinformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 231, 6)))

Tilleggsinformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nettoloenn'), Nettoloennsordning, scope=Tilleggsinformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 232, 6)))

Tilleggsinformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pensjon'), AldersUfoereEtterlatteAvtalefestetOgKrigspensjon, scope=Tilleggsinformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 233, 6)))

Tilleggsinformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reiseKostOgLosji'), ReiseKostOgLosji, scope=Tilleggsinformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 234, 6)))

Tilleggsinformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'utenlandskArtist'), UtenlandskArtist, scope=Tilleggsinformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 235, 6)))

Tilleggsinformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bonusFraForsvaret'), BonusFraForsvaret, scope=Tilleggsinformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 236, 6)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Tilleggsinformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bilOgBaat')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 225, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Tilleggsinformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dagmammaIEgenBolig')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 226, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Tilleggsinformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'etterbetalingsperiode')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 227, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Tilleggsinformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inntektPaaNorskKontinentalsokkel')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 228, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Tilleggsinformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inntjeningsforhold')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 229, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Tilleggsinformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'livrente')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 230, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Tilleggsinformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lottOgPart')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 231, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Tilleggsinformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nettoloenn')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 232, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Tilleggsinformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pensjon')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 233, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Tilleggsinformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'reiseKostOgLosji')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 234, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Tilleggsinformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'utenlandskArtist')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 235, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Tilleggsinformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bonusFraForsvaret')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 236, 6))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    transitions = []
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Tilleggsinformasjon._Automaton = _BuildAutomaton_18()




Periode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startdato'), Dato, scope=Periode, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 241, 6)))

Periode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sluttdato'), Dato, scope=Periode, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 242, 6)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Periode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startdato')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 241, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Periode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sluttdato')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 242, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Periode._Automaton = _BuildAutomaton_19()




BilOgBaat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'antallKilometer'), Desimaltall, scope=BilOgBaat, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 247, 6)))

BilOgBaat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'antallReiser'), Heltall, scope=BilOgBaat, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 248, 6)))

BilOgBaat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heravAntallKilometerMellomHjemOgArbeid'), Desimaltall, scope=BilOgBaat, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 249, 6)))

BilOgBaat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'listeprisForBil'), Beloep, scope=BilOgBaat, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 250, 6)))

BilOgBaat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bilregistreringsnummer'), TekstMedRestriksjon, scope=BilOgBaat, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 251, 6)))

BilOgBaat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'erBilpool'), Boolsk, scope=BilOgBaat, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 252, 6)))

BilOgBaat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'erAnnenBil'), Boolsk, scope=BilOgBaat, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 253, 6)))

BilOgBaat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'erBilUtenforStandardregelen'), Boolsk, scope=BilOgBaat, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 254, 6)))

BilOgBaat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'personklassifiseringAvBilbruker'), PersontypeForReiseKostLosji, scope=BilOgBaat, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 255, 6)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 247, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 248, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 249, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 250, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 251, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 252, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 253, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 254, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 255, 6))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BilOgBaat._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'antallKilometer')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 247, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BilOgBaat._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'antallReiser')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 248, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BilOgBaat._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heravAntallKilometerMellomHjemOgArbeid')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 249, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(BilOgBaat._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'listeprisForBil')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 250, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(BilOgBaat._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bilregistreringsnummer')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 251, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(BilOgBaat._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'erBilpool')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 252, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(BilOgBaat._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'erAnnenBil')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 253, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(BilOgBaat._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'erBilUtenforStandardregelen')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 254, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(BilOgBaat._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'personklassifiseringAvBilbruker')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 255, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BilOgBaat._Automaton = _BuildAutomaton_20()




DagmammaIEgenBolig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'antallBarn'), Heltall, scope=DagmammaIEgenBolig, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 263, 6)))

DagmammaIEgenBolig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'antallMaaneder'), Heltall, scope=DagmammaIEgenBolig, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 264, 6)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DagmammaIEgenBolig._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'antallBarn')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 263, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DagmammaIEgenBolig._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'antallMaaneder')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 264, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DagmammaIEgenBolig._Automaton = _BuildAutomaton_21()




NorskKontinentalsokkel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tidsrom'), Periode, scope=NorskKontinentalsokkel, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 269, 6)))

NorskKontinentalsokkel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gjelderLoennFoerste60Dager'), Boolsk, scope=NorskKontinentalsokkel, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 270, 6)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 269, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 270, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NorskKontinentalsokkel._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tidsrom')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 269, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NorskKontinentalsokkel._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gjelderLoennFoerste60Dager')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 270, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NorskKontinentalsokkel._Automaton = _BuildAutomaton_22()




Livrente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'totaltUtbetaltBeloep'), Beloep, scope=Livrente, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 278, 6)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Livrente._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'totaltUtbetaltBeloep')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 278, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Livrente._Automaton = _BuildAutomaton_23()




LottOgPartInnenFiske._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'antallDager'), Heltall, scope=LottOgPartInnenFiske, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 283, 6)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 283, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LottOgPartInnenFiske._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'antallDager')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 283, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LottOgPartInnenFiske._Automaton = _BuildAutomaton_24()




Nettoloennsordning._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'oppgrossingstabellnummer'), Heltall, scope=Nettoloennsordning, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 288, 6)))

Nettoloennsordning._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bilinformasjon'), BilOgBaat, scope=Nettoloennsordning, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 289, 6)))

Nettoloennsordning._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'betaltSkattebeloepIUtlandet'), Beloep, scope=Nettoloennsordning, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 290, 6)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 288, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 289, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 290, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Nettoloennsordning._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'oppgrossingstabellnummer')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 288, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Nettoloennsordning._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bilinformasjon')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 289, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Nettoloennsordning._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'betaltSkattebeloepIUtlandet')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 290, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Nettoloennsordning._Automaton = _BuildAutomaton_25()




AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'grunnpensjonsbeloep'), Beloep, scope=AldersUfoereEtterlatteAvtalefestetOgKrigspensjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 295, 6)))

AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tilleggspensjonsbeloep'), Beloep, scope=AldersUfoereEtterlatteAvtalefestetOgKrigspensjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 296, 6)))

AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ufoeregrad'), Heltall, scope=AldersUfoereEtterlatteAvtalefestetOgKrigspensjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 297, 6)))

AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pensjonsgrad'), Heltall, scope=AldersUfoereEtterlatteAvtalefestetOgKrigspensjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 298, 6)))

AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heravEtterlattepensjon'), Beloep, scope=AldersUfoereEtterlatteAvtalefestetOgKrigspensjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 299, 6)))

AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tidsrom'), Periode, scope=AldersUfoereEtterlatteAvtalefestetOgKrigspensjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 300, 6)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 295, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 296, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 297, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 298, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 299, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 300, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'grunnpensjonsbeloep')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 295, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tilleggspensjonsbeloep')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 296, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ufoeregrad')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 297, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pensjonsgrad')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 298, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heravEtterlattepensjon')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 299, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tidsrom')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 300, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._Automaton = _BuildAutomaton_26()




ReiseKostOgLosji._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'persontype'), PersontypeForReiseKostLosji, scope=ReiseKostOgLosji, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 305, 6)))

ReiseKostOgLosji._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'antallReiser'), Heltall, scope=ReiseKostOgLosji, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 306, 6)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 305, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 306, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReiseKostOgLosji._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'persontype')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 305, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ReiseKostOgLosji._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'antallReiser')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 306, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ReiseKostOgLosji._Automaton = _BuildAutomaton_27()




UtenlandskArtist._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inntektsaar'), AArstall, scope=UtenlandskArtist, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 311, 6)))

UtenlandskArtist._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'oppgrossingsgrunnlag'), Beloep, scope=UtenlandskArtist, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 312, 6)))

UtenlandskArtist._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'trukketArtistskatt'), BeloepSomHeltall, scope=UtenlandskArtist, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 313, 6)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UtenlandskArtist._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inntektsaar')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 311, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UtenlandskArtist._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'oppgrossingsgrunnlag')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 312, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UtenlandskArtist._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'trukketArtistskatt')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 313, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UtenlandskArtist._Automaton = _BuildAutomaton_28()




BonusFraForsvaret._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aaretUtbetalingenGjelderFor'), AArstall, scope=BonusFraForsvaret, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 318, 6)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 318, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BonusFraForsvaret._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'aaretUtbetalingenGjelderFor')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 318, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BonusFraForsvaret._Automaton = _BuildAutomaton_29()




Spesifikasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'skattemessigBosattILand'), Landkode, scope=Spesifikasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 323, 6)))

Spesifikasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'opptjeningsland'), Landkode, scope=Spesifikasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 324, 6)))

Spesifikasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'erOpptjentPaaHjelpefartoey'), Boolsk, scope=Spesifikasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 325, 6)))

Spesifikasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'erOpptjentPaaKontinentalsokkel'), Boolsk, scope=Spesifikasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 326, 6)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 323, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 324, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 325, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 326, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Spesifikasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'skattemessigBosattILand')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 323, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Spesifikasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'opptjeningsland')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 324, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Spesifikasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'erOpptjentPaaHjelpefartoey')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 325, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Spesifikasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'erOpptjentPaaKontinentalsokkel')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 326, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Spesifikasjon._Automaton = _BuildAutomaton_30()




YtelseFraOffentlige._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse'), YtelseFraOffentligeBeskrivelse, scope=YtelseFraOffentlige, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 331, 6)))

YtelseFraOffentlige._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tilleggsinformasjon'), Tilleggsinformasjon, scope=YtelseFraOffentlige, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 332, 6)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 332, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(YtelseFraOffentlige._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 331, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(YtelseFraOffentlige._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tilleggsinformasjon')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 332, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
YtelseFraOffentlige._Automaton = _BuildAutomaton_31()




PensjonEllerTrygd._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse'), PensjonEllerTrygdebeskrivelse, scope=PensjonEllerTrygd, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 340, 6)))

PensjonEllerTrygd._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tilleggsinformasjon'), Tilleggsinformasjon, scope=PensjonEllerTrygd, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 341, 6)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 341, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PensjonEllerTrygd._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 340, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PensjonEllerTrygd._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tilleggsinformasjon')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 341, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PensjonEllerTrygd._Automaton = _BuildAutomaton_32()




Naeringsinntekt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse'), Naeringsinntektsbeskrivelse, scope=Naeringsinntekt, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 349, 6)))

Naeringsinntekt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tilleggsinformasjon'), Tilleggsinformasjon, scope=Naeringsinntekt, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 350, 6)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 350, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Naeringsinntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 349, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Naeringsinntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tilleggsinformasjon')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 350, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Naeringsinntekt._Automaton = _BuildAutomaton_33()




SjoefolksrelatertInformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'antallDoegnOmbord'), Heltall, scope=SjoefolksrelatertInformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 361, 6)))

SjoefolksrelatertInformasjon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'antallDoegnOmbordUtenDekkedeSmaautgifter'), Heltall, scope=SjoefolksrelatertInformasjon, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 362, 6)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 361, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 362, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SjoefolksrelatertInformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'antallDoegnOmbord')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 361, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SjoefolksrelatertInformasjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'antallDoegnOmbordUtenDekkedeSmaautgifter')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 362, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SjoefolksrelatertInformasjon._Automaton = _BuildAutomaton_34()




OppholdPaaSvalbardJanMayenOgBilandene._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'oppholdsId'), Identifikator, scope=OppholdPaaSvalbardJanMayenOgBilandene, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 367, 6)))

OppholdPaaSvalbardJanMayenOgBilandene._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startdato'), Dato, scope=OppholdPaaSvalbardJanMayenOgBilandene, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 368, 6)))

OppholdPaaSvalbardJanMayenOgBilandene._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sluttdato'), Dato, scope=OppholdPaaSvalbardJanMayenOgBilandene, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 369, 6)))

OppholdPaaSvalbardJanMayenOgBilandene._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse'), OppholdsbeskrivelseForSvalbardJanMayenOgBilandene, scope=OppholdPaaSvalbardJanMayenOgBilandene, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 370, 6)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 369, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OppholdPaaSvalbardJanMayenOgBilandene._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'oppholdsId')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 367, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OppholdPaaSvalbardJanMayenOgBilandene._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startdato')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 368, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OppholdPaaSvalbardJanMayenOgBilandene._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sluttdato')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 369, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OppholdPaaSvalbardJanMayenOgBilandene._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 370, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OppholdPaaSvalbardJanMayenOgBilandene._Automaton = _BuildAutomaton_35()




Utleggstrekk._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse'), Utleggstrekkbeskrivelse, scope=Utleggstrekk, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 375, 6)))

Utleggstrekk._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'beloep'), BeloepSomHeltall, scope=Utleggstrekk, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 376, 6)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Utleggstrekk._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'beskrivelse')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 375, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Utleggstrekk._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'beloep')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 376, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Utleggstrekk._Automaton = _BuildAutomaton_36()




Arbeidsgiveravgift._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'loennOgGodtgjoerelse'), Arbeidsgiveravgiftsgrunnlag, scope=Arbeidsgiveravgift, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 384, 6)))

Arbeidsgiveravgift._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tilskuddOgPremieTilPensjon'), Arbeidsgiveravgiftsgrunnlag, scope=Arbeidsgiveravgift, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 385, 6)))

Arbeidsgiveravgift._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'utenlandskeMedSaerskiltProsentsats'), UtenlandskeMedSaerskiltProsentsats, scope=Arbeidsgiveravgift, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 386, 6)))

Arbeidsgiveravgift._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'utenlandskeMedFastAvgiftsbeloep'), UtenlandskeMedFastAvgiftsbeloep, scope=Arbeidsgiveravgift, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 387, 6)))

Arbeidsgiveravgift._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fradragIGrunnlagetForSone'), FradragIGrunnlaget, scope=Arbeidsgiveravgift, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 388, 6)))

Arbeidsgiveravgift._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fradragIGrunnlagetForUtenlandsk'), FradragIGrunnlagetForUtenlandsk, scope=Arbeidsgiveravgift, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 389, 6)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 384, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 385, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 386, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 387, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 388, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 389, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsgiveravgift._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'loennOgGodtgjoerelse')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 384, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsgiveravgift._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tilskuddOgPremieTilPensjon')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 385, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsgiveravgift._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'utenlandskeMedSaerskiltProsentsats')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 386, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsgiveravgift._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'utenlandskeMedFastAvgiftsbeloep')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 387, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsgiveravgift._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fradragIGrunnlagetForSone')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 388, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Arbeidsgiveravgift._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fradragIGrunnlagetForUtenlandsk')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 389, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Arbeidsgiveravgift._Automaton = _BuildAutomaton_37()




Arbeidsgiveravgiftsgrunnlag._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'beregningskodeForArbeidsgiveravgift'), BeregningskodeForArbeidsgiveravgift, scope=Arbeidsgiveravgiftsgrunnlag, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 394, 6)))

Arbeidsgiveravgiftsgrunnlag._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sone'), Arbeidsgiveravgiftsone, scope=Arbeidsgiveravgiftsgrunnlag, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 395, 6)))

Arbeidsgiveravgiftsgrunnlag._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avgiftsgrunnlagBeloep'), Beloep, scope=Arbeidsgiveravgiftsgrunnlag, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 396, 6)))

Arbeidsgiveravgiftsgrunnlag._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'prosentsatsForAvgiftsberegning'), Grunnlagsprosent, scope=Arbeidsgiveravgiftsgrunnlag, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 397, 6)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Arbeidsgiveravgiftsgrunnlag._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'beregningskodeForArbeidsgiveravgift')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 394, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Arbeidsgiveravgiftsgrunnlag._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sone')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 395, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Arbeidsgiveravgiftsgrunnlag._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avgiftsgrunnlagBeloep')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 396, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Arbeidsgiveravgiftsgrunnlag._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'prosentsatsForAvgiftsberegning')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 397, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Arbeidsgiveravgiftsgrunnlag._Automaton = _BuildAutomaton_38()




UtenlandskeMedSaerskiltProsentsats._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avgiftsgrunnlagBeloep'), Beloep, scope=UtenlandskeMedSaerskiltProsentsats, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 417, 6)))

UtenlandskeMedSaerskiltProsentsats._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'prosentsatsForAvgiftsberegning'), GrunnlagsprosentForUtenlandske, scope=UtenlandskeMedSaerskiltProsentsats, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 418, 6)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UtenlandskeMedSaerskiltProsentsats._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avgiftsgrunnlagBeloep')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 417, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UtenlandskeMedSaerskiltProsentsats._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'prosentsatsForAvgiftsberegning')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 418, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UtenlandskeMedSaerskiltProsentsats._Automaton = _BuildAutomaton_39()




UtenlandskeMedFastAvgiftsbeloep._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'antallAvgiftsgrunnlagPersoner'), Heltall, scope=UtenlandskeMedFastAvgiftsbeloep, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 423, 6)))

UtenlandskeMedFastAvgiftsbeloep._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'beloepssatsForAvgiftsberegning'), GrunnlagsbeloepForUtenlandske, scope=UtenlandskeMedFastAvgiftsbeloep, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 424, 6)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UtenlandskeMedFastAvgiftsbeloep._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'antallAvgiftsgrunnlagPersoner')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 423, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UtenlandskeMedFastAvgiftsbeloep._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'beloepssatsForAvgiftsberegning')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 424, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UtenlandskeMedFastAvgiftsbeloep._Automaton = _BuildAutomaton_40()




FradragIGrunnlaget._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'beregningskodeForArbeidsgiveravgift'), BeregningskodeForArbeidsgiveravgift, scope=FradragIGrunnlaget, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 429, 6)))

FradragIGrunnlaget._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sone'), Arbeidsgiveravgiftsone, scope=FradragIGrunnlaget, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 430, 6)))

FradragIGrunnlaget._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avgiftsfradragBeloep'), Beloep, scope=FradragIGrunnlaget, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 431, 6)))

FradragIGrunnlaget._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'prosentsatsForAvgiftsberegning'), Grunnlagsprosent, scope=FradragIGrunnlaget, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 432, 6)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FradragIGrunnlaget._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'beregningskodeForArbeidsgiveravgift')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 429, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FradragIGrunnlaget._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sone')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 430, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FradragIGrunnlaget._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avgiftsfradragBeloep')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 431, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FradragIGrunnlaget._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'prosentsatsForAvgiftsberegning')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 432, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FradragIGrunnlaget._Automaton = _BuildAutomaton_41()




FradragIGrunnlagetForUtenlandsk._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avgiftsfradragBeloep'), Beloep, scope=FradragIGrunnlagetForUtenlandsk, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 437, 6)))

FradragIGrunnlagetForUtenlandsk._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'prosentsatsForAvgiftsberegning'), GrunnlagsprosentForUtenlandske, scope=FradragIGrunnlagetForUtenlandsk, location=pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 438, 6)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FradragIGrunnlagetForUtenlandsk._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avgiftsfradragBeloep')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 437, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FradragIGrunnlagetForUtenlandsk._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'prosentsatsForAvgiftsberegning')), pyxb.utils.utility.Location('/o/12d/custom/src/apps2grow/apps/l10n_no_payroll/models/amelding_v2_2.xsd', 438, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FradragIGrunnlagetForUtenlandsk._Automaton = _BuildAutomaton_42()

