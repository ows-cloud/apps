# .\amelding.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:0d09d714fd675d48512b57111f69de3b9ccf4461
# Generated 2018-01-11 13:15:44.067000 by PyXB version 1.2.6 using Python 2.7.8.final.0
# Namespace urn:ske:fastsetting:innsamling:a-meldingen:v2_1

from __future__ import unicode_literals

import io

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import pyxb.utils.domutils
import pyxb.utils.six as _six
import pyxb.utils.utility

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier(
    "urn:uuid:257651a1-f6c9-11e7-bce1-bed567469a01"
)

# Version of PyXB used to generate the bindings
_PyXBVersion = "1.2.6"
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(
    "urn:ske:fastsetting:innsamling:a-meldingen:v2_1", create_if_missing=True
)
Namespace.configureCategories(["typeBinding", "elementBinding"])


def CreateFromDocument(xml_text, default_namespace=None, location_base=None):
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
    saxer = pyxb.binding.saxer.make_parser(
        fallback_namespace=default_namespace, location_base=location_base
    )
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance


def CreateFromDOM(node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}InternasjonalIdentifikatortype
class InternasjonalIdentifikatortype(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(
        Namespace, "InternasjonalIdentifikatortype"
    )
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 82, 1
    )
    _Documentation = None


InternasjonalIdentifikatortype._InitializeFacetMap()
Namespace.addCategoryObject(
    "typeBinding", "InternasjonalIdentifikatortype", InternasjonalIdentifikatortype
)
_module_typeBindings.InternasjonalIdentifikatortype = InternasjonalIdentifikatortype

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Landkode
class Landkode(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Landkode")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 85, 1
    )
    _Documentation = None


Landkode._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "Landkode", Landkode)
_module_typeBindings.Landkode = Landkode

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Arbeidsforholdstype
class Arbeidsforholdstype(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Arbeidsforholdstype")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 114, 1
    )
    _Documentation = None


Arbeidsforholdstype._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "Arbeidsforholdstype", Arbeidsforholdstype)
_module_typeBindings.Arbeidsforholdstype = Arbeidsforholdstype

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Avloenningstype
class Avloenningstype(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Avloenningstype")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 117, 1
    )
    _Documentation = None


Avloenningstype._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "Avloenningstype", Avloenningstype)
_module_typeBindings.Avloenningstype = Avloenningstype

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Yrke
class Yrke(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Yrke")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 120, 1
    )
    _Documentation = None


Yrke._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "Yrke", Yrke)
_module_typeBindings.Yrke = Yrke

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Arbeidstidsordning
class Arbeidstidsordning(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Arbeidstidsordning")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 123, 1
    )
    _Documentation = None


Arbeidstidsordning._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "Arbeidstidsordning", Arbeidstidsordning)
_module_typeBindings.Arbeidstidsordning = Arbeidstidsordning

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Skipsregister
class Skipsregister(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Skipsregister")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 133, 1
    )
    _Documentation = None


Skipsregister._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "Skipsregister", Skipsregister)
_module_typeBindings.Skipsregister = Skipsregister

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Skipstype
class Skipstype(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Skipstype")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 136, 1
    )
    _Documentation = None


Skipstype._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "Skipstype", Skipstype)
_module_typeBindings.Skipstype = Skipstype

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Fartsomraade
class Fartsomraade(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Fartsomraade")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 139, 1
    )
    _Documentation = None


Fartsomraade._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "Fartsomraade", Fartsomraade)
_module_typeBindings.Fartsomraade = Fartsomraade

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}PermisjonsOgPermitteringsBeskrivelse
class PermisjonsOgPermitteringsBeskrivelse(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(
        Namespace, "PermisjonsOgPermitteringsBeskrivelse"
    )
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 142, 1
    )
    _Documentation = None


PermisjonsOgPermitteringsBeskrivelse._InitializeFacetMap()
Namespace.addCategoryObject(
    "typeBinding",
    "PermisjonsOgPermitteringsBeskrivelse",
    PermisjonsOgPermitteringsBeskrivelse,
)
_module_typeBindings.PermisjonsOgPermitteringsBeskrivelse = (
    PermisjonsOgPermitteringsBeskrivelse
)

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Fradragsbeskrivelse
class Fradragsbeskrivelse(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Fradragsbeskrivelse")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 160, 1
    )
    _Documentation = None


Fradragsbeskrivelse._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "Fradragsbeskrivelse", Fradragsbeskrivelse)
_module_typeBindings.Fradragsbeskrivelse = Fradragsbeskrivelse

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Forskuddstrekksbeskrivelse
class Forskuddstrekksbeskrivelse(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Forskuddstrekksbeskrivelse")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 169, 1
    )
    _Documentation = None


Forskuddstrekksbeskrivelse._InitializeFacetMap()
Namespace.addCategoryObject(
    "typeBinding", "Forskuddstrekksbeskrivelse", Forskuddstrekksbeskrivelse
)
_module_typeBindings.Forskuddstrekksbeskrivelse = Forskuddstrekksbeskrivelse

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}SkatteOgAvgiftsregel
class SkatteOgAvgiftsregel(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "SkatteOgAvgiftsregel")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 190, 1
    )
    _Documentation = None


SkatteOgAvgiftsregel._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "SkatteOgAvgiftsregel", SkatteOgAvgiftsregel)
_module_typeBindings.SkatteOgAvgiftsregel = SkatteOgAvgiftsregel

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Fordel
class Fordel(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Fordel")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 193, 1
    )
    _Documentation = None


Fordel._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "Fordel", Fordel)
_module_typeBindings.Fordel = Fordel

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Loennsbeskrivelse
class Loennsbeskrivelse(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Loennsbeskrivelse")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 204, 1
    )
    _Documentation = None


Loennsbeskrivelse._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "Loennsbeskrivelse", Loennsbeskrivelse)
_module_typeBindings.Loennsbeskrivelse = Loennsbeskrivelse

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}PersontypeForReiseKostLosji
class PersontypeForReiseKostLosji(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(
        Namespace, "PersontypeForReiseKostLosji"
    )
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 242, 1
    )
    _Documentation = None


PersontypeForReiseKostLosji._InitializeFacetMap()
Namespace.addCategoryObject(
    "typeBinding", "PersontypeForReiseKostLosji", PersontypeForReiseKostLosji
)
_module_typeBindings.PersontypeForReiseKostLosji = PersontypeForReiseKostLosji

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}SpesielleInntjeningsforhold
class SpesielleInntjeningsforhold(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(
        Namespace, "SpesielleInntjeningsforhold"
    )
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 257, 1
    )
    _Documentation = None


SpesielleInntjeningsforhold._InitializeFacetMap()
Namespace.addCategoryObject(
    "typeBinding", "SpesielleInntjeningsforhold", SpesielleInntjeningsforhold
)
_module_typeBindings.SpesielleInntjeningsforhold = SpesielleInntjeningsforhold

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}YtelseFraOffentligeBeskrivelse
class YtelseFraOffentligeBeskrivelse(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(
        Namespace, "YtelseFraOffentligeBeskrivelse"
    )
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 319, 1
    )
    _Documentation = None


YtelseFraOffentligeBeskrivelse._InitializeFacetMap()
Namespace.addCategoryObject(
    "typeBinding", "YtelseFraOffentligeBeskrivelse", YtelseFraOffentligeBeskrivelse
)
_module_typeBindings.YtelseFraOffentligeBeskrivelse = YtelseFraOffentligeBeskrivelse

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}PensjonEllerTrygdebeskrivelse
class PensjonEllerTrygdebeskrivelse(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(
        Namespace, "PensjonEllerTrygdebeskrivelse"
    )
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 328, 1
    )
    _Documentation = None


PensjonEllerTrygdebeskrivelse._InitializeFacetMap()
Namespace.addCategoryObject(
    "typeBinding", "PensjonEllerTrygdebeskrivelse", PensjonEllerTrygdebeskrivelse
)
_module_typeBindings.PensjonEllerTrygdebeskrivelse = PensjonEllerTrygdebeskrivelse

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Naeringsinntektsbeskrivelse
class Naeringsinntektsbeskrivelse(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(
        Namespace, "Naeringsinntektsbeskrivelse"
    )
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 337, 1
    )
    _Documentation = None


Naeringsinntektsbeskrivelse._InitializeFacetMap()
Namespace.addCategoryObject(
    "typeBinding", "Naeringsinntektsbeskrivelse", Naeringsinntektsbeskrivelse
)
_module_typeBindings.Naeringsinntektsbeskrivelse = Naeringsinntektsbeskrivelse

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}OppholdsbeskrivelseForSvalbardJanMayenOgBilandene
class OppholdsbeskrivelseForSvalbardJanMayenOgBilandene(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(
        Namespace, "OppholdsbeskrivelseForSvalbardJanMayenOgBilandene"
    )
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 340, 1
    )
    _Documentation = None


OppholdsbeskrivelseForSvalbardJanMayenOgBilandene._InitializeFacetMap()
Namespace.addCategoryObject(
    "typeBinding",
    "OppholdsbeskrivelseForSvalbardJanMayenOgBilandene",
    OppholdsbeskrivelseForSvalbardJanMayenOgBilandene,
)
_module_typeBindings.OppholdsbeskrivelseForSvalbardJanMayenOgBilandene = (
    OppholdsbeskrivelseForSvalbardJanMayenOgBilandene
)

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}BeregningskodeForArbeidsgiveravgift
class BeregningskodeForArbeidsgiveravgift(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(
        Namespace, "BeregningskodeForArbeidsgiveravgift"
    )
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 375, 1
    )
    _Documentation = None


BeregningskodeForArbeidsgiveravgift._InitializeFacetMap()
Namespace.addCategoryObject(
    "typeBinding",
    "BeregningskodeForArbeidsgiveravgift",
    BeregningskodeForArbeidsgiveravgift,
)
_module_typeBindings.BeregningskodeForArbeidsgiveravgift = (
    BeregningskodeForArbeidsgiveravgift
)

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Arbeidsgiveravgiftsone
class Arbeidsgiveravgiftsone(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Arbeidsgiveravgiftsone")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 378, 1
    )
    _Documentation = None


Arbeidsgiveravgiftsone._InitializeFacetMap()
Namespace.addCategoryObject(
    "typeBinding", "Arbeidsgiveravgiftsone", Arbeidsgiveravgiftsone
)
_module_typeBindings.Arbeidsgiveravgiftsone = Arbeidsgiveravgiftsone

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Grunnlagsprosent
class Grunnlagsprosent(pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Grunnlagsprosent")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 381, 1
    )
    _Documentation = None


Grunnlagsprosent._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "Grunnlagsprosent", Grunnlagsprosent)
_module_typeBindings.Grunnlagsprosent = Grunnlagsprosent

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}GrunnlagsprosentForUtenlandske
class GrunnlagsprosentForUtenlandske(pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(
        Namespace, "GrunnlagsprosentForUtenlandske"
    )
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 384, 1
    )
    _Documentation = None


GrunnlagsprosentForUtenlandske._InitializeFacetMap()
Namespace.addCategoryObject(
    "typeBinding", "GrunnlagsprosentForUtenlandske", GrunnlagsprosentForUtenlandske
)
_module_typeBindings.GrunnlagsprosentForUtenlandske = GrunnlagsprosentForUtenlandske

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}GrunnlagsbeloepForUtenlandske
class GrunnlagsbeloepForUtenlandske(pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(
        Namespace, "GrunnlagsbeloepForUtenlandske"
    )
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 387, 1
    )
    _Documentation = None


GrunnlagsbeloepForUtenlandske._InitializeFacetMap()
Namespace.addCategoryObject(
    "typeBinding", "GrunnlagsbeloepForUtenlandske", GrunnlagsbeloepForUtenlandske
)
_module_typeBindings.GrunnlagsbeloepForUtenlandske = GrunnlagsbeloepForUtenlandske

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}DatoTid
class DatoTid(pyxb.binding.datatypes.dateTime):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "DatoTid")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 416, 1
    )
    _Documentation = None


DatoTid._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "DatoTid", DatoTid)
_module_typeBindings.DatoTid = DatoTid

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}AArOgMaaned
class AArOgMaaned(pyxb.binding.datatypes.gYearMonth):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "AArOgMaaned")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 419, 1
    )
    _Documentation = None


AArOgMaaned._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "AArOgMaaned", AArOgMaaned)
_module_typeBindings.AArOgMaaned = AArOgMaaned

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Tekst
class Tekst(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Tekst")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 422, 1
    )
    _Documentation = None


Tekst._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "Tekst", Tekst)
_module_typeBindings.Tekst = Tekst

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}NorskIdentifikator
class NorskIdentifikator(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "NorskIdentifikator")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 425, 1
    )
    _Documentation = None


NorskIdentifikator._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "NorskIdentifikator", NorskIdentifikator)
_module_typeBindings.NorskIdentifikator = NorskIdentifikator

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}BeloepSomHeltall
class BeloepSomHeltall(pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "BeloepSomHeltall")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 428, 1
    )
    _Documentation = None


BeloepSomHeltall._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "BeloepSomHeltall", BeloepSomHeltall)
_module_typeBindings.BeloepSomHeltall = BeloepSomHeltall

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Beloep
class Beloep(pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Beloep")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 431, 1
    )
    _Documentation = None


Beloep._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "Beloep", Beloep)
_module_typeBindings.Beloep = Beloep

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Dato
class Dato(pyxb.binding.datatypes.date):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Dato")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 434, 1
    )
    _Documentation = None


Dato._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "Dato", Dato)
_module_typeBindings.Dato = Dato

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Desimaltall
class Desimaltall(pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Desimaltall")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 437, 1
    )
    _Documentation = None


Desimaltall._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "Desimaltall", Desimaltall)
_module_typeBindings.Desimaltall = Desimaltall

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Boolsk
class Boolsk(pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Boolsk")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 440, 1
    )
    _Documentation = None


Boolsk._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "Boolsk", Boolsk)
_module_typeBindings.Boolsk = Boolsk

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Heltall
class Heltall(pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Heltall")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 443, 1
    )
    _Documentation = None


Heltall._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "Heltall", Heltall)
_module_typeBindings.Heltall = Heltall

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}AArstall
class AArstall(pyxb.binding.datatypes.gYear):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "AArstall")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 446, 1
    )
    _Documentation = None


AArstall._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "AArstall", AArstall)
_module_typeBindings.AArstall = AArstall

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Spraak
class Spraak(pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Spraak")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 449, 1
    )
    _Documentation = None


Spraak._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=Spraak, enum_prefix=None
)
Spraak.bokmaal = Spraak._CF_enumeration.addEnumeration(
    unicode_value="bokmaal", tag="bokmaal"
)
Spraak.nynorsk = Spraak._CF_enumeration.addEnumeration(
    unicode_value="nynorsk", tag="nynorsk"
)
Spraak.engelsk = Spraak._CF_enumeration.addEnumeration(
    unicode_value="engelsk", tag="engelsk"
)
Spraak._InitializeFacetMap(Spraak._CF_enumeration)
Namespace.addCategoryObject("typeBinding", "Spraak", Spraak)
_module_typeBindings.Spraak = Spraak

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}RestriksjonTekstfelt
class RestriksjonTekstfelt(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "RestriksjonTekstfelt")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 459, 1
    )
    _Documentation = None


RestriksjonTekstfelt._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(255)
)
RestriksjonTekstfelt._InitializeFacetMap(RestriksjonTekstfelt._CF_maxLength)
Namespace.addCategoryObject("typeBinding", "RestriksjonTekstfelt", RestriksjonTekstfelt)
_module_typeBindings.RestriksjonTekstfelt = RestriksjonTekstfelt

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}RestriksjonIdentifikator
class RestriksjonIdentifikator(pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "RestriksjonIdentifikator")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 467, 1
    )
    _Documentation = None


RestriksjonIdentifikator._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(150)
)
RestriksjonIdentifikator._CF_pattern = pyxb.binding.facets.CF_pattern()
RestriksjonIdentifikator._CF_pattern.addPattern(pattern="([0-9a-zA-Z_.-])*")
RestriksjonIdentifikator._InitializeFacetMap(
    RestriksjonIdentifikator._CF_maxLength, RestriksjonIdentifikator._CF_pattern
)
Namespace.addCategoryObject(
    "typeBinding", "RestriksjonIdentifikator", RestriksjonIdentifikator
)
_module_typeBindings.RestriksjonIdentifikator = RestriksjonIdentifikator

# Atomic simple type: [anonymous]
class STD_ANON(AArOgMaaned):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 13, 4
    )
    _Documentation = None


STD_ANON._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(
    value_datatype=STD_ANON, value=pyxb.binding.datatypes.gYearMonth("2099-12")
)
STD_ANON._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(
    value_datatype=STD_ANON, value=pyxb.binding.datatypes.gYearMonth("2014-01")
)
STD_ANON._InitializeFacetMap(STD_ANON._CF_maxInclusive, STD_ANON._CF_minInclusive)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}TekstMedRestriksjon
class TekstMedRestriksjon(RestriksjonTekstfelt):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "TekstMedRestriksjon")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 456, 1
    )
    _Documentation = None


TekstMedRestriksjon._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "TekstMedRestriksjon", TekstMedRestriksjon)
_module_typeBindings.TekstMedRestriksjon = TekstMedRestriksjon

# Atomic simple type: {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Identifikator
class Identifikator(RestriksjonIdentifikator):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Identifikator")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 464, 1
    )
    _Documentation = None


Identifikator._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "Identifikator", Identifikator)
_module_typeBindings.Identifikator = Identifikator

# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}EDAG_M with content type ELEMENT_ONLY
class EDAG_M(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}EDAG_M with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "EDAG_M")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 4, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Leveranse uses Python identifier Leveranse
    __Leveranse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Leveranse"),
        "Leveranse",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_EDAG_M_urnskefastsettinginnsamlinga_meldingenv2_1Leveranse",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 6, 3
        ),
    )

    Leveranse = property(__Leveranse.value, __Leveranse.set, None, None)

    _ElementMap.update({__Leveranse.name(): __Leveranse})
    _AttributeMap.update({})


_module_typeBindings.EDAG_M = EDAG_M
Namespace.addCategoryObject("typeBinding", "EDAG_M", EDAG_M)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Leveranse with content type ELEMENT_ONLY
class Leveranse(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Leveranse with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Leveranse")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 9, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}leveringstidspunkt uses Python identifier leveringstidspunkt
    __leveringstidspunkt = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "leveringstidspunkt"),
        "leveringstidspunkt",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Leveranse_urnskefastsettinginnsamlinga_meldingenv2_1leveringstidspunkt",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 11, 3
        ),
    )

    leveringstidspunkt = property(
        __leveringstidspunkt.value, __leveringstidspunkt.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}kalendermaaned uses Python identifier kalendermaaned
    __kalendermaaned = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "kalendermaaned"),
        "kalendermaaned",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Leveranse_urnskefastsettinginnsamlinga_meldingenv2_1kalendermaaned",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 12, 3
        ),
    )

    kalendermaaned = property(__kalendermaaned.value, __kalendermaaned.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}kildesystem uses Python identifier kildesystem
    __kildesystem = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "kildesystem"),
        "kildesystem",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Leveranse_urnskefastsettinginnsamlinga_meldingenv2_1kildesystem",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 20, 3
        ),
    )

    kildesystem = property(__kildesystem.value, __kildesystem.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}erstatterMeldingsId uses Python identifier erstatterMeldingsId
    __erstatterMeldingsId = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "erstatterMeldingsId"),
        "erstatterMeldingsId",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Leveranse_urnskefastsettinginnsamlinga_meldingenv2_1erstatterMeldingsId",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 21, 3
        ),
    )

    erstatterMeldingsId = property(
        __erstatterMeldingsId.value, __erstatterMeldingsId.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}meldingsId uses Python identifier meldingsId
    __meldingsId = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "meldingsId"),
        "meldingsId",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Leveranse_urnskefastsettinginnsamlinga_meldingenv2_1meldingsId",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 22, 3
        ),
    )

    meldingsId = property(__meldingsId.value, __meldingsId.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}opplysningspliktig uses Python identifier opplysningspliktig
    __opplysningspliktig = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "opplysningspliktig"),
        "opplysningspliktig",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Leveranse_urnskefastsettinginnsamlinga_meldingenv2_1opplysningspliktig",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 23, 3
        ),
    )

    opplysningspliktig = property(
        __opplysningspliktig.value, __opplysningspliktig.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}oppgave uses Python identifier oppgave
    __oppgave = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "oppgave"),
        "oppgave",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Leveranse_urnskefastsettinginnsamlinga_meldingenv2_1oppgave",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 24, 3
        ),
    )

    oppgave = property(__oppgave.value, __oppgave.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}spraakForTilbakemelding uses Python identifier spraakForTilbakemelding
    __spraakForTilbakemelding = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "spraakForTilbakemelding"),
        "spraakForTilbakemelding",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Leveranse_urnskefastsettinginnsamlinga_meldingenv2_1spraakForTilbakemelding",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 25, 3
        ),
    )

    spraakForTilbakemelding = property(
        __spraakForTilbakemelding.value, __spraakForTilbakemelding.set, None, None
    )

    _ElementMap.update(
        {
            __leveringstidspunkt.name(): __leveringstidspunkt,
            __kalendermaaned.name(): __kalendermaaned,
            __kildesystem.name(): __kildesystem,
            __erstatterMeldingsId.name(): __erstatterMeldingsId,
            __meldingsId.name(): __meldingsId,
            __opplysningspliktig.name(): __opplysningspliktig,
            __oppgave.name(): __oppgave,
            __spraakForTilbakemelding.name(): __spraakForTilbakemelding,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Leveranse = Leveranse
Namespace.addCategoryObject("typeBinding", "Leveranse", Leveranse)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Opplysningspliktig with content type ELEMENT_ONLY
class Opplysningspliktig(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Opplysningspliktig with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Opplysningspliktig")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 28, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}norskIdentifikator uses Python identifier norskIdentifikator
    __norskIdentifikator = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "norskIdentifikator"),
        "norskIdentifikator",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Opplysningspliktig_urnskefastsettinginnsamlinga_meldingenv2_1norskIdentifikator",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 30, 3
        ),
    )

    norskIdentifikator = property(
        __norskIdentifikator.value, __norskIdentifikator.set, None, None
    )

    _ElementMap.update({__norskIdentifikator.name(): __norskIdentifikator})
    _AttributeMap.update({})


_module_typeBindings.Opplysningspliktig = Opplysningspliktig
Namespace.addCategoryObject("typeBinding", "Opplysningspliktig", Opplysningspliktig)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}JuridiskEntitet with content type ELEMENT_ONLY
class JuridiskEntitet(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}JuridiskEntitet with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "JuridiskEntitet")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 33, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}betalingsinformasjon uses Python identifier betalingsinformasjon
    __betalingsinformasjon = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "betalingsinformasjon"),
        "betalingsinformasjon",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_JuridiskEntitet_urnskefastsettinginnsamlinga_meldingenv2_1betalingsinformasjon",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 35, 3
        ),
    )

    betalingsinformasjon = property(
        __betalingsinformasjon.value, __betalingsinformasjon.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}betalingsinformasjonForForenkletOrdning uses Python identifier betalingsinformasjonForForenkletOrdning
    __betalingsinformasjonForForenkletOrdning = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(
            Namespace, "betalingsinformasjonForForenkletOrdning"
        ),
        "betalingsinformasjonForForenkletOrdning",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_JuridiskEntitet_urnskefastsettinginnsamlinga_meldingenv2_1betalingsinformasjonForForenkletOrdning",
        True,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 36, 3
        ),
    )

    betalingsinformasjonForForenkletOrdning = property(
        __betalingsinformasjonForForenkletOrdning.value,
        __betalingsinformasjonForForenkletOrdning.set,
        None,
        None,
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}annenBagatellmessigStoette uses Python identifier annenBagatellmessigStoette
    __annenBagatellmessigStoette = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "annenBagatellmessigStoette"),
        "annenBagatellmessigStoette",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_JuridiskEntitet_urnskefastsettinginnsamlinga_meldingenv2_1annenBagatellmessigStoette",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 37, 3
        ),
    )

    annenBagatellmessigStoette = property(
        __annenBagatellmessigStoette.value, __annenBagatellmessigStoette.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}virksomhet uses Python identifier virksomhet
    __virksomhet = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "virksomhet"),
        "virksomhet",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_JuridiskEntitet_urnskefastsettinginnsamlinga_meldingenv2_1virksomhet",
        True,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 38, 3
        ),
    )

    virksomhet = property(__virksomhet.value, __virksomhet.set, None, None)

    _ElementMap.update(
        {
            __betalingsinformasjon.name(): __betalingsinformasjon,
            __betalingsinformasjonForForenkletOrdning.name(): __betalingsinformasjonForForenkletOrdning,
            __annenBagatellmessigStoette.name(): __annenBagatellmessigStoette,
            __virksomhet.name(): __virksomhet,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.JuridiskEntitet = JuridiskEntitet
Namespace.addCategoryObject("typeBinding", "JuridiskEntitet", JuridiskEntitet)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Betalingsinformasjon with content type ELEMENT_ONLY
class Betalingsinformasjon(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Betalingsinformasjon with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Betalingsinformasjon")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 41, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}sumForskuddstrekk uses Python identifier sumForskuddstrekk
    __sumForskuddstrekk = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "sumForskuddstrekk"),
        "sumForskuddstrekk",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Betalingsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_1sumForskuddstrekk",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 43, 3
        ),
    )

    sumForskuddstrekk = property(
        __sumForskuddstrekk.value, __sumForskuddstrekk.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}sumArbeidsgiveravgift uses Python identifier sumArbeidsgiveravgift
    __sumArbeidsgiveravgift = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "sumArbeidsgiveravgift"),
        "sumArbeidsgiveravgift",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Betalingsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_1sumArbeidsgiveravgift",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 44, 3
        ),
    )

    sumArbeidsgiveravgift = property(
        __sumArbeidsgiveravgift.value, __sumArbeidsgiveravgift.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}sumFinansskattLoenn uses Python identifier sumFinansskattLoenn
    __sumFinansskattLoenn = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "sumFinansskattLoenn"),
        "sumFinansskattLoenn",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Betalingsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_1sumFinansskattLoenn",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 45, 3
        ),
    )

    sumFinansskattLoenn = property(
        __sumFinansskattLoenn.value, __sumFinansskattLoenn.set, None, None
    )

    _ElementMap.update(
        {
            __sumForskuddstrekk.name(): __sumForskuddstrekk,
            __sumArbeidsgiveravgift.name(): __sumArbeidsgiveravgift,
            __sumFinansskattLoenn.name(): __sumFinansskattLoenn,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Betalingsinformasjon = Betalingsinformasjon
Namespace.addCategoryObject("typeBinding", "Betalingsinformasjon", Betalingsinformasjon)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}BetalingsinformasjonForForenkletOrdning with content type ELEMENT_ONLY
class BetalingsinformasjonForForenkletOrdning(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}BetalingsinformasjonForForenkletOrdning with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(
        Namespace, "BetalingsinformasjonForForenkletOrdning"
    )
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 48, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}sumForskuddstrekk uses Python identifier sumForskuddstrekk
    __sumForskuddstrekk = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "sumForskuddstrekk"),
        "sumForskuddstrekk",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_BetalingsinformasjonForForenkletOrdning_urnskefastsettinginnsamlinga_meldingenv2_1sumForskuddstrekk",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 50, 3
        ),
    )

    sumForskuddstrekk = property(
        __sumForskuddstrekk.value, __sumForskuddstrekk.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}sumArbeidsgiveravgift uses Python identifier sumArbeidsgiveravgift
    __sumArbeidsgiveravgift = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "sumArbeidsgiveravgift"),
        "sumArbeidsgiveravgift",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_BetalingsinformasjonForForenkletOrdning_urnskefastsettinginnsamlinga_meldingenv2_1sumArbeidsgiveravgift",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 51, 3
        ),
    )

    sumArbeidsgiveravgift = property(
        __sumArbeidsgiveravgift.value, __sumArbeidsgiveravgift.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}loennsutbetalingsdato uses Python identifier loennsutbetalingsdato
    __loennsutbetalingsdato = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "loennsutbetalingsdato"),
        "loennsutbetalingsdato",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_BetalingsinformasjonForForenkletOrdning_urnskefastsettinginnsamlinga_meldingenv2_1loennsutbetalingsdato",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 52, 3
        ),
    )

    loennsutbetalingsdato = property(
        __loennsutbetalingsdato.value, __loennsutbetalingsdato.set, None, None
    )

    _ElementMap.update(
        {
            __sumForskuddstrekk.name(): __sumForskuddstrekk,
            __sumArbeidsgiveravgift.name(): __sumArbeidsgiveravgift,
            __loennsutbetalingsdato.name(): __loennsutbetalingsdato,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.BetalingsinformasjonForForenkletOrdning = (
    BetalingsinformasjonForForenkletOrdning
)
Namespace.addCategoryObject(
    "typeBinding",
    "BetalingsinformasjonForForenkletOrdning",
    BetalingsinformasjonForForenkletOrdning,
)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Virksomhet with content type ELEMENT_ONLY
class Virksomhet(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Virksomhet with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Virksomhet")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 55, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}norskIdentifikator uses Python identifier norskIdentifikator
    __norskIdentifikator = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "norskIdentifikator"),
        "norskIdentifikator",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Virksomhet_urnskefastsettinginnsamlinga_meldingenv2_1norskIdentifikator",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 57, 3
        ),
    )

    norskIdentifikator = property(
        __norskIdentifikator.value, __norskIdentifikator.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}inntektsmottaker uses Python identifier inntektsmottaker
    __inntektsmottaker = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "inntektsmottaker"),
        "inntektsmottaker",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Virksomhet_urnskefastsettinginnsamlinga_meldingenv2_1inntektsmottaker",
        True,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 58, 3
        ),
    )

    inntektsmottaker = property(
        __inntektsmottaker.value, __inntektsmottaker.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}arbeidsgiveravgift uses Python identifier arbeidsgiveravgift
    __arbeidsgiveravgift = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "arbeidsgiveravgift"),
        "arbeidsgiveravgift",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Virksomhet_urnskefastsettinginnsamlinga_meldingenv2_1arbeidsgiveravgift",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 59, 3
        ),
    )

    arbeidsgiveravgift = property(
        __arbeidsgiveravgift.value, __arbeidsgiveravgift.set, None, None
    )

    _ElementMap.update(
        {
            __norskIdentifikator.name(): __norskIdentifikator,
            __inntektsmottaker.name(): __inntektsmottaker,
            __arbeidsgiveravgift.name(): __arbeidsgiveravgift,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Virksomhet = Virksomhet
Namespace.addCategoryObject("typeBinding", "Virksomhet", Virksomhet)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Inntektsmottaker with content type ELEMENT_ONLY
class Inntektsmottaker(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Inntektsmottaker with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Inntektsmottaker")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 62, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}norskIdentifikator uses Python identifier norskIdentifikator
    __norskIdentifikator = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "norskIdentifikator"),
        "norskIdentifikator",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntektsmottaker_urnskefastsettinginnsamlinga_meldingenv2_1norskIdentifikator",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 64, 3
        ),
    )

    norskIdentifikator = property(
        __norskIdentifikator.value, __norskIdentifikator.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}internasjonalIdentifikator uses Python identifier internasjonalIdentifikator
    __internasjonalIdentifikator = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "internasjonalIdentifikator"),
        "internasjonalIdentifikator",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntektsmottaker_urnskefastsettinginnsamlinga_meldingenv2_1internasjonalIdentifikator",
        True,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 65, 3
        ),
    )

    internasjonalIdentifikator = property(
        __internasjonalIdentifikator.value, __internasjonalIdentifikator.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}identifiserendeInformasjon uses Python identifier identifiserendeInformasjon
    __identifiserendeInformasjon = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "identifiserendeInformasjon"),
        "identifiserendeInformasjon",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntektsmottaker_urnskefastsettinginnsamlinga_meldingenv2_1identifiserendeInformasjon",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 66, 3
        ),
    )

    identifiserendeInformasjon = property(
        __identifiserendeInformasjon.value, __identifiserendeInformasjon.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}arbeidsforhold uses Python identifier arbeidsforhold
    __arbeidsforhold = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "arbeidsforhold"),
        "arbeidsforhold",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntektsmottaker_urnskefastsettinginnsamlinga_meldingenv2_1arbeidsforhold",
        True,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 67, 3
        ),
    )

    arbeidsforhold = property(__arbeidsforhold.value, __arbeidsforhold.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}fradrag uses Python identifier fradrag
    __fradrag = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "fradrag"),
        "fradrag",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntektsmottaker_urnskefastsettinginnsamlinga_meldingenv2_1fradrag",
        True,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 68, 3
        ),
    )

    fradrag = property(__fradrag.value, __fradrag.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}forskuddstrekk uses Python identifier forskuddstrekk
    __forskuddstrekk = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "forskuddstrekk"),
        "forskuddstrekk",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntektsmottaker_urnskefastsettinginnsamlinga_meldingenv2_1forskuddstrekk",
        True,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 69, 3
        ),
    )

    forskuddstrekk = property(__forskuddstrekk.value, __forskuddstrekk.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}inntekt uses Python identifier inntekt
    __inntekt = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "inntekt"),
        "inntekt",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntektsmottaker_urnskefastsettinginnsamlinga_meldingenv2_1inntekt",
        True,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 70, 3
        ),
    )

    inntekt = property(__inntekt.value, __inntekt.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}sjoefolksrelatertInformasjon uses Python identifier sjoefolksrelatertInformasjon
    __sjoefolksrelatertInformasjon = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "sjoefolksrelatertInformasjon"),
        "sjoefolksrelatertInformasjon",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntektsmottaker_urnskefastsettinginnsamlinga_meldingenv2_1sjoefolksrelatertInformasjon",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 71, 3
        ),
    )

    sjoefolksrelatertInformasjon = property(
        __sjoefolksrelatertInformasjon.value,
        __sjoefolksrelatertInformasjon.set,
        None,
        None,
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}oppholdPaaSvalbardJanMayenOgBilandene uses Python identifier oppholdPaaSvalbardJanMayenOgBilandene
    __oppholdPaaSvalbardJanMayenOgBilandene = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "oppholdPaaSvalbardJanMayenOgBilandene"),
        "oppholdPaaSvalbardJanMayenOgBilandene",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntektsmottaker_urnskefastsettinginnsamlinga_meldingenv2_1oppholdPaaSvalbardJanMayenOgBilandene",
        True,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 72, 3
        ),
    )

    oppholdPaaSvalbardJanMayenOgBilandene = property(
        __oppholdPaaSvalbardJanMayenOgBilandene.value,
        __oppholdPaaSvalbardJanMayenOgBilandene.set,
        None,
        None,
    )

    _ElementMap.update(
        {
            __norskIdentifikator.name(): __norskIdentifikator,
            __internasjonalIdentifikator.name(): __internasjonalIdentifikator,
            __identifiserendeInformasjon.name(): __identifiserendeInformasjon,
            __arbeidsforhold.name(): __arbeidsforhold,
            __fradrag.name(): __fradrag,
            __forskuddstrekk.name(): __forskuddstrekk,
            __inntekt.name(): __inntekt,
            __sjoefolksrelatertInformasjon.name(): __sjoefolksrelatertInformasjon,
            __oppholdPaaSvalbardJanMayenOgBilandene.name(): __oppholdPaaSvalbardJanMayenOgBilandene,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Inntektsmottaker = Inntektsmottaker
Namespace.addCategoryObject("typeBinding", "Inntektsmottaker", Inntektsmottaker)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}InternasjonalIdentifikator with content type ELEMENT_ONLY
class InternasjonalIdentifikator(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}InternasjonalIdentifikator with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "InternasjonalIdentifikator")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 75, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}identifikator uses Python identifier identifikator
    __identifikator = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "identifikator"),
        "identifikator",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_InternasjonalIdentifikator_urnskefastsettinginnsamlinga_meldingenv2_1identifikator",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 77, 3
        ),
    )

    identifikator = property(__identifikator.value, __identifikator.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}identifikatortype uses Python identifier identifikatortype
    __identifikatortype = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "identifikatortype"),
        "identifikatortype",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_InternasjonalIdentifikator_urnskefastsettinginnsamlinga_meldingenv2_1identifikatortype",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 78, 3
        ),
    )

    identifikatortype = property(
        __identifikatortype.value, __identifikatortype.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}land uses Python identifier land
    __land = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "land"),
        "land",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_InternasjonalIdentifikator_urnskefastsettinginnsamlinga_meldingenv2_1land",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 79, 3
        ),
    )

    land = property(__land.value, __land.set, None, None)

    _ElementMap.update(
        {
            __identifikator.name(): __identifikator,
            __identifikatortype.name(): __identifikatortype,
            __land.name(): __land,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.InternasjonalIdentifikator = InternasjonalIdentifikator
Namespace.addCategoryObject(
    "typeBinding", "InternasjonalIdentifikator", InternasjonalIdentifikator
)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}IdentifiserendeInformasjon with content type ELEMENT_ONLY
class IdentifiserendeInformasjon(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}IdentifiserendeInformasjon with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "IdentifiserendeInformasjon")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 88, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}navn uses Python identifier navn
    __navn = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "navn"),
        "navn",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_IdentifiserendeInformasjon_urnskefastsettinginnsamlinga_meldingenv2_1navn",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 90, 3
        ),
    )

    navn = property(__navn.value, __navn.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}foedselsdato uses Python identifier foedselsdato
    __foedselsdato = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "foedselsdato"),
        "foedselsdato",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_IdentifiserendeInformasjon_urnskefastsettinginnsamlinga_meldingenv2_1foedselsdato",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 91, 3
        ),
    )

    foedselsdato = property(__foedselsdato.value, __foedselsdato.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}ansattnummer uses Python identifier ansattnummer
    __ansattnummer = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ansattnummer"),
        "ansattnummer",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_IdentifiserendeInformasjon_urnskefastsettinginnsamlinga_meldingenv2_1ansattnummer",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 92, 3
        ),
    )

    ansattnummer = property(__ansattnummer.value, __ansattnummer.set, None, None)

    _ElementMap.update(
        {
            __navn.name(): __navn,
            __foedselsdato.name(): __foedselsdato,
            __ansattnummer.name(): __ansattnummer,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.IdentifiserendeInformasjon = IdentifiserendeInformasjon
Namespace.addCategoryObject(
    "typeBinding", "IdentifiserendeInformasjon", IdentifiserendeInformasjon
)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Arbeidsforhold with content type ELEMENT_ONLY
class Arbeidsforhold(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Arbeidsforhold with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Arbeidsforhold")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 95, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}arbeidsforholdId uses Python identifier arbeidsforholdId
    __arbeidsforholdId = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "arbeidsforholdId"),
        "arbeidsforholdId",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_1arbeidsforholdId",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 97, 3
        ),
    )

    arbeidsforholdId = property(
        __arbeidsforholdId.value, __arbeidsforholdId.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}typeArbeidsforhold uses Python identifier typeArbeidsforhold
    __typeArbeidsforhold = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "typeArbeidsforhold"),
        "typeArbeidsforhold",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_1typeArbeidsforhold",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 98, 3
        ),
    )

    typeArbeidsforhold = property(
        __typeArbeidsforhold.value, __typeArbeidsforhold.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}startdato uses Python identifier startdato
    __startdato = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "startdato"),
        "startdato",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_1startdato",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 99, 3
        ),
    )

    startdato = property(__startdato.value, __startdato.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}sluttdato uses Python identifier sluttdato
    __sluttdato = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "sluttdato"),
        "sluttdato",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_1sluttdato",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 100, 3
        ),
    )

    sluttdato = property(__sluttdato.value, __sluttdato.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}antallTimerPerUkeSomEnFullStillingTilsvarer uses Python identifier antallTimerPerUkeSomEnFullStillingTilsvarer
    __antallTimerPerUkeSomEnFullStillingTilsvarer = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(
            Namespace, "antallTimerPerUkeSomEnFullStillingTilsvarer"
        ),
        "antallTimerPerUkeSomEnFullStillingTilsvarer",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_1antallTimerPerUkeSomEnFullStillingTilsvarer",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 101, 3
        ),
    )

    antallTimerPerUkeSomEnFullStillingTilsvarer = property(
        __antallTimerPerUkeSomEnFullStillingTilsvarer.value,
        __antallTimerPerUkeSomEnFullStillingTilsvarer.set,
        None,
        None,
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}avloenningstype uses Python identifier avloenningstype
    __avloenningstype = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "avloenningstype"),
        "avloenningstype",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_1avloenningstype",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 102, 3
        ),
    )

    avloenningstype = property(
        __avloenningstype.value, __avloenningstype.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}yrke uses Python identifier yrke
    __yrke = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "yrke"),
        "yrke",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_1yrke",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 103, 3
        ),
    )

    yrke = property(__yrke.value, __yrke.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}arbeidstidsordning uses Python identifier arbeidstidsordning
    __arbeidstidsordning = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "arbeidstidsordning"),
        "arbeidstidsordning",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_1arbeidstidsordning",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 104, 3
        ),
    )

    arbeidstidsordning = property(
        __arbeidstidsordning.value, __arbeidstidsordning.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}stillingsprosent uses Python identifier stillingsprosent
    __stillingsprosent = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "stillingsprosent"),
        "stillingsprosent",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_1stillingsprosent",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 105, 3
        ),
    )

    stillingsprosent = property(
        __stillingsprosent.value, __stillingsprosent.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}sisteLoennsendringsdato uses Python identifier sisteLoennsendringsdato
    __sisteLoennsendringsdato = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "sisteLoennsendringsdato"),
        "sisteLoennsendringsdato",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_1sisteLoennsendringsdato",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 106, 3
        ),
    )

    sisteLoennsendringsdato = property(
        __sisteLoennsendringsdato.value, __sisteLoennsendringsdato.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}loennsansiennitet uses Python identifier loennsansiennitet
    __loennsansiennitet = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "loennsansiennitet"),
        "loennsansiennitet",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_1loennsansiennitet",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 107, 3
        ),
    )

    loennsansiennitet = property(
        __loennsansiennitet.value, __loennsansiennitet.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}loennstrinn uses Python identifier loennstrinn
    __loennstrinn = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "loennstrinn"),
        "loennstrinn",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_1loennstrinn",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 108, 3
        ),
    )

    loennstrinn = property(__loennstrinn.value, __loennstrinn.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}fartoey uses Python identifier fartoey
    __fartoey = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "fartoey"),
        "fartoey",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_1fartoey",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 109, 3
        ),
    )

    fartoey = property(__fartoey.value, __fartoey.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}permisjon uses Python identifier permisjon
    __permisjon = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "permisjon"),
        "permisjon",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_1permisjon",
        True,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 110, 3
        ),
    )

    permisjon = property(__permisjon.value, __permisjon.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}sisteDatoForStillingsprosentendring uses Python identifier sisteDatoForStillingsprosentendring
    __sisteDatoForStillingsprosentendring = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "sisteDatoForStillingsprosentendring"),
        "sisteDatoForStillingsprosentendring",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsforhold_urnskefastsettinginnsamlinga_meldingenv2_1sisteDatoForStillingsprosentendring",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 111, 3
        ),
    )

    sisteDatoForStillingsprosentendring = property(
        __sisteDatoForStillingsprosentendring.value,
        __sisteDatoForStillingsprosentendring.set,
        None,
        None,
    )

    _ElementMap.update(
        {
            __arbeidsforholdId.name(): __arbeidsforholdId,
            __typeArbeidsforhold.name(): __typeArbeidsforhold,
            __startdato.name(): __startdato,
            __sluttdato.name(): __sluttdato,
            __antallTimerPerUkeSomEnFullStillingTilsvarer.name(): __antallTimerPerUkeSomEnFullStillingTilsvarer,
            __avloenningstype.name(): __avloenningstype,
            __yrke.name(): __yrke,
            __arbeidstidsordning.name(): __arbeidstidsordning,
            __stillingsprosent.name(): __stillingsprosent,
            __sisteLoennsendringsdato.name(): __sisteLoennsendringsdato,
            __loennsansiennitet.name(): __loennsansiennitet,
            __loennstrinn.name(): __loennstrinn,
            __fartoey.name(): __fartoey,
            __permisjon.name(): __permisjon,
            __sisteDatoForStillingsprosentendring.name(): __sisteDatoForStillingsprosentendring,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Arbeidsforhold = Arbeidsforhold
Namespace.addCategoryObject("typeBinding", "Arbeidsforhold", Arbeidsforhold)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Fartoey with content type ELEMENT_ONLY
class Fartoey(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Fartoey with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Fartoey")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 126, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}skipsregister uses Python identifier skipsregister
    __skipsregister = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "skipsregister"),
        "skipsregister",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Fartoey_urnskefastsettinginnsamlinga_meldingenv2_1skipsregister",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 128, 3
        ),
    )

    skipsregister = property(__skipsregister.value, __skipsregister.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}skipstype uses Python identifier skipstype
    __skipstype = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "skipstype"),
        "skipstype",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Fartoey_urnskefastsettinginnsamlinga_meldingenv2_1skipstype",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 129, 3
        ),
    )

    skipstype = property(__skipstype.value, __skipstype.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}fartsomraade uses Python identifier fartsomraade
    __fartsomraade = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "fartsomraade"),
        "fartsomraade",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Fartoey_urnskefastsettinginnsamlinga_meldingenv2_1fartsomraade",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 130, 3
        ),
    )

    fartsomraade = property(__fartsomraade.value, __fartsomraade.set, None, None)

    _ElementMap.update(
        {
            __skipsregister.name(): __skipsregister,
            __skipstype.name(): __skipstype,
            __fartsomraade.name(): __fartsomraade,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Fartoey = Fartoey
Namespace.addCategoryObject("typeBinding", "Fartoey", Fartoey)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Permisjon with content type ELEMENT_ONLY
class Permisjon(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Permisjon with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Permisjon")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 145, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}startdato uses Python identifier startdato
    __startdato = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "startdato"),
        "startdato",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Permisjon_urnskefastsettinginnsamlinga_meldingenv2_1startdato",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 147, 3
        ),
    )

    startdato = property(__startdato.value, __startdato.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}sluttdato uses Python identifier sluttdato
    __sluttdato = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "sluttdato"),
        "sluttdato",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Permisjon_urnskefastsettinginnsamlinga_meldingenv2_1sluttdato",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 148, 3
        ),
    )

    sluttdato = property(__sluttdato.value, __sluttdato.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}permisjonsprosent uses Python identifier permisjonsprosent
    __permisjonsprosent = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "permisjonsprosent"),
        "permisjonsprosent",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Permisjon_urnskefastsettinginnsamlinga_meldingenv2_1permisjonsprosent",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 149, 3
        ),
    )

    permisjonsprosent = property(
        __permisjonsprosent.value, __permisjonsprosent.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}permisjonId uses Python identifier permisjonId
    __permisjonId = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "permisjonId"),
        "permisjonId",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Permisjon_urnskefastsettinginnsamlinga_meldingenv2_1permisjonId",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 150, 3
        ),
    )

    permisjonId = property(__permisjonId.value, __permisjonId.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "beskrivelse"),
        "beskrivelse",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Permisjon_urnskefastsettinginnsamlinga_meldingenv2_1beskrivelse",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 151, 3
        ),
    )

    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    _ElementMap.update(
        {
            __startdato.name(): __startdato,
            __sluttdato.name(): __sluttdato,
            __permisjonsprosent.name(): __permisjonsprosent,
            __permisjonId.name(): __permisjonId,
            __beskrivelse.name(): __beskrivelse,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Permisjon = Permisjon
Namespace.addCategoryObject("typeBinding", "Permisjon", Permisjon)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Fradrag with content type ELEMENT_ONLY
class Fradrag(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Fradrag with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Fradrag")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 154, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "beskrivelse"),
        "beskrivelse",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Fradrag_urnskefastsettinginnsamlinga_meldingenv2_1beskrivelse",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 156, 3
        ),
    )

    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}beloep uses Python identifier beloep
    __beloep = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "beloep"),
        "beloep",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Fradrag_urnskefastsettinginnsamlinga_meldingenv2_1beloep",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 157, 3
        ),
    )

    beloep = property(__beloep.value, __beloep.set, None, None)

    _ElementMap.update({__beskrivelse.name(): __beskrivelse, __beloep.name(): __beloep})
    _AttributeMap.update({})


_module_typeBindings.Fradrag = Fradrag
Namespace.addCategoryObject("typeBinding", "Fradrag", Fradrag)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Forskuddstrekk with content type ELEMENT_ONLY
class Forskuddstrekk(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Forskuddstrekk with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Forskuddstrekk")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 163, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "beskrivelse"),
        "beskrivelse",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Forskuddstrekk_urnskefastsettinginnsamlinga_meldingenv2_1beskrivelse",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 165, 3
        ),
    )

    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}beloep uses Python identifier beloep
    __beloep = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "beloep"),
        "beloep",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Forskuddstrekk_urnskefastsettinginnsamlinga_meldingenv2_1beloep",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 166, 3
        ),
    )

    beloep = property(__beloep.value, __beloep.set, None, None)

    _ElementMap.update({__beskrivelse.name(): __beskrivelse, __beloep.name(): __beloep})
    _AttributeMap.update({})


_module_typeBindings.Forskuddstrekk = Forskuddstrekk
Namespace.addCategoryObject("typeBinding", "Forskuddstrekk", Forskuddstrekk)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Inntekt with content type ELEMENT_ONLY
class Inntekt(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Inntekt with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Inntekt")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 172, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}skatteOgAvgiftsregel uses Python identifier skatteOgAvgiftsregel
    __skatteOgAvgiftsregel = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "skatteOgAvgiftsregel"),
        "skatteOgAvgiftsregel",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_1skatteOgAvgiftsregel",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 174, 3
        ),
    )

    skatteOgAvgiftsregel = property(
        __skatteOgAvgiftsregel.value, __skatteOgAvgiftsregel.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}startdatoOpptjeningsperiode uses Python identifier startdatoOpptjeningsperiode
    __startdatoOpptjeningsperiode = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "startdatoOpptjeningsperiode"),
        "startdatoOpptjeningsperiode",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_1startdatoOpptjeningsperiode",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 175, 3
        ),
    )

    startdatoOpptjeningsperiode = property(
        __startdatoOpptjeningsperiode.value,
        __startdatoOpptjeningsperiode.set,
        None,
        None,
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}sluttdatoOpptjeningsperiode uses Python identifier sluttdatoOpptjeningsperiode
    __sluttdatoOpptjeningsperiode = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "sluttdatoOpptjeningsperiode"),
        "sluttdatoOpptjeningsperiode",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_1sluttdatoOpptjeningsperiode",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 176, 3
        ),
    )

    sluttdatoOpptjeningsperiode = property(
        __sluttdatoOpptjeningsperiode.value,
        __sluttdatoOpptjeningsperiode.set,
        None,
        None,
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}fordel uses Python identifier fordel
    __fordel = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "fordel"),
        "fordel",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_1fordel",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 177, 3
        ),
    )

    fordel = property(__fordel.value, __fordel.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}utloeserArbeidsgiveravgift uses Python identifier utloeserArbeidsgiveravgift
    __utloeserArbeidsgiveravgift = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "utloeserArbeidsgiveravgift"),
        "utloeserArbeidsgiveravgift",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_1utloeserArbeidsgiveravgift",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 178, 3
        ),
    )

    utloeserArbeidsgiveravgift = property(
        __utloeserArbeidsgiveravgift.value, __utloeserArbeidsgiveravgift.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}inngaarIGrunnlagForTrekk uses Python identifier inngaarIGrunnlagForTrekk
    __inngaarIGrunnlagForTrekk = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "inngaarIGrunnlagForTrekk"),
        "inngaarIGrunnlagForTrekk",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_1inngaarIGrunnlagForTrekk",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 179, 3
        ),
    )

    inngaarIGrunnlagForTrekk = property(
        __inngaarIGrunnlagForTrekk.value, __inngaarIGrunnlagForTrekk.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}beloep uses Python identifier beloep
    __beloep = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "beloep"),
        "beloep",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_1beloep",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 180, 3
        ),
    )

    beloep = property(__beloep.value, __beloep.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}arbeidsforholdId uses Python identifier arbeidsforholdId
    __arbeidsforholdId = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "arbeidsforholdId"),
        "arbeidsforholdId",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_1arbeidsforholdId",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 181, 3
        ),
    )

    arbeidsforholdId = property(
        __arbeidsforholdId.value, __arbeidsforholdId.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}loennsinntekt uses Python identifier loennsinntekt
    __loennsinntekt = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "loennsinntekt"),
        "loennsinntekt",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_1loennsinntekt",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 183, 4
        ),
    )

    loennsinntekt = property(__loennsinntekt.value, __loennsinntekt.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}ytelseFraOffentlige uses Python identifier ytelseFraOffentlige
    __ytelseFraOffentlige = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ytelseFraOffentlige"),
        "ytelseFraOffentlige",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_1ytelseFraOffentlige",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 184, 4
        ),
    )

    ytelseFraOffentlige = property(
        __ytelseFraOffentlige.value, __ytelseFraOffentlige.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}pensjonEllerTrygd uses Python identifier pensjonEllerTrygd
    __pensjonEllerTrygd = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "pensjonEllerTrygd"),
        "pensjonEllerTrygd",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_1pensjonEllerTrygd",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 185, 4
        ),
    )

    pensjonEllerTrygd = property(
        __pensjonEllerTrygd.value, __pensjonEllerTrygd.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}naeringsinntekt uses Python identifier naeringsinntekt
    __naeringsinntekt = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "naeringsinntekt"),
        "naeringsinntekt",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Inntekt_urnskefastsettinginnsamlinga_meldingenv2_1naeringsinntekt",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 186, 4
        ),
    )

    naeringsinntekt = property(
        __naeringsinntekt.value, __naeringsinntekt.set, None, None
    )

    _ElementMap.update(
        {
            __skatteOgAvgiftsregel.name(): __skatteOgAvgiftsregel,
            __startdatoOpptjeningsperiode.name(): __startdatoOpptjeningsperiode,
            __sluttdatoOpptjeningsperiode.name(): __sluttdatoOpptjeningsperiode,
            __fordel.name(): __fordel,
            __utloeserArbeidsgiveravgift.name(): __utloeserArbeidsgiveravgift,
            __inngaarIGrunnlagForTrekk.name(): __inngaarIGrunnlagForTrekk,
            __beloep.name(): __beloep,
            __arbeidsforholdId.name(): __arbeidsforholdId,
            __loennsinntekt.name(): __loennsinntekt,
            __ytelseFraOffentlige.name(): __ytelseFraOffentlige,
            __pensjonEllerTrygd.name(): __pensjonEllerTrygd,
            __naeringsinntekt.name(): __naeringsinntekt,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Inntekt = Inntekt
Namespace.addCategoryObject("typeBinding", "Inntekt", Inntekt)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Loennsinntekt with content type ELEMENT_ONLY
class Loennsinntekt(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Loennsinntekt with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Loennsinntekt")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 196, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "beskrivelse"),
        "beskrivelse",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Loennsinntekt_urnskefastsettinginnsamlinga_meldingenv2_1beskrivelse",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 198, 3
        ),
    )

    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}tilleggsinformasjon uses Python identifier tilleggsinformasjon
    __tilleggsinformasjon = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "tilleggsinformasjon"),
        "tilleggsinformasjon",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Loennsinntekt_urnskefastsettinginnsamlinga_meldingenv2_1tilleggsinformasjon",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 199, 3
        ),
    )

    tilleggsinformasjon = property(
        __tilleggsinformasjon.value, __tilleggsinformasjon.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}spesifikasjon uses Python identifier spesifikasjon
    __spesifikasjon = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "spesifikasjon"),
        "spesifikasjon",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Loennsinntekt_urnskefastsettinginnsamlinga_meldingenv2_1spesifikasjon",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 200, 3
        ),
    )

    spesifikasjon = property(__spesifikasjon.value, __spesifikasjon.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}antall uses Python identifier antall
    __antall = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "antall"),
        "antall",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Loennsinntekt_urnskefastsettinginnsamlinga_meldingenv2_1antall",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 201, 3
        ),
    )

    antall = property(__antall.value, __antall.set, None, None)

    _ElementMap.update(
        {
            __beskrivelse.name(): __beskrivelse,
            __tilleggsinformasjon.name(): __tilleggsinformasjon,
            __spesifikasjon.name(): __spesifikasjon,
            __antall.name(): __antall,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Loennsinntekt = Loennsinntekt
Namespace.addCategoryObject("typeBinding", "Loennsinntekt", Loennsinntekt)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Tilleggsinformasjon with content type ELEMENT_ONLY
class Tilleggsinformasjon(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Tilleggsinformasjon with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Tilleggsinformasjon")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 207, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}bilOgBaat uses Python identifier bilOgBaat
    __bilOgBaat = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "bilOgBaat"),
        "bilOgBaat",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_1bilOgBaat",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 209, 3
        ),
    )

    bilOgBaat = property(__bilOgBaat.value, __bilOgBaat.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}dagmammaIEgenBolig uses Python identifier dagmammaIEgenBolig
    __dagmammaIEgenBolig = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "dagmammaIEgenBolig"),
        "dagmammaIEgenBolig",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_1dagmammaIEgenBolig",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 210, 3
        ),
    )

    dagmammaIEgenBolig = property(
        __dagmammaIEgenBolig.value, __dagmammaIEgenBolig.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}etterbetalingsperiode uses Python identifier etterbetalingsperiode
    __etterbetalingsperiode = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "etterbetalingsperiode"),
        "etterbetalingsperiode",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_1etterbetalingsperiode",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 211, 3
        ),
    )

    etterbetalingsperiode = property(
        __etterbetalingsperiode.value, __etterbetalingsperiode.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}inntektPaaNorskKontinentalsokkel uses Python identifier inntektPaaNorskKontinentalsokkel
    __inntektPaaNorskKontinentalsokkel = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "inntektPaaNorskKontinentalsokkel"),
        "inntektPaaNorskKontinentalsokkel",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_1inntektPaaNorskKontinentalsokkel",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 212, 3
        ),
    )

    inntektPaaNorskKontinentalsokkel = property(
        __inntektPaaNorskKontinentalsokkel.value,
        __inntektPaaNorskKontinentalsokkel.set,
        None,
        None,
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}inntjeningsforhold uses Python identifier inntjeningsforhold
    __inntjeningsforhold = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "inntjeningsforhold"),
        "inntjeningsforhold",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_1inntjeningsforhold",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 213, 3
        ),
    )

    inntjeningsforhold = property(
        __inntjeningsforhold.value, __inntjeningsforhold.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}livrente uses Python identifier livrente
    __livrente = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "livrente"),
        "livrente",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_1livrente",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 214, 3
        ),
    )

    livrente = property(__livrente.value, __livrente.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}lottOgPart uses Python identifier lottOgPart
    __lottOgPart = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "lottOgPart"),
        "lottOgPart",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_1lottOgPart",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 215, 3
        ),
    )

    lottOgPart = property(__lottOgPart.value, __lottOgPart.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}nettoloenn uses Python identifier nettoloenn
    __nettoloenn = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "nettoloenn"),
        "nettoloenn",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_1nettoloenn",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 216, 3
        ),
    )

    nettoloenn = property(__nettoloenn.value, __nettoloenn.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}pensjon uses Python identifier pensjon
    __pensjon = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "pensjon"),
        "pensjon",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_1pensjon",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 217, 3
        ),
    )

    pensjon = property(__pensjon.value, __pensjon.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}reiseKostOgLosji uses Python identifier reiseKostOgLosji
    __reiseKostOgLosji = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "reiseKostOgLosji"),
        "reiseKostOgLosji",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_1reiseKostOgLosji",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 218, 3
        ),
    )

    reiseKostOgLosji = property(
        __reiseKostOgLosji.value, __reiseKostOgLosji.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}utenlandskArtist uses Python identifier utenlandskArtist
    __utenlandskArtist = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "utenlandskArtist"),
        "utenlandskArtist",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_1utenlandskArtist",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 219, 3
        ),
    )

    utenlandskArtist = property(
        __utenlandskArtist.value, __utenlandskArtist.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}bonusFraForsvaret uses Python identifier bonusFraForsvaret
    __bonusFraForsvaret = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "bonusFraForsvaret"),
        "bonusFraForsvaret",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Tilleggsinformasjon_urnskefastsettinginnsamlinga_meldingenv2_1bonusFraForsvaret",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 220, 3
        ),
    )

    bonusFraForsvaret = property(
        __bonusFraForsvaret.value, __bonusFraForsvaret.set, None, None
    )

    _ElementMap.update(
        {
            __bilOgBaat.name(): __bilOgBaat,
            __dagmammaIEgenBolig.name(): __dagmammaIEgenBolig,
            __etterbetalingsperiode.name(): __etterbetalingsperiode,
            __inntektPaaNorskKontinentalsokkel.name(): __inntektPaaNorskKontinentalsokkel,
            __inntjeningsforhold.name(): __inntjeningsforhold,
            __livrente.name(): __livrente,
            __lottOgPart.name(): __lottOgPart,
            __nettoloenn.name(): __nettoloenn,
            __pensjon.name(): __pensjon,
            __reiseKostOgLosji.name(): __reiseKostOgLosji,
            __utenlandskArtist.name(): __utenlandskArtist,
            __bonusFraForsvaret.name(): __bonusFraForsvaret,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Tilleggsinformasjon = Tilleggsinformasjon
Namespace.addCategoryObject("typeBinding", "Tilleggsinformasjon", Tilleggsinformasjon)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Periode with content type ELEMENT_ONLY
class Periode(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Periode with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Periode")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 223, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}startdato uses Python identifier startdato
    __startdato = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "startdato"),
        "startdato",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Periode_urnskefastsettinginnsamlinga_meldingenv2_1startdato",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 225, 3
        ),
    )

    startdato = property(__startdato.value, __startdato.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}sluttdato uses Python identifier sluttdato
    __sluttdato = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "sluttdato"),
        "sluttdato",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Periode_urnskefastsettinginnsamlinga_meldingenv2_1sluttdato",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 226, 3
        ),
    )

    sluttdato = property(__sluttdato.value, __sluttdato.set, None, None)

    _ElementMap.update(
        {__startdato.name(): __startdato, __sluttdato.name(): __sluttdato}
    )
    _AttributeMap.update({})


_module_typeBindings.Periode = Periode
Namespace.addCategoryObject("typeBinding", "Periode", Periode)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}BilOgBaat with content type ELEMENT_ONLY
class BilOgBaat(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}BilOgBaat with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "BilOgBaat")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 229, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}antallKilometer uses Python identifier antallKilometer
    __antallKilometer = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "antallKilometer"),
        "antallKilometer",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_BilOgBaat_urnskefastsettinginnsamlinga_meldingenv2_1antallKilometer",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 231, 3
        ),
    )

    antallKilometer = property(
        __antallKilometer.value, __antallKilometer.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}antallReiser uses Python identifier antallReiser
    __antallReiser = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "antallReiser"),
        "antallReiser",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_BilOgBaat_urnskefastsettinginnsamlinga_meldingenv2_1antallReiser",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 232, 3
        ),
    )

    antallReiser = property(__antallReiser.value, __antallReiser.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}heravAntallKilometerMellomHjemOgArbeid uses Python identifier heravAntallKilometerMellomHjemOgArbeid
    __heravAntallKilometerMellomHjemOgArbeid = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(
            Namespace, "heravAntallKilometerMellomHjemOgArbeid"
        ),
        "heravAntallKilometerMellomHjemOgArbeid",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_BilOgBaat_urnskefastsettinginnsamlinga_meldingenv2_1heravAntallKilometerMellomHjemOgArbeid",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 233, 3
        ),
    )

    heravAntallKilometerMellomHjemOgArbeid = property(
        __heravAntallKilometerMellomHjemOgArbeid.value,
        __heravAntallKilometerMellomHjemOgArbeid.set,
        None,
        None,
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}listeprisForBil uses Python identifier listeprisForBil
    __listeprisForBil = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "listeprisForBil"),
        "listeprisForBil",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_BilOgBaat_urnskefastsettinginnsamlinga_meldingenv2_1listeprisForBil",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 234, 3
        ),
    )

    listeprisForBil = property(
        __listeprisForBil.value, __listeprisForBil.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}bilregistreringsnummer uses Python identifier bilregistreringsnummer
    __bilregistreringsnummer = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "bilregistreringsnummer"),
        "bilregistreringsnummer",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_BilOgBaat_urnskefastsettinginnsamlinga_meldingenv2_1bilregistreringsnummer",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 235, 3
        ),
    )

    bilregistreringsnummer = property(
        __bilregistreringsnummer.value, __bilregistreringsnummer.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}erBilpool uses Python identifier erBilpool
    __erBilpool = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "erBilpool"),
        "erBilpool",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_BilOgBaat_urnskefastsettinginnsamlinga_meldingenv2_1erBilpool",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 236, 3
        ),
    )

    erBilpool = property(__erBilpool.value, __erBilpool.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}erAnnenBil uses Python identifier erAnnenBil
    __erAnnenBil = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "erAnnenBil"),
        "erAnnenBil",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_BilOgBaat_urnskefastsettinginnsamlinga_meldingenv2_1erAnnenBil",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 237, 3
        ),
    )

    erAnnenBil = property(__erAnnenBil.value, __erAnnenBil.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}erBilUtenforStandardregelen uses Python identifier erBilUtenforStandardregelen
    __erBilUtenforStandardregelen = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "erBilUtenforStandardregelen"),
        "erBilUtenforStandardregelen",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_BilOgBaat_urnskefastsettinginnsamlinga_meldingenv2_1erBilUtenforStandardregelen",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 238, 3
        ),
    )

    erBilUtenforStandardregelen = property(
        __erBilUtenforStandardregelen.value,
        __erBilUtenforStandardregelen.set,
        None,
        None,
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}personklassifiseringAvBilbruker uses Python identifier personklassifiseringAvBilbruker
    __personklassifiseringAvBilbruker = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "personklassifiseringAvBilbruker"),
        "personklassifiseringAvBilbruker",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_BilOgBaat_urnskefastsettinginnsamlinga_meldingenv2_1personklassifiseringAvBilbruker",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 239, 3
        ),
    )

    personklassifiseringAvBilbruker = property(
        __personklassifiseringAvBilbruker.value,
        __personklassifiseringAvBilbruker.set,
        None,
        None,
    )

    _ElementMap.update(
        {
            __antallKilometer.name(): __antallKilometer,
            __antallReiser.name(): __antallReiser,
            __heravAntallKilometerMellomHjemOgArbeid.name(): __heravAntallKilometerMellomHjemOgArbeid,
            __listeprisForBil.name(): __listeprisForBil,
            __bilregistreringsnummer.name(): __bilregistreringsnummer,
            __erBilpool.name(): __erBilpool,
            __erAnnenBil.name(): __erAnnenBil,
            __erBilUtenforStandardregelen.name(): __erBilUtenforStandardregelen,
            __personklassifiseringAvBilbruker.name(): __personklassifiseringAvBilbruker,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.BilOgBaat = BilOgBaat
Namespace.addCategoryObject("typeBinding", "BilOgBaat", BilOgBaat)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}DagmammaIEgenBolig with content type ELEMENT_ONLY
class DagmammaIEgenBolig(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}DagmammaIEgenBolig with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "DagmammaIEgenBolig")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 245, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}antallBarn uses Python identifier antallBarn
    __antallBarn = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "antallBarn"),
        "antallBarn",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_DagmammaIEgenBolig_urnskefastsettinginnsamlinga_meldingenv2_1antallBarn",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 247, 3
        ),
    )

    antallBarn = property(__antallBarn.value, __antallBarn.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}antallMaaneder uses Python identifier antallMaaneder
    __antallMaaneder = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "antallMaaneder"),
        "antallMaaneder",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_DagmammaIEgenBolig_urnskefastsettinginnsamlinga_meldingenv2_1antallMaaneder",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 248, 3
        ),
    )

    antallMaaneder = property(__antallMaaneder.value, __antallMaaneder.set, None, None)

    _ElementMap.update(
        {__antallBarn.name(): __antallBarn, __antallMaaneder.name(): __antallMaaneder}
    )
    _AttributeMap.update({})


_module_typeBindings.DagmammaIEgenBolig = DagmammaIEgenBolig
Namespace.addCategoryObject("typeBinding", "DagmammaIEgenBolig", DagmammaIEgenBolig)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}NorskKontinentalsokkel with content type ELEMENT_ONLY
class NorskKontinentalsokkel(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}NorskKontinentalsokkel with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "NorskKontinentalsokkel")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 251, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}tidsrom uses Python identifier tidsrom
    __tidsrom = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "tidsrom"),
        "tidsrom",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_NorskKontinentalsokkel_urnskefastsettinginnsamlinga_meldingenv2_1tidsrom",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 253, 3
        ),
    )

    tidsrom = property(__tidsrom.value, __tidsrom.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}gjelderLoennFoerste60Dager uses Python identifier gjelderLoennFoerste60Dager
    __gjelderLoennFoerste60Dager = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "gjelderLoennFoerste60Dager"),
        "gjelderLoennFoerste60Dager",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_NorskKontinentalsokkel_urnskefastsettinginnsamlinga_meldingenv2_1gjelderLoennFoerste60Dager",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 254, 3
        ),
    )

    gjelderLoennFoerste60Dager = property(
        __gjelderLoennFoerste60Dager.value, __gjelderLoennFoerste60Dager.set, None, None
    )

    _ElementMap.update(
        {
            __tidsrom.name(): __tidsrom,
            __gjelderLoennFoerste60Dager.name(): __gjelderLoennFoerste60Dager,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.NorskKontinentalsokkel = NorskKontinentalsokkel
Namespace.addCategoryObject(
    "typeBinding", "NorskKontinentalsokkel", NorskKontinentalsokkel
)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Livrente with content type ELEMENT_ONLY
class Livrente(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Livrente with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Livrente")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 260, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}totaltUtbetaltBeloep uses Python identifier totaltUtbetaltBeloep
    __totaltUtbetaltBeloep = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "totaltUtbetaltBeloep"),
        "totaltUtbetaltBeloep",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Livrente_urnskefastsettinginnsamlinga_meldingenv2_1totaltUtbetaltBeloep",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 262, 3
        ),
    )

    totaltUtbetaltBeloep = property(
        __totaltUtbetaltBeloep.value, __totaltUtbetaltBeloep.set, None, None
    )

    _ElementMap.update({__totaltUtbetaltBeloep.name(): __totaltUtbetaltBeloep})
    _AttributeMap.update({})


_module_typeBindings.Livrente = Livrente
Namespace.addCategoryObject("typeBinding", "Livrente", Livrente)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}LottOgPartInnenFiske with content type ELEMENT_ONLY
class LottOgPartInnenFiske(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}LottOgPartInnenFiske with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "LottOgPartInnenFiske")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 265, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}antallDager uses Python identifier antallDager
    __antallDager = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "antallDager"),
        "antallDager",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_LottOgPartInnenFiske_urnskefastsettinginnsamlinga_meldingenv2_1antallDager",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 267, 3
        ),
    )

    antallDager = property(__antallDager.value, __antallDager.set, None, None)

    _ElementMap.update({__antallDager.name(): __antallDager})
    _AttributeMap.update({})


_module_typeBindings.LottOgPartInnenFiske = LottOgPartInnenFiske
Namespace.addCategoryObject("typeBinding", "LottOgPartInnenFiske", LottOgPartInnenFiske)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Nettoloennsordning with content type ELEMENT_ONLY
class Nettoloennsordning(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Nettoloennsordning with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Nettoloennsordning")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 270, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}oppgrossingstabellnummer uses Python identifier oppgrossingstabellnummer
    __oppgrossingstabellnummer = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "oppgrossingstabellnummer"),
        "oppgrossingstabellnummer",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Nettoloennsordning_urnskefastsettinginnsamlinga_meldingenv2_1oppgrossingstabellnummer",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 272, 3
        ),
    )

    oppgrossingstabellnummer = property(
        __oppgrossingstabellnummer.value, __oppgrossingstabellnummer.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}bilinformasjon uses Python identifier bilinformasjon
    __bilinformasjon = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "bilinformasjon"),
        "bilinformasjon",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Nettoloennsordning_urnskefastsettinginnsamlinga_meldingenv2_1bilinformasjon",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 273, 3
        ),
    )

    bilinformasjon = property(__bilinformasjon.value, __bilinformasjon.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}betaltSkattebeloepIUtlandet uses Python identifier betaltSkattebeloepIUtlandet
    __betaltSkattebeloepIUtlandet = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "betaltSkattebeloepIUtlandet"),
        "betaltSkattebeloepIUtlandet",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Nettoloennsordning_urnskefastsettinginnsamlinga_meldingenv2_1betaltSkattebeloepIUtlandet",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 274, 3
        ),
    )

    betaltSkattebeloepIUtlandet = property(
        __betaltSkattebeloepIUtlandet.value,
        __betaltSkattebeloepIUtlandet.set,
        None,
        None,
    )

    _ElementMap.update(
        {
            __oppgrossingstabellnummer.name(): __oppgrossingstabellnummer,
            __bilinformasjon.name(): __bilinformasjon,
            __betaltSkattebeloepIUtlandet.name(): __betaltSkattebeloepIUtlandet,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Nettoloennsordning = Nettoloennsordning
Namespace.addCategoryObject("typeBinding", "Nettoloennsordning", Nettoloennsordning)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}AldersUfoereEtterlatteAvtalefestetOgKrigspensjon with content type ELEMENT_ONLY
class AldersUfoereEtterlatteAvtalefestetOgKrigspensjon(
    pyxb.binding.basis.complexTypeDefinition
):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}AldersUfoereEtterlatteAvtalefestetOgKrigspensjon with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(
        Namespace, "AldersUfoereEtterlatteAvtalefestetOgKrigspensjon"
    )
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 277, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}grunnpensjonsbeloep uses Python identifier grunnpensjonsbeloep
    __grunnpensjonsbeloep = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "grunnpensjonsbeloep"),
        "grunnpensjonsbeloep",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_AldersUfoereEtterlatteAvtalefestetOgKrigspensjon_urnskefastsettinginnsamlinga_meldingenv2_1grunnpensjonsbeloep",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 279, 3
        ),
    )

    grunnpensjonsbeloep = property(
        __grunnpensjonsbeloep.value, __grunnpensjonsbeloep.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}tilleggspensjonsbeloep uses Python identifier tilleggspensjonsbeloep
    __tilleggspensjonsbeloep = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "tilleggspensjonsbeloep"),
        "tilleggspensjonsbeloep",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_AldersUfoereEtterlatteAvtalefestetOgKrigspensjon_urnskefastsettinginnsamlinga_meldingenv2_1tilleggspensjonsbeloep",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 280, 3
        ),
    )

    tilleggspensjonsbeloep = property(
        __tilleggspensjonsbeloep.value, __tilleggspensjonsbeloep.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}ufoeregrad uses Python identifier ufoeregrad
    __ufoeregrad = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ufoeregrad"),
        "ufoeregrad",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_AldersUfoereEtterlatteAvtalefestetOgKrigspensjon_urnskefastsettinginnsamlinga_meldingenv2_1ufoeregrad",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 281, 3
        ),
    )

    ufoeregrad = property(__ufoeregrad.value, __ufoeregrad.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}pensjonsgrad uses Python identifier pensjonsgrad
    __pensjonsgrad = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "pensjonsgrad"),
        "pensjonsgrad",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_AldersUfoereEtterlatteAvtalefestetOgKrigspensjon_urnskefastsettinginnsamlinga_meldingenv2_1pensjonsgrad",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 282, 3
        ),
    )

    pensjonsgrad = property(__pensjonsgrad.value, __pensjonsgrad.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}heravEtterlattepensjon uses Python identifier heravEtterlattepensjon
    __heravEtterlattepensjon = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "heravEtterlattepensjon"),
        "heravEtterlattepensjon",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_AldersUfoereEtterlatteAvtalefestetOgKrigspensjon_urnskefastsettinginnsamlinga_meldingenv2_1heravEtterlattepensjon",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 283, 3
        ),
    )

    heravEtterlattepensjon = property(
        __heravEtterlattepensjon.value, __heravEtterlattepensjon.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}tidsrom uses Python identifier tidsrom
    __tidsrom = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "tidsrom"),
        "tidsrom",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_AldersUfoereEtterlatteAvtalefestetOgKrigspensjon_urnskefastsettinginnsamlinga_meldingenv2_1tidsrom",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 284, 3
        ),
    )

    tidsrom = property(__tidsrom.value, __tidsrom.set, None, None)

    _ElementMap.update(
        {
            __grunnpensjonsbeloep.name(): __grunnpensjonsbeloep,
            __tilleggspensjonsbeloep.name(): __tilleggspensjonsbeloep,
            __ufoeregrad.name(): __ufoeregrad,
            __pensjonsgrad.name(): __pensjonsgrad,
            __heravEtterlattepensjon.name(): __heravEtterlattepensjon,
            __tidsrom.name(): __tidsrom,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.AldersUfoereEtterlatteAvtalefestetOgKrigspensjon = (
    AldersUfoereEtterlatteAvtalefestetOgKrigspensjon
)
Namespace.addCategoryObject(
    "typeBinding",
    "AldersUfoereEtterlatteAvtalefestetOgKrigspensjon",
    AldersUfoereEtterlatteAvtalefestetOgKrigspensjon,
)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}ReiseKostOgLosji with content type ELEMENT_ONLY
class ReiseKostOgLosji(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}ReiseKostOgLosji with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "ReiseKostOgLosji")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 287, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}persontype uses Python identifier persontype
    __persontype = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "persontype"),
        "persontype",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_ReiseKostOgLosji_urnskefastsettinginnsamlinga_meldingenv2_1persontype",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 289, 3
        ),
    )

    persontype = property(__persontype.value, __persontype.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}antallReiser uses Python identifier antallReiser
    __antallReiser = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "antallReiser"),
        "antallReiser",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_ReiseKostOgLosji_urnskefastsettinginnsamlinga_meldingenv2_1antallReiser",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 290, 3
        ),
    )

    antallReiser = property(__antallReiser.value, __antallReiser.set, None, None)

    _ElementMap.update(
        {__persontype.name(): __persontype, __antallReiser.name(): __antallReiser}
    )
    _AttributeMap.update({})


_module_typeBindings.ReiseKostOgLosji = ReiseKostOgLosji
Namespace.addCategoryObject("typeBinding", "ReiseKostOgLosji", ReiseKostOgLosji)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}UtenlandskArtist with content type ELEMENT_ONLY
class UtenlandskArtist(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}UtenlandskArtist with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "UtenlandskArtist")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 293, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}inntektsaar uses Python identifier inntektsaar
    __inntektsaar = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "inntektsaar"),
        "inntektsaar",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_UtenlandskArtist_urnskefastsettinginnsamlinga_meldingenv2_1inntektsaar",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 295, 3
        ),
    )

    inntektsaar = property(__inntektsaar.value, __inntektsaar.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}oppgrossingsgrunnlag uses Python identifier oppgrossingsgrunnlag
    __oppgrossingsgrunnlag = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "oppgrossingsgrunnlag"),
        "oppgrossingsgrunnlag",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_UtenlandskArtist_urnskefastsettinginnsamlinga_meldingenv2_1oppgrossingsgrunnlag",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 296, 3
        ),
    )

    oppgrossingsgrunnlag = property(
        __oppgrossingsgrunnlag.value, __oppgrossingsgrunnlag.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}trukketArtistskatt uses Python identifier trukketArtistskatt
    __trukketArtistskatt = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "trukketArtistskatt"),
        "trukketArtistskatt",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_UtenlandskArtist_urnskefastsettinginnsamlinga_meldingenv2_1trukketArtistskatt",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 297, 3
        ),
    )

    trukketArtistskatt = property(
        __trukketArtistskatt.value, __trukketArtistskatt.set, None, None
    )

    _ElementMap.update(
        {
            __inntektsaar.name(): __inntektsaar,
            __oppgrossingsgrunnlag.name(): __oppgrossingsgrunnlag,
            __trukketArtistskatt.name(): __trukketArtistskatt,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.UtenlandskArtist = UtenlandskArtist
Namespace.addCategoryObject("typeBinding", "UtenlandskArtist", UtenlandskArtist)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}BonusFraForsvaret with content type ELEMENT_ONLY
class BonusFraForsvaret(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}BonusFraForsvaret with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "BonusFraForsvaret")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 300, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}aaretUtbetalingenGjelderFor uses Python identifier aaretUtbetalingenGjelderFor
    __aaretUtbetalingenGjelderFor = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "aaretUtbetalingenGjelderFor"),
        "aaretUtbetalingenGjelderFor",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_BonusFraForsvaret_urnskefastsettinginnsamlinga_meldingenv2_1aaretUtbetalingenGjelderFor",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 302, 3
        ),
    )

    aaretUtbetalingenGjelderFor = property(
        __aaretUtbetalingenGjelderFor.value,
        __aaretUtbetalingenGjelderFor.set,
        None,
        None,
    )

    _ElementMap.update(
        {__aaretUtbetalingenGjelderFor.name(): __aaretUtbetalingenGjelderFor}
    )
    _AttributeMap.update({})


_module_typeBindings.BonusFraForsvaret = BonusFraForsvaret
Namespace.addCategoryObject("typeBinding", "BonusFraForsvaret", BonusFraForsvaret)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Spesifikasjon with content type ELEMENT_ONLY
class Spesifikasjon(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Spesifikasjon with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Spesifikasjon")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 305, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}skattemessigBosattILand uses Python identifier skattemessigBosattILand
    __skattemessigBosattILand = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "skattemessigBosattILand"),
        "skattemessigBosattILand",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Spesifikasjon_urnskefastsettinginnsamlinga_meldingenv2_1skattemessigBosattILand",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 307, 3
        ),
    )

    skattemessigBosattILand = property(
        __skattemessigBosattILand.value, __skattemessigBosattILand.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}opptjeningsland uses Python identifier opptjeningsland
    __opptjeningsland = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "opptjeningsland"),
        "opptjeningsland",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Spesifikasjon_urnskefastsettinginnsamlinga_meldingenv2_1opptjeningsland",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 308, 3
        ),
    )

    opptjeningsland = property(
        __opptjeningsland.value, __opptjeningsland.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}erOpptjentPaaHjelpefartoey uses Python identifier erOpptjentPaaHjelpefartoey
    __erOpptjentPaaHjelpefartoey = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "erOpptjentPaaHjelpefartoey"),
        "erOpptjentPaaHjelpefartoey",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Spesifikasjon_urnskefastsettinginnsamlinga_meldingenv2_1erOpptjentPaaHjelpefartoey",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 309, 3
        ),
    )

    erOpptjentPaaHjelpefartoey = property(
        __erOpptjentPaaHjelpefartoey.value, __erOpptjentPaaHjelpefartoey.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}erOpptjentPaaKontinentalsokkel uses Python identifier erOpptjentPaaKontinentalsokkel
    __erOpptjentPaaKontinentalsokkel = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "erOpptjentPaaKontinentalsokkel"),
        "erOpptjentPaaKontinentalsokkel",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Spesifikasjon_urnskefastsettinginnsamlinga_meldingenv2_1erOpptjentPaaKontinentalsokkel",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 310, 3
        ),
    )

    erOpptjentPaaKontinentalsokkel = property(
        __erOpptjentPaaKontinentalsokkel.value,
        __erOpptjentPaaKontinentalsokkel.set,
        None,
        None,
    )

    _ElementMap.update(
        {
            __skattemessigBosattILand.name(): __skattemessigBosattILand,
            __opptjeningsland.name(): __opptjeningsland,
            __erOpptjentPaaHjelpefartoey.name(): __erOpptjentPaaHjelpefartoey,
            __erOpptjentPaaKontinentalsokkel.name(): __erOpptjentPaaKontinentalsokkel,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Spesifikasjon = Spesifikasjon
Namespace.addCategoryObject("typeBinding", "Spesifikasjon", Spesifikasjon)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}YtelseFraOffentlige with content type ELEMENT_ONLY
class YtelseFraOffentlige(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}YtelseFraOffentlige with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "YtelseFraOffentlige")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 313, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "beskrivelse"),
        "beskrivelse",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_YtelseFraOffentlige_urnskefastsettinginnsamlinga_meldingenv2_1beskrivelse",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 315, 3
        ),
    )

    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}tilleggsinformasjon uses Python identifier tilleggsinformasjon
    __tilleggsinformasjon = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "tilleggsinformasjon"),
        "tilleggsinformasjon",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_YtelseFraOffentlige_urnskefastsettinginnsamlinga_meldingenv2_1tilleggsinformasjon",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 316, 3
        ),
    )

    tilleggsinformasjon = property(
        __tilleggsinformasjon.value, __tilleggsinformasjon.set, None, None
    )

    _ElementMap.update(
        {
            __beskrivelse.name(): __beskrivelse,
            __tilleggsinformasjon.name(): __tilleggsinformasjon,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.YtelseFraOffentlige = YtelseFraOffentlige
Namespace.addCategoryObject("typeBinding", "YtelseFraOffentlige", YtelseFraOffentlige)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}PensjonEllerTrygd with content type ELEMENT_ONLY
class PensjonEllerTrygd(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}PensjonEllerTrygd with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "PensjonEllerTrygd")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 322, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "beskrivelse"),
        "beskrivelse",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_PensjonEllerTrygd_urnskefastsettinginnsamlinga_meldingenv2_1beskrivelse",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 324, 3
        ),
    )

    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}tilleggsinformasjon uses Python identifier tilleggsinformasjon
    __tilleggsinformasjon = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "tilleggsinformasjon"),
        "tilleggsinformasjon",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_PensjonEllerTrygd_urnskefastsettinginnsamlinga_meldingenv2_1tilleggsinformasjon",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 325, 3
        ),
    )

    tilleggsinformasjon = property(
        __tilleggsinformasjon.value, __tilleggsinformasjon.set, None, None
    )

    _ElementMap.update(
        {
            __beskrivelse.name(): __beskrivelse,
            __tilleggsinformasjon.name(): __tilleggsinformasjon,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.PensjonEllerTrygd = PensjonEllerTrygd
Namespace.addCategoryObject("typeBinding", "PensjonEllerTrygd", PensjonEllerTrygd)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Naeringsinntekt with content type ELEMENT_ONLY
class Naeringsinntekt(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Naeringsinntekt with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Naeringsinntekt")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 331, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "beskrivelse"),
        "beskrivelse",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Naeringsinntekt_urnskefastsettinginnsamlinga_meldingenv2_1beskrivelse",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 333, 3
        ),
    )

    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}tilleggsinformasjon uses Python identifier tilleggsinformasjon
    __tilleggsinformasjon = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "tilleggsinformasjon"),
        "tilleggsinformasjon",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Naeringsinntekt_urnskefastsettinginnsamlinga_meldingenv2_1tilleggsinformasjon",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 334, 3
        ),
    )

    tilleggsinformasjon = property(
        __tilleggsinformasjon.value, __tilleggsinformasjon.set, None, None
    )

    _ElementMap.update(
        {
            __beskrivelse.name(): __beskrivelse,
            __tilleggsinformasjon.name(): __tilleggsinformasjon,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Naeringsinntekt = Naeringsinntekt
Namespace.addCategoryObject("typeBinding", "Naeringsinntekt", Naeringsinntekt)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}SjoefolksrelatertInformasjon with content type ELEMENT_ONLY
class SjoefolksrelatertInformasjon(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}SjoefolksrelatertInformasjon with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(
        Namespace, "SjoefolksrelatertInformasjon"
    )
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 343, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}antallDoegnOmbord uses Python identifier antallDoegnOmbord
    __antallDoegnOmbord = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "antallDoegnOmbord"),
        "antallDoegnOmbord",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_SjoefolksrelatertInformasjon_urnskefastsettinginnsamlinga_meldingenv2_1antallDoegnOmbord",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 345, 3
        ),
    )

    antallDoegnOmbord = property(
        __antallDoegnOmbord.value, __antallDoegnOmbord.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}antallDoegnOmbordUtenDekkedeSmaautgifter uses Python identifier antallDoegnOmbordUtenDekkedeSmaautgifter
    __antallDoegnOmbordUtenDekkedeSmaautgifter = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(
            Namespace, "antallDoegnOmbordUtenDekkedeSmaautgifter"
        ),
        "antallDoegnOmbordUtenDekkedeSmaautgifter",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_SjoefolksrelatertInformasjon_urnskefastsettinginnsamlinga_meldingenv2_1antallDoegnOmbordUtenDekkedeSmaautgifter",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 346, 3
        ),
    )

    antallDoegnOmbordUtenDekkedeSmaautgifter = property(
        __antallDoegnOmbordUtenDekkedeSmaautgifter.value,
        __antallDoegnOmbordUtenDekkedeSmaautgifter.set,
        None,
        None,
    )

    _ElementMap.update(
        {
            __antallDoegnOmbord.name(): __antallDoegnOmbord,
            __antallDoegnOmbordUtenDekkedeSmaautgifter.name(): __antallDoegnOmbordUtenDekkedeSmaautgifter,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.SjoefolksrelatertInformasjon = SjoefolksrelatertInformasjon
Namespace.addCategoryObject(
    "typeBinding", "SjoefolksrelatertInformasjon", SjoefolksrelatertInformasjon
)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}OppholdPaaSvalbardJanMayenOgBilandene with content type ELEMENT_ONLY
class OppholdPaaSvalbardJanMayenOgBilandene(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}OppholdPaaSvalbardJanMayenOgBilandene with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(
        Namespace, "OppholdPaaSvalbardJanMayenOgBilandene"
    )
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 349, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}oppholdsId uses Python identifier oppholdsId
    __oppholdsId = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "oppholdsId"),
        "oppholdsId",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_OppholdPaaSvalbardJanMayenOgBilandene_urnskefastsettinginnsamlinga_meldingenv2_1oppholdsId",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 351, 3
        ),
    )

    oppholdsId = property(__oppholdsId.value, __oppholdsId.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}startdato uses Python identifier startdato
    __startdato = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "startdato"),
        "startdato",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_OppholdPaaSvalbardJanMayenOgBilandene_urnskefastsettinginnsamlinga_meldingenv2_1startdato",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 352, 3
        ),
    )

    startdato = property(__startdato.value, __startdato.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}sluttdato uses Python identifier sluttdato
    __sluttdato = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "sluttdato"),
        "sluttdato",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_OppholdPaaSvalbardJanMayenOgBilandene_urnskefastsettinginnsamlinga_meldingenv2_1sluttdato",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 353, 3
        ),
    )

    sluttdato = property(__sluttdato.value, __sluttdato.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "beskrivelse"),
        "beskrivelse",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_OppholdPaaSvalbardJanMayenOgBilandene_urnskefastsettinginnsamlinga_meldingenv2_1beskrivelse",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 354, 3
        ),
    )

    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    _ElementMap.update(
        {
            __oppholdsId.name(): __oppholdsId,
            __startdato.name(): __startdato,
            __sluttdato.name(): __sluttdato,
            __beskrivelse.name(): __beskrivelse,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.OppholdPaaSvalbardJanMayenOgBilandene = (
    OppholdPaaSvalbardJanMayenOgBilandene
)
Namespace.addCategoryObject(
    "typeBinding",
    "OppholdPaaSvalbardJanMayenOgBilandene",
    OppholdPaaSvalbardJanMayenOgBilandene,
)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Arbeidsgiveravgift with content type ELEMENT_ONLY
class Arbeidsgiveravgift(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Arbeidsgiveravgift with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Arbeidsgiveravgift")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 357, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}loennOgGodtgjoerelse uses Python identifier loennOgGodtgjoerelse
    __loennOgGodtgjoerelse = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "loennOgGodtgjoerelse"),
        "loennOgGodtgjoerelse",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsgiveravgift_urnskefastsettinginnsamlinga_meldingenv2_1loennOgGodtgjoerelse",
        True,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 359, 3
        ),
    )

    loennOgGodtgjoerelse = property(
        __loennOgGodtgjoerelse.value, __loennOgGodtgjoerelse.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}tilskuddOgPremieTilPensjon uses Python identifier tilskuddOgPremieTilPensjon
    __tilskuddOgPremieTilPensjon = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "tilskuddOgPremieTilPensjon"),
        "tilskuddOgPremieTilPensjon",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsgiveravgift_urnskefastsettinginnsamlinga_meldingenv2_1tilskuddOgPremieTilPensjon",
        True,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 360, 3
        ),
    )

    tilskuddOgPremieTilPensjon = property(
        __tilskuddOgPremieTilPensjon.value, __tilskuddOgPremieTilPensjon.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}utenlandskeMedSaerskiltProsentsats uses Python identifier utenlandskeMedSaerskiltProsentsats
    __utenlandskeMedSaerskiltProsentsats = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "utenlandskeMedSaerskiltProsentsats"),
        "utenlandskeMedSaerskiltProsentsats",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsgiveravgift_urnskefastsettinginnsamlinga_meldingenv2_1utenlandskeMedSaerskiltProsentsats",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 361, 3
        ),
    )

    utenlandskeMedSaerskiltProsentsats = property(
        __utenlandskeMedSaerskiltProsentsats.value,
        __utenlandskeMedSaerskiltProsentsats.set,
        None,
        None,
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}utenlandskeMedFastAvgiftsbeloep uses Python identifier utenlandskeMedFastAvgiftsbeloep
    __utenlandskeMedFastAvgiftsbeloep = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "utenlandskeMedFastAvgiftsbeloep"),
        "utenlandskeMedFastAvgiftsbeloep",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsgiveravgift_urnskefastsettinginnsamlinga_meldingenv2_1utenlandskeMedFastAvgiftsbeloep",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 362, 3
        ),
    )

    utenlandskeMedFastAvgiftsbeloep = property(
        __utenlandskeMedFastAvgiftsbeloep.value,
        __utenlandskeMedFastAvgiftsbeloep.set,
        None,
        None,
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}fradragIGrunnlagetForSone uses Python identifier fradragIGrunnlagetForSone
    __fradragIGrunnlagetForSone = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "fradragIGrunnlagetForSone"),
        "fradragIGrunnlagetForSone",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsgiveravgift_urnskefastsettinginnsamlinga_meldingenv2_1fradragIGrunnlagetForSone",
        True,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 363, 3
        ),
    )

    fradragIGrunnlagetForSone = property(
        __fradragIGrunnlagetForSone.value, __fradragIGrunnlagetForSone.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}fradragIGrunnlagetForUtenlandsk uses Python identifier fradragIGrunnlagetForUtenlandsk
    __fradragIGrunnlagetForUtenlandsk = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "fradragIGrunnlagetForUtenlandsk"),
        "fradragIGrunnlagetForUtenlandsk",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsgiveravgift_urnskefastsettinginnsamlinga_meldingenv2_1fradragIGrunnlagetForUtenlandsk",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 364, 3
        ),
    )

    fradragIGrunnlagetForUtenlandsk = property(
        __fradragIGrunnlagetForUtenlandsk.value,
        __fradragIGrunnlagetForUtenlandsk.set,
        None,
        None,
    )

    _ElementMap.update(
        {
            __loennOgGodtgjoerelse.name(): __loennOgGodtgjoerelse,
            __tilskuddOgPremieTilPensjon.name(): __tilskuddOgPremieTilPensjon,
            __utenlandskeMedSaerskiltProsentsats.name(): __utenlandskeMedSaerskiltProsentsats,
            __utenlandskeMedFastAvgiftsbeloep.name(): __utenlandskeMedFastAvgiftsbeloep,
            __fradragIGrunnlagetForSone.name(): __fradragIGrunnlagetForSone,
            __fradragIGrunnlagetForUtenlandsk.name(): __fradragIGrunnlagetForUtenlandsk,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Arbeidsgiveravgift = Arbeidsgiveravgift
Namespace.addCategoryObject("typeBinding", "Arbeidsgiveravgift", Arbeidsgiveravgift)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Arbeidsgiveravgiftsgrunnlag with content type ELEMENT_ONLY
class Arbeidsgiveravgiftsgrunnlag(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}Arbeidsgiveravgiftsgrunnlag with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(
        Namespace, "Arbeidsgiveravgiftsgrunnlag"
    )
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 367, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}beregningskodeForArbeidsgiveravgift uses Python identifier beregningskodeForArbeidsgiveravgift
    __beregningskodeForArbeidsgiveravgift = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "beregningskodeForArbeidsgiveravgift"),
        "beregningskodeForArbeidsgiveravgift",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsgiveravgiftsgrunnlag_urnskefastsettinginnsamlinga_meldingenv2_1beregningskodeForArbeidsgiveravgift",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 369, 3
        ),
    )

    beregningskodeForArbeidsgiveravgift = property(
        __beregningskodeForArbeidsgiveravgift.value,
        __beregningskodeForArbeidsgiveravgift.set,
        None,
        None,
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}sone uses Python identifier sone
    __sone = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "sone"),
        "sone",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsgiveravgiftsgrunnlag_urnskefastsettinginnsamlinga_meldingenv2_1sone",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 370, 3
        ),
    )

    sone = property(__sone.value, __sone.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}avgiftsgrunnlagBeloep uses Python identifier avgiftsgrunnlagBeloep
    __avgiftsgrunnlagBeloep = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "avgiftsgrunnlagBeloep"),
        "avgiftsgrunnlagBeloep",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsgiveravgiftsgrunnlag_urnskefastsettinginnsamlinga_meldingenv2_1avgiftsgrunnlagBeloep",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 371, 3
        ),
    )

    avgiftsgrunnlagBeloep = property(
        __avgiftsgrunnlagBeloep.value, __avgiftsgrunnlagBeloep.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}prosentsatsForAvgiftsberegning uses Python identifier prosentsatsForAvgiftsberegning
    __prosentsatsForAvgiftsberegning = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "prosentsatsForAvgiftsberegning"),
        "prosentsatsForAvgiftsberegning",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_Arbeidsgiveravgiftsgrunnlag_urnskefastsettinginnsamlinga_meldingenv2_1prosentsatsForAvgiftsberegning",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 372, 3
        ),
    )

    prosentsatsForAvgiftsberegning = property(
        __prosentsatsForAvgiftsberegning.value,
        __prosentsatsForAvgiftsberegning.set,
        None,
        None,
    )

    _ElementMap.update(
        {
            __beregningskodeForArbeidsgiveravgift.name(): __beregningskodeForArbeidsgiveravgift,
            __sone.name(): __sone,
            __avgiftsgrunnlagBeloep.name(): __avgiftsgrunnlagBeloep,
            __prosentsatsForAvgiftsberegning.name(): __prosentsatsForAvgiftsberegning,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Arbeidsgiveravgiftsgrunnlag = Arbeidsgiveravgiftsgrunnlag
Namespace.addCategoryObject(
    "typeBinding", "Arbeidsgiveravgiftsgrunnlag", Arbeidsgiveravgiftsgrunnlag
)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}UtenlandskeMedSaerskiltProsentsats with content type ELEMENT_ONLY
class UtenlandskeMedSaerskiltProsentsats(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}UtenlandskeMedSaerskiltProsentsats with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(
        Namespace, "UtenlandskeMedSaerskiltProsentsats"
    )
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 390, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}avgiftsgrunnlagBeloep uses Python identifier avgiftsgrunnlagBeloep
    __avgiftsgrunnlagBeloep = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "avgiftsgrunnlagBeloep"),
        "avgiftsgrunnlagBeloep",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_UtenlandskeMedSaerskiltProsentsats_urnskefastsettinginnsamlinga_meldingenv2_1avgiftsgrunnlagBeloep",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 392, 3
        ),
    )

    avgiftsgrunnlagBeloep = property(
        __avgiftsgrunnlagBeloep.value, __avgiftsgrunnlagBeloep.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}prosentsatsForAvgiftsberegning uses Python identifier prosentsatsForAvgiftsberegning
    __prosentsatsForAvgiftsberegning = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "prosentsatsForAvgiftsberegning"),
        "prosentsatsForAvgiftsberegning",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_UtenlandskeMedSaerskiltProsentsats_urnskefastsettinginnsamlinga_meldingenv2_1prosentsatsForAvgiftsberegning",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 393, 3
        ),
    )

    prosentsatsForAvgiftsberegning = property(
        __prosentsatsForAvgiftsberegning.value,
        __prosentsatsForAvgiftsberegning.set,
        None,
        None,
    )

    _ElementMap.update(
        {
            __avgiftsgrunnlagBeloep.name(): __avgiftsgrunnlagBeloep,
            __prosentsatsForAvgiftsberegning.name(): __prosentsatsForAvgiftsberegning,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.UtenlandskeMedSaerskiltProsentsats = (
    UtenlandskeMedSaerskiltProsentsats
)
Namespace.addCategoryObject(
    "typeBinding",
    "UtenlandskeMedSaerskiltProsentsats",
    UtenlandskeMedSaerskiltProsentsats,
)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}UtenlandskeMedFastAvgiftsbeloep with content type ELEMENT_ONLY
class UtenlandskeMedFastAvgiftsbeloep(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}UtenlandskeMedFastAvgiftsbeloep with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(
        Namespace, "UtenlandskeMedFastAvgiftsbeloep"
    )
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 396, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}antallAvgiftsgrunnlagPersoner uses Python identifier antallAvgiftsgrunnlagPersoner
    __antallAvgiftsgrunnlagPersoner = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "antallAvgiftsgrunnlagPersoner"),
        "antallAvgiftsgrunnlagPersoner",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_UtenlandskeMedFastAvgiftsbeloep_urnskefastsettinginnsamlinga_meldingenv2_1antallAvgiftsgrunnlagPersoner",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 398, 3
        ),
    )

    antallAvgiftsgrunnlagPersoner = property(
        __antallAvgiftsgrunnlagPersoner.value,
        __antallAvgiftsgrunnlagPersoner.set,
        None,
        None,
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}beloepssatsForAvgiftsberegning uses Python identifier beloepssatsForAvgiftsberegning
    __beloepssatsForAvgiftsberegning = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "beloepssatsForAvgiftsberegning"),
        "beloepssatsForAvgiftsberegning",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_UtenlandskeMedFastAvgiftsbeloep_urnskefastsettinginnsamlinga_meldingenv2_1beloepssatsForAvgiftsberegning",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 399, 3
        ),
    )

    beloepssatsForAvgiftsberegning = property(
        __beloepssatsForAvgiftsberegning.value,
        __beloepssatsForAvgiftsberegning.set,
        None,
        None,
    )

    _ElementMap.update(
        {
            __antallAvgiftsgrunnlagPersoner.name(): __antallAvgiftsgrunnlagPersoner,
            __beloepssatsForAvgiftsberegning.name(): __beloepssatsForAvgiftsberegning,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.UtenlandskeMedFastAvgiftsbeloep = UtenlandskeMedFastAvgiftsbeloep
Namespace.addCategoryObject(
    "typeBinding", "UtenlandskeMedFastAvgiftsbeloep", UtenlandskeMedFastAvgiftsbeloep
)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}FradragIGrunnlaget with content type ELEMENT_ONLY
class FradragIGrunnlaget(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}FradragIGrunnlaget with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "FradragIGrunnlaget")
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 402, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}beregningskodeForArbeidsgiveravgift uses Python identifier beregningskodeForArbeidsgiveravgift
    __beregningskodeForArbeidsgiveravgift = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "beregningskodeForArbeidsgiveravgift"),
        "beregningskodeForArbeidsgiveravgift",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_FradragIGrunnlaget_urnskefastsettinginnsamlinga_meldingenv2_1beregningskodeForArbeidsgiveravgift",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 404, 3
        ),
    )

    beregningskodeForArbeidsgiveravgift = property(
        __beregningskodeForArbeidsgiveravgift.value,
        __beregningskodeForArbeidsgiveravgift.set,
        None,
        None,
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}sone uses Python identifier sone
    __sone = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "sone"),
        "sone",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_FradragIGrunnlaget_urnskefastsettinginnsamlinga_meldingenv2_1sone",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 405, 3
        ),
    )

    sone = property(__sone.value, __sone.set, None, None)

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}avgiftsfradragBeloep uses Python identifier avgiftsfradragBeloep
    __avgiftsfradragBeloep = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "avgiftsfradragBeloep"),
        "avgiftsfradragBeloep",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_FradragIGrunnlaget_urnskefastsettinginnsamlinga_meldingenv2_1avgiftsfradragBeloep",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 406, 3
        ),
    )

    avgiftsfradragBeloep = property(
        __avgiftsfradragBeloep.value, __avgiftsfradragBeloep.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}prosentsatsForAvgiftsberegning uses Python identifier prosentsatsForAvgiftsberegning
    __prosentsatsForAvgiftsberegning = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "prosentsatsForAvgiftsberegning"),
        "prosentsatsForAvgiftsberegning",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_FradragIGrunnlaget_urnskefastsettinginnsamlinga_meldingenv2_1prosentsatsForAvgiftsberegning",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 407, 3
        ),
    )

    prosentsatsForAvgiftsberegning = property(
        __prosentsatsForAvgiftsberegning.value,
        __prosentsatsForAvgiftsberegning.set,
        None,
        None,
    )

    _ElementMap.update(
        {
            __beregningskodeForArbeidsgiveravgift.name(): __beregningskodeForArbeidsgiveravgift,
            __sone.name(): __sone,
            __avgiftsfradragBeloep.name(): __avgiftsfradragBeloep,
            __prosentsatsForAvgiftsberegning.name(): __prosentsatsForAvgiftsberegning,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.FradragIGrunnlaget = FradragIGrunnlaget
Namespace.addCategoryObject("typeBinding", "FradragIGrunnlaget", FradragIGrunnlaget)


# Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}FradragIGrunnlagetForUtenlandsk with content type ELEMENT_ONLY
class FradragIGrunnlagetForUtenlandsk(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}FradragIGrunnlagetForUtenlandsk with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(
        Namespace, "FradragIGrunnlagetForUtenlandsk"
    )
    _XSDLocation = pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 410, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}avgiftsfradragBeloep uses Python identifier avgiftsfradragBeloep
    __avgiftsfradragBeloep = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "avgiftsfradragBeloep"),
        "avgiftsfradragBeloep",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_FradragIGrunnlagetForUtenlandsk_urnskefastsettinginnsamlinga_meldingenv2_1avgiftsfradragBeloep",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 412, 3
        ),
    )

    avgiftsfradragBeloep = property(
        __avgiftsfradragBeloep.value, __avgiftsfradragBeloep.set, None, None
    )

    # Element {urn:ske:fastsetting:innsamling:a-meldingen:v2_1}prosentsatsForAvgiftsberegning uses Python identifier prosentsatsForAvgiftsberegning
    __prosentsatsForAvgiftsberegning = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "prosentsatsForAvgiftsberegning"),
        "prosentsatsForAvgiftsberegning",
        "__urnskefastsettinginnsamlinga_meldingenv2_1_FradragIGrunnlagetForUtenlandsk_urnskefastsettinginnsamlinga_meldingenv2_1prosentsatsForAvgiftsberegning",
        False,
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 413, 3
        ),
    )

    prosentsatsForAvgiftsberegning = property(
        __prosentsatsForAvgiftsberegning.value,
        __prosentsatsForAvgiftsberegning.set,
        None,
        None,
    )

    _ElementMap.update(
        {
            __avgiftsfradragBeloep.name(): __avgiftsfradragBeloep,
            __prosentsatsForAvgiftsberegning.name(): __prosentsatsForAvgiftsberegning,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.FradragIGrunnlagetForUtenlandsk = FradragIGrunnlagetForUtenlandsk
Namespace.addCategoryObject(
    "typeBinding", "FradragIGrunnlagetForUtenlandsk", FradragIGrunnlagetForUtenlandsk
)


melding = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "melding"),
    EDAG_M,
    location=pyxb.utils.utility.Location(
        "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 3, 1
    ),
)
Namespace.addCategoryObject("elementBinding", melding.name().localName(), melding)


EDAG_M._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Leveranse"),
        Leveranse,
        scope=EDAG_M,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 6, 3
        ),
    )
)


def _BuildAutomaton():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        EDAG_M._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Leveranse")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 6, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


EDAG_M._Automaton = _BuildAutomaton()


Leveranse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "leveringstidspunkt"),
        DatoTid,
        scope=Leveranse,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 11, 3
        ),
    )
)

Leveranse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "kalendermaaned"),
        STD_ANON,
        scope=Leveranse,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 12, 3
        ),
    )
)

Leveranse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "kildesystem"),
        TekstMedRestriksjon,
        scope=Leveranse,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 20, 3
        ),
    )
)

Leveranse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "erstatterMeldingsId"),
        Identifikator,
        scope=Leveranse,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 21, 3
        ),
    )
)

Leveranse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "meldingsId"),
        Identifikator,
        scope=Leveranse,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 22, 3
        ),
    )
)

Leveranse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "opplysningspliktig"),
        Opplysningspliktig,
        scope=Leveranse,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 23, 3
        ),
    )
)

Leveranse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "oppgave"),
        JuridiskEntitet,
        scope=Leveranse,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 24, 3
        ),
    )
)

Leveranse._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "spraakForTilbakemelding"),
        Spraak,
        scope=Leveranse,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 25, 3
        ),
    )
)


def _BuildAutomaton_():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 21, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 25, 3
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Leveranse._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "leveringstidspunkt")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 11, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Leveranse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "kalendermaaned")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 12, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Leveranse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "kildesystem")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 20, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Leveranse._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "erstatterMeldingsId")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 21, 3
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Leveranse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "meldingsId")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 22, 3
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Leveranse._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "opplysningspliktig")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 23, 3
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Leveranse._UseForTag(pyxb.namespace.ExpandedName(Namespace, "oppgave")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 24, 3
        ),
    )
    st_6 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        Leveranse._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "spraakForTilbakemelding")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 25, 3
        ),
    )
    st_7 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    transitions.append(fac.Transition(st_4, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, []))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, []))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, []))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_1, True)]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Leveranse._Automaton = _BuildAutomaton_()


Opplysningspliktig._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "norskIdentifikator"),
        NorskIdentifikator,
        scope=Opplysningspliktig,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 30, 3
        ),
    )
)


def _BuildAutomaton_2():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Opplysningspliktig._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "norskIdentifikator")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 30, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Opplysningspliktig._Automaton = _BuildAutomaton_2()


JuridiskEntitet._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "betalingsinformasjon"),
        Betalingsinformasjon,
        scope=JuridiskEntitet,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 35, 3
        ),
    )
)

JuridiskEntitet._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(
            Namespace, "betalingsinformasjonForForenkletOrdning"
        ),
        BetalingsinformasjonForForenkletOrdning,
        scope=JuridiskEntitet,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 36, 3
        ),
    )
)

JuridiskEntitet._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "annenBagatellmessigStoette"),
        Beloep,
        scope=JuridiskEntitet,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 37, 3
        ),
    )
)

JuridiskEntitet._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "virksomhet"),
        Virksomhet,
        scope=JuridiskEntitet,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 38, 3
        ),
    )
)


def _BuildAutomaton_3():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 35, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 36, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 37, 3
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 38, 3
        ),
    )
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        JuridiskEntitet._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "betalingsinformasjon")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 35, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        JuridiskEntitet._UseForTag(
            pyxb.namespace.ExpandedName(
                Namespace, "betalingsinformasjonForForenkletOrdning"
            )
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 36, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        JuridiskEntitet._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "annenBagatellmessigStoette")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 37, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        JuridiskEntitet._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "virksomhet")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 38, 3
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_3, True)]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


JuridiskEntitet._Automaton = _BuildAutomaton_3()


Betalingsinformasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "sumForskuddstrekk"),
        BeloepSomHeltall,
        scope=Betalingsinformasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 43, 3
        ),
    )
)

Betalingsinformasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "sumArbeidsgiveravgift"),
        BeloepSomHeltall,
        scope=Betalingsinformasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 44, 3
        ),
    )
)

Betalingsinformasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "sumFinansskattLoenn"),
        BeloepSomHeltall,
        scope=Betalingsinformasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 45, 3
        ),
    )
)


def _BuildAutomaton_4():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 43, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 44, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 45, 3
        ),
    )
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        Betalingsinformasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "sumForskuddstrekk")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 43, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        Betalingsinformasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "sumArbeidsgiveravgift")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 44, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        Betalingsinformasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "sumFinansskattLoenn")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 45, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_2, True)]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Betalingsinformasjon._Automaton = _BuildAutomaton_4()


BetalingsinformasjonForForenkletOrdning._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "sumForskuddstrekk"),
        BeloepSomHeltall,
        scope=BetalingsinformasjonForForenkletOrdning,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 50, 3
        ),
    )
)

BetalingsinformasjonForForenkletOrdning._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "sumArbeidsgiveravgift"),
        BeloepSomHeltall,
        scope=BetalingsinformasjonForForenkletOrdning,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 51, 3
        ),
    )
)

BetalingsinformasjonForForenkletOrdning._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "loennsutbetalingsdato"),
        Dato,
        scope=BetalingsinformasjonForForenkletOrdning,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 52, 3
        ),
    )
)


def _BuildAutomaton_5():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 50, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 51, 3
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        BetalingsinformasjonForForenkletOrdning._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "sumForskuddstrekk")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 50, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        BetalingsinformasjonForForenkletOrdning._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "sumArbeidsgiveravgift")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 51, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        BetalingsinformasjonForForenkletOrdning._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "loennsutbetalingsdato")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 52, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


BetalingsinformasjonForForenkletOrdning._Automaton = _BuildAutomaton_5()


Virksomhet._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "norskIdentifikator"),
        NorskIdentifikator,
        scope=Virksomhet,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 57, 3
        ),
    )
)

Virksomhet._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "inntektsmottaker"),
        Inntektsmottaker,
        scope=Virksomhet,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 58, 3
        ),
    )
)

Virksomhet._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "arbeidsgiveravgift"),
        Arbeidsgiveravgift,
        scope=Virksomhet,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 59, 3
        ),
    )
)


def _BuildAutomaton_6():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 58, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 59, 3
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Virksomhet._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "norskIdentifikator")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 57, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        Virksomhet._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "inntektsmottaker")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 58, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        Virksomhet._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "arbeidsgiveravgift")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 59, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    transitions.append(fac.Transition(st_2, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, True)]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Virksomhet._Automaton = _BuildAutomaton_6()


Inntektsmottaker._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "norskIdentifikator"),
        NorskIdentifikator,
        scope=Inntektsmottaker,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 64, 3
        ),
    )
)

Inntektsmottaker._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "internasjonalIdentifikator"),
        InternasjonalIdentifikator,
        scope=Inntektsmottaker,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 65, 3
        ),
    )
)

Inntektsmottaker._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "identifiserendeInformasjon"),
        IdentifiserendeInformasjon,
        scope=Inntektsmottaker,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 66, 3
        ),
    )
)

Inntektsmottaker._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "arbeidsforhold"),
        Arbeidsforhold,
        scope=Inntektsmottaker,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 67, 3
        ),
    )
)

Inntektsmottaker._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "fradrag"),
        Fradrag,
        scope=Inntektsmottaker,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 68, 3
        ),
    )
)

Inntektsmottaker._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "forskuddstrekk"),
        Forskuddstrekk,
        scope=Inntektsmottaker,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 69, 3
        ),
    )
)

Inntektsmottaker._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "inntekt"),
        Inntekt,
        scope=Inntektsmottaker,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 70, 3
        ),
    )
)

Inntektsmottaker._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "sjoefolksrelatertInformasjon"),
        SjoefolksrelatertInformasjon,
        scope=Inntektsmottaker,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 71, 3
        ),
    )
)

Inntektsmottaker._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "oppholdPaaSvalbardJanMayenOgBilandene"),
        OppholdPaaSvalbardJanMayenOgBilandene,
        scope=Inntektsmottaker,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 72, 3
        ),
    )
)


def _BuildAutomaton_7():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 64, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 65, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 66, 3
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 67, 3
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 68, 3
        ),
    )
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 69, 3
        ),
    )
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 70, 3
        ),
    )
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 71, 3
        ),
    )
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 72, 3
        ),
    )
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        Inntektsmottaker._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "norskIdentifikator")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 64, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        Inntektsmottaker._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "internasjonalIdentifikator")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 65, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        Inntektsmottaker._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "identifiserendeInformasjon")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 66, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        Inntektsmottaker._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "arbeidsforhold")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 67, 3
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(
        Inntektsmottaker._UseForTag(pyxb.namespace.ExpandedName(Namespace, "fradrag")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 68, 3
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(
        Inntektsmottaker._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "forskuddstrekk")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 69, 3
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(
        Inntektsmottaker._UseForTag(pyxb.namespace.ExpandedName(Namespace, "inntekt")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 70, 3
        ),
    )
    st_6 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(
        Inntektsmottaker._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "sjoefolksrelatertInformasjon")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 71, 3
        ),
    )
    st_7 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(
        Inntektsmottaker._UseForTag(
            pyxb.namespace.ExpandedName(
                Namespace, "oppholdPaaSvalbardJanMayenOgBilandene"
            )
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 72, 3
        ),
    )
    st_8 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_8, True)]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Inntektsmottaker._Automaton = _BuildAutomaton_7()


InternasjonalIdentifikator._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "identifikator"),
        TekstMedRestriksjon,
        scope=InternasjonalIdentifikator,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 77, 3
        ),
    )
)

InternasjonalIdentifikator._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "identifikatortype"),
        InternasjonalIdentifikatortype,
        scope=InternasjonalIdentifikator,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 78, 3
        ),
    )
)

InternasjonalIdentifikator._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "land"),
        Landkode,
        scope=InternasjonalIdentifikator,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 79, 3
        ),
    )
)


def _BuildAutomaton_8():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        InternasjonalIdentifikator._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "identifikator")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 77, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        InternasjonalIdentifikator._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "identifikatortype")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 78, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        InternasjonalIdentifikator._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "land")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 79, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


InternasjonalIdentifikator._Automaton = _BuildAutomaton_8()


IdentifiserendeInformasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "navn"),
        TekstMedRestriksjon,
        scope=IdentifiserendeInformasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 90, 3
        ),
    )
)

IdentifiserendeInformasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "foedselsdato"),
        Dato,
        scope=IdentifiserendeInformasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 91, 3
        ),
    )
)

IdentifiserendeInformasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ansattnummer"),
        TekstMedRestriksjon,
        scope=IdentifiserendeInformasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 92, 3
        ),
    )
)


def _BuildAutomaton_9():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 92, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        IdentifiserendeInformasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "navn")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 90, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        IdentifiserendeInformasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "foedselsdato")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 91, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        IdentifiserendeInformasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "ansattnummer")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 92, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, True)]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


IdentifiserendeInformasjon._Automaton = _BuildAutomaton_9()


Arbeidsforhold._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "arbeidsforholdId"),
        Identifikator,
        scope=Arbeidsforhold,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 97, 3
        ),
    )
)

Arbeidsforhold._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "typeArbeidsforhold"),
        Arbeidsforholdstype,
        scope=Arbeidsforhold,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 98, 3
        ),
    )
)

Arbeidsforhold._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "startdato"),
        Dato,
        scope=Arbeidsforhold,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 99, 3
        ),
    )
)

Arbeidsforhold._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "sluttdato"),
        Dato,
        scope=Arbeidsforhold,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 100, 3
        ),
    )
)

Arbeidsforhold._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(
            Namespace, "antallTimerPerUkeSomEnFullStillingTilsvarer"
        ),
        Desimaltall,
        scope=Arbeidsforhold,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 101, 3
        ),
    )
)

Arbeidsforhold._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "avloenningstype"),
        Avloenningstype,
        scope=Arbeidsforhold,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 102, 3
        ),
    )
)

Arbeidsforhold._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "yrke"),
        Yrke,
        scope=Arbeidsforhold,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 103, 3
        ),
    )
)

Arbeidsforhold._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "arbeidstidsordning"),
        Arbeidstidsordning,
        scope=Arbeidsforhold,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 104, 3
        ),
    )
)

Arbeidsforhold._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "stillingsprosent"),
        Desimaltall,
        scope=Arbeidsforhold,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 105, 3
        ),
    )
)

Arbeidsforhold._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "sisteLoennsendringsdato"),
        Dato,
        scope=Arbeidsforhold,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 106, 3
        ),
    )
)

Arbeidsforhold._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "loennsansiennitet"),
        Dato,
        scope=Arbeidsforhold,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 107, 3
        ),
    )
)

Arbeidsforhold._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "loennstrinn"),
        TekstMedRestriksjon,
        scope=Arbeidsforhold,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 108, 3
        ),
    )
)

Arbeidsforhold._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "fartoey"),
        Fartoey,
        scope=Arbeidsforhold,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 109, 3
        ),
    )
)

Arbeidsforhold._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "permisjon"),
        Permisjon,
        scope=Arbeidsforhold,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 110, 3
        ),
    )
)

Arbeidsforhold._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "sisteDatoForStillingsprosentendring"),
        Dato,
        scope=Arbeidsforhold,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 111, 3
        ),
    )
)


def _BuildAutomaton_10():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 97, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 99, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 100, 3
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 101, 3
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 102, 3
        ),
    )
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 103, 3
        ),
    )
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 104, 3
        ),
    )
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 105, 3
        ),
    )
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 106, 3
        ),
    )
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 107, 3
        ),
    )
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 108, 3
        ),
    )
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 109, 3
        ),
    )
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 110, 3
        ),
    )
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 111, 3
        ),
    )
    counters.add(cc_13)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsforhold._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "arbeidsforholdId")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 97, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsforhold._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "typeArbeidsforhold")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 98, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, "startdato")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 99, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, "sluttdato")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 100, 3
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsforhold._UseForTag(
            pyxb.namespace.ExpandedName(
                Namespace, "antallTimerPerUkeSomEnFullStillingTilsvarer"
            )
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 101, 3
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsforhold._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "avloenningstype")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 102, 3
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, "yrke")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 103, 3
        ),
    )
    st_6 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsforhold._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "arbeidstidsordning")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 104, 3
        ),
    )
    st_7 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsforhold._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "stillingsprosent")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 105, 3
        ),
    )
    st_8 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsforhold._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "sisteLoennsendringsdato")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 106, 3
        ),
    )
    st_9 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsforhold._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "loennsansiennitet")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 107, 3
        ),
    )
    st_10 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsforhold._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "loennstrinn")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 108, 3
        ),
    )
    st_11 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, "fartoey")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 109, 3
        ),
    )
    st_12 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsforhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, "permisjon")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 110, 3
        ),
    )
    st_13 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsforhold._UseForTag(
            pyxb.namespace.ExpandedName(
                Namespace, "sisteDatoForStillingsprosentendring"
            )
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 111, 3
        ),
    )
    st_14 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_14)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    transitions.append(fac.Transition(st_4, []))
    transitions.append(fac.Transition(st_5, []))
    transitions.append(fac.Transition(st_6, []))
    transitions.append(fac.Transition(st_7, []))
    transitions.append(fac.Transition(st_8, []))
    transitions.append(fac.Transition(st_9, []))
    transitions.append(fac.Transition(st_10, []))
    transitions.append(fac.Transition(st_11, []))
    transitions.append(fac.Transition(st_12, []))
    transitions.append(fac.Transition(st_13, []))
    transitions.append(fac.Transition(st_14, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_2, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_3, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_6, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_7, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_8, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_9, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_10, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_11, True)]))
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_11, False)]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_12, True)]))
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_12, False)]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [fac.UpdateInstruction(cc_13, True)]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Arbeidsforhold._Automaton = _BuildAutomaton_10()


Fartoey._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "skipsregister"),
        Skipsregister,
        scope=Fartoey,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 128, 3
        ),
    )
)

Fartoey._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "skipstype"),
        Skipstype,
        scope=Fartoey,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 129, 3
        ),
    )
)

Fartoey._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "fartsomraade"),
        Fartsomraade,
        scope=Fartoey,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 130, 3
        ),
    )
)


def _BuildAutomaton_11():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Fartoey._UseForTag(pyxb.namespace.ExpandedName(Namespace, "skipsregister")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 128, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Fartoey._UseForTag(pyxb.namespace.ExpandedName(Namespace, "skipstype")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 129, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Fartoey._UseForTag(pyxb.namespace.ExpandedName(Namespace, "fartsomraade")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 130, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Fartoey._Automaton = _BuildAutomaton_11()


Permisjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "startdato"),
        Dato,
        scope=Permisjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 147, 3
        ),
    )
)

Permisjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "sluttdato"),
        Dato,
        scope=Permisjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 148, 3
        ),
    )
)

Permisjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "permisjonsprosent"),
        Desimaltall,
        scope=Permisjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 149, 3
        ),
    )
)

Permisjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "permisjonId"),
        Identifikator,
        scope=Permisjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 150, 3
        ),
    )
)

Permisjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "beskrivelse"),
        PermisjonsOgPermitteringsBeskrivelse,
        scope=Permisjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 151, 3
        ),
    )
)


def _BuildAutomaton_12():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 148, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Permisjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, "startdato")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 147, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Permisjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, "sluttdato")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 148, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Permisjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "permisjonsprosent")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 149, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Permisjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, "permisjonId")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 150, 3
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Permisjon._UseForTag(pyxb.namespace.ExpandedName(Namespace, "beskrivelse")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 151, 3
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    transitions.append(fac.Transition(st_2, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Permisjon._Automaton = _BuildAutomaton_12()


Fradrag._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "beskrivelse"),
        Fradragsbeskrivelse,
        scope=Fradrag,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 156, 3
        ),
    )
)

Fradrag._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "beloep"),
        Beloep,
        scope=Fradrag,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 157, 3
        ),
    )
)


def _BuildAutomaton_13():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Fradrag._UseForTag(pyxb.namespace.ExpandedName(Namespace, "beskrivelse")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 156, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Fradrag._UseForTag(pyxb.namespace.ExpandedName(Namespace, "beloep")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 157, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Fradrag._Automaton = _BuildAutomaton_13()


Forskuddstrekk._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "beskrivelse"),
        Forskuddstrekksbeskrivelse,
        scope=Forskuddstrekk,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 165, 3
        ),
    )
)

Forskuddstrekk._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "beloep"),
        BeloepSomHeltall,
        scope=Forskuddstrekk,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 166, 3
        ),
    )
)


def _BuildAutomaton_14():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 165, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Forskuddstrekk._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "beskrivelse")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 165, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Forskuddstrekk._UseForTag(pyxb.namespace.ExpandedName(Namespace, "beloep")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 166, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Forskuddstrekk._Automaton = _BuildAutomaton_14()


Inntekt._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "skatteOgAvgiftsregel"),
        SkatteOgAvgiftsregel,
        scope=Inntekt,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 174, 3
        ),
    )
)

Inntekt._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "startdatoOpptjeningsperiode"),
        Dato,
        scope=Inntekt,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 175, 3
        ),
    )
)

Inntekt._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "sluttdatoOpptjeningsperiode"),
        Dato,
        scope=Inntekt,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 176, 3
        ),
    )
)

Inntekt._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "fordel"),
        Fordel,
        scope=Inntekt,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 177, 3
        ),
    )
)

Inntekt._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "utloeserArbeidsgiveravgift"),
        Boolsk,
        scope=Inntekt,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 178, 3
        ),
    )
)

Inntekt._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "inngaarIGrunnlagForTrekk"),
        Boolsk,
        scope=Inntekt,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 179, 3
        ),
    )
)

Inntekt._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "beloep"),
        Beloep,
        scope=Inntekt,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 180, 3
        ),
    )
)

Inntekt._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "arbeidsforholdId"),
        Identifikator,
        scope=Inntekt,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 181, 3
        ),
    )
)

Inntekt._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "loennsinntekt"),
        Loennsinntekt,
        scope=Inntekt,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 183, 4
        ),
    )
)

Inntekt._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ytelseFraOffentlige"),
        YtelseFraOffentlige,
        scope=Inntekt,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 184, 4
        ),
    )
)

Inntekt._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "pensjonEllerTrygd"),
        PensjonEllerTrygd,
        scope=Inntekt,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 185, 4
        ),
    )
)

Inntekt._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "naeringsinntekt"),
        Naeringsinntekt,
        scope=Inntekt,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 186, 4
        ),
    )
)


def _BuildAutomaton_15():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 174, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 175, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 176, 3
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 181, 3
        ),
    )
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Inntekt._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "skatteOgAvgiftsregel")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 174, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Inntekt._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "startdatoOpptjeningsperiode")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 175, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Inntekt._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "sluttdatoOpptjeningsperiode")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 176, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Inntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, "fordel")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 177, 3
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Inntekt._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "utloeserArbeidsgiveravgift")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 178, 3
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Inntekt._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "inngaarIGrunnlagForTrekk")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 179, 3
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Inntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, "beloep")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 180, 3
        ),
    )
    st_6 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Inntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, "arbeidsforholdId")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 181, 3
        ),
    )
    st_7 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Inntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, "loennsinntekt")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 183, 4
        ),
    )
    st_8 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Inntekt._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "ytelseFraOffentlige")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 184, 4
        ),
    )
    st_9 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Inntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, "pensjonEllerTrygd")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 185, 4
        ),
    )
    st_10 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Inntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, "naeringsinntekt")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 186, 4
        ),
    )
    st_11 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, []))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, []))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, []))
    transitions.append(fac.Transition(st_8, []))
    transitions.append(fac.Transition(st_9, []))
    transitions.append(fac.Transition(st_10, []))
    transitions.append(fac.Transition(st_11, []))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_3, False)]))
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


Inntekt._Automaton = _BuildAutomaton_15()


Loennsinntekt._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "beskrivelse"),
        Loennsbeskrivelse,
        scope=Loennsinntekt,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 198, 3
        ),
    )
)

Loennsinntekt._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "tilleggsinformasjon"),
        Tilleggsinformasjon,
        scope=Loennsinntekt,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 199, 3
        ),
    )
)

Loennsinntekt._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "spesifikasjon"),
        Spesifikasjon,
        scope=Loennsinntekt,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 200, 3
        ),
    )
)

Loennsinntekt._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "antall"),
        Desimaltall,
        scope=Loennsinntekt,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 201, 3
        ),
    )
)


def _BuildAutomaton_16():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 199, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 200, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 201, 3
        ),
    )
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Loennsinntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, "beskrivelse")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 198, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        Loennsinntekt._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "tilleggsinformasjon")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 199, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        Loennsinntekt._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "spesifikasjon")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 200, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        Loennsinntekt._UseForTag(pyxb.namespace.ExpandedName(Namespace, "antall")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 201, 3
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, True)]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Loennsinntekt._Automaton = _BuildAutomaton_16()


Tilleggsinformasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "bilOgBaat"),
        BilOgBaat,
        scope=Tilleggsinformasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 209, 3
        ),
    )
)

Tilleggsinformasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "dagmammaIEgenBolig"),
        DagmammaIEgenBolig,
        scope=Tilleggsinformasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 210, 3
        ),
    )
)

Tilleggsinformasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "etterbetalingsperiode"),
        Periode,
        scope=Tilleggsinformasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 211, 3
        ),
    )
)

Tilleggsinformasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "inntektPaaNorskKontinentalsokkel"),
        NorskKontinentalsokkel,
        scope=Tilleggsinformasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 212, 3
        ),
    )
)

Tilleggsinformasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "inntjeningsforhold"),
        SpesielleInntjeningsforhold,
        scope=Tilleggsinformasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 213, 3
        ),
    )
)

Tilleggsinformasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "livrente"),
        Livrente,
        scope=Tilleggsinformasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 214, 3
        ),
    )
)

Tilleggsinformasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "lottOgPart"),
        LottOgPartInnenFiske,
        scope=Tilleggsinformasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 215, 3
        ),
    )
)

Tilleggsinformasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "nettoloenn"),
        Nettoloennsordning,
        scope=Tilleggsinformasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 216, 3
        ),
    )
)

Tilleggsinformasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "pensjon"),
        AldersUfoereEtterlatteAvtalefestetOgKrigspensjon,
        scope=Tilleggsinformasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 217, 3
        ),
    )
)

Tilleggsinformasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "reiseKostOgLosji"),
        ReiseKostOgLosji,
        scope=Tilleggsinformasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 218, 3
        ),
    )
)

Tilleggsinformasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "utenlandskArtist"),
        UtenlandskArtist,
        scope=Tilleggsinformasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 219, 3
        ),
    )
)

Tilleggsinformasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "bonusFraForsvaret"),
        BonusFraForsvaret,
        scope=Tilleggsinformasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 220, 3
        ),
    )
)


def _BuildAutomaton_17():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Tilleggsinformasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "bilOgBaat")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 209, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Tilleggsinformasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "dagmammaIEgenBolig")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 210, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Tilleggsinformasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "etterbetalingsperiode")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 211, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Tilleggsinformasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "inntektPaaNorskKontinentalsokkel")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 212, 3
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Tilleggsinformasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "inntjeningsforhold")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 213, 3
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Tilleggsinformasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "livrente")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 214, 3
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Tilleggsinformasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "lottOgPart")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 215, 3
        ),
    )
    st_6 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Tilleggsinformasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "nettoloenn")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 216, 3
        ),
    )
    st_7 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Tilleggsinformasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "pensjon")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 217, 3
        ),
    )
    st_8 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Tilleggsinformasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "reiseKostOgLosji")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 218, 3
        ),
    )
    st_9 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Tilleggsinformasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "utenlandskArtist")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 219, 3
        ),
    )
    st_10 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Tilleggsinformasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "bonusFraForsvaret")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 220, 3
        ),
    )
    st_11 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
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


Tilleggsinformasjon._Automaton = _BuildAutomaton_17()


Periode._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "startdato"),
        Dato,
        scope=Periode,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 225, 3
        ),
    )
)

Periode._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "sluttdato"),
        Dato,
        scope=Periode,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 226, 3
        ),
    )
)


def _BuildAutomaton_18():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Periode._UseForTag(pyxb.namespace.ExpandedName(Namespace, "startdato")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 225, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Periode._UseForTag(pyxb.namespace.ExpandedName(Namespace, "sluttdato")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 226, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Periode._Automaton = _BuildAutomaton_18()


BilOgBaat._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "antallKilometer"),
        Desimaltall,
        scope=BilOgBaat,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 231, 3
        ),
    )
)

BilOgBaat._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "antallReiser"),
        Heltall,
        scope=BilOgBaat,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 232, 3
        ),
    )
)

BilOgBaat._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(
            Namespace, "heravAntallKilometerMellomHjemOgArbeid"
        ),
        Desimaltall,
        scope=BilOgBaat,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 233, 3
        ),
    )
)

BilOgBaat._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "listeprisForBil"),
        Beloep,
        scope=BilOgBaat,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 234, 3
        ),
    )
)

BilOgBaat._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "bilregistreringsnummer"),
        TekstMedRestriksjon,
        scope=BilOgBaat,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 235, 3
        ),
    )
)

BilOgBaat._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "erBilpool"),
        Boolsk,
        scope=BilOgBaat,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 236, 3
        ),
    )
)

BilOgBaat._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "erAnnenBil"),
        Boolsk,
        scope=BilOgBaat,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 237, 3
        ),
    )
)

BilOgBaat._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "erBilUtenforStandardregelen"),
        Boolsk,
        scope=BilOgBaat,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 238, 3
        ),
    )
)

BilOgBaat._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "personklassifiseringAvBilbruker"),
        PersontypeForReiseKostLosji,
        scope=BilOgBaat,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 239, 3
        ),
    )
)


def _BuildAutomaton_19():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 231, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 232, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 233, 3
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 234, 3
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 235, 3
        ),
    )
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 236, 3
        ),
    )
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 237, 3
        ),
    )
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 238, 3
        ),
    )
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 239, 3
        ),
    )
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        BilOgBaat._UseForTag(pyxb.namespace.ExpandedName(Namespace, "antallKilometer")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 231, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        BilOgBaat._UseForTag(pyxb.namespace.ExpandedName(Namespace, "antallReiser")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 232, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        BilOgBaat._UseForTag(
            pyxb.namespace.ExpandedName(
                Namespace, "heravAntallKilometerMellomHjemOgArbeid"
            )
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 233, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        BilOgBaat._UseForTag(pyxb.namespace.ExpandedName(Namespace, "listeprisForBil")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 234, 3
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(
        BilOgBaat._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "bilregistreringsnummer")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 235, 3
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(
        BilOgBaat._UseForTag(pyxb.namespace.ExpandedName(Namespace, "erBilpool")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 236, 3
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(
        BilOgBaat._UseForTag(pyxb.namespace.ExpandedName(Namespace, "erAnnenBil")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 237, 3
        ),
    )
    st_6 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(
        BilOgBaat._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "erBilUtenforStandardregelen")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 238, 3
        ),
    )
    st_7 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(
        BilOgBaat._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "personklassifiseringAvBilbruker")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 239, 3
        ),
    )
    st_8 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_8, True)]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


BilOgBaat._Automaton = _BuildAutomaton_19()


DagmammaIEgenBolig._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "antallBarn"),
        Heltall,
        scope=DagmammaIEgenBolig,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 247, 3
        ),
    )
)

DagmammaIEgenBolig._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "antallMaaneder"),
        Heltall,
        scope=DagmammaIEgenBolig,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 248, 3
        ),
    )
)


def _BuildAutomaton_20():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        DagmammaIEgenBolig._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "antallBarn")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 247, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        DagmammaIEgenBolig._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "antallMaaneder")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 248, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


DagmammaIEgenBolig._Automaton = _BuildAutomaton_20()


NorskKontinentalsokkel._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "tidsrom"),
        Periode,
        scope=NorskKontinentalsokkel,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 253, 3
        ),
    )
)

NorskKontinentalsokkel._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "gjelderLoennFoerste60Dager"),
        Boolsk,
        scope=NorskKontinentalsokkel,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 254, 3
        ),
    )
)


def _BuildAutomaton_21():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 253, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 254, 3
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        NorskKontinentalsokkel._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "tidsrom")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 253, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        NorskKontinentalsokkel._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "gjelderLoennFoerste60Dager")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 254, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


NorskKontinentalsokkel._Automaton = _BuildAutomaton_21()


Livrente._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "totaltUtbetaltBeloep"),
        Beloep,
        scope=Livrente,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 262, 3
        ),
    )
)


def _BuildAutomaton_22():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Livrente._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "totaltUtbetaltBeloep")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 262, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Livrente._Automaton = _BuildAutomaton_22()


LottOgPartInnenFiske._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "antallDager"),
        Heltall,
        scope=LottOgPartInnenFiske,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 267, 3
        ),
    )
)


def _BuildAutomaton_23():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 267, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        LottOgPartInnenFiske._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "antallDager")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 267, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


LottOgPartInnenFiske._Automaton = _BuildAutomaton_23()


Nettoloennsordning._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "oppgrossingstabellnummer"),
        Heltall,
        scope=Nettoloennsordning,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 272, 3
        ),
    )
)

Nettoloennsordning._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "bilinformasjon"),
        BilOgBaat,
        scope=Nettoloennsordning,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 273, 3
        ),
    )
)

Nettoloennsordning._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "betaltSkattebeloepIUtlandet"),
        Beloep,
        scope=Nettoloennsordning,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 274, 3
        ),
    )
)


def _BuildAutomaton_24():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 272, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 273, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 274, 3
        ),
    )
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        Nettoloennsordning._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "oppgrossingstabellnummer")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 272, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        Nettoloennsordning._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "bilinformasjon")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 273, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        Nettoloennsordning._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "betaltSkattebeloepIUtlandet")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 274, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_2, True)]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Nettoloennsordning._Automaton = _BuildAutomaton_24()


AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "grunnpensjonsbeloep"),
        Beloep,
        scope=AldersUfoereEtterlatteAvtalefestetOgKrigspensjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 279, 3
        ),
    )
)

AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "tilleggspensjonsbeloep"),
        Beloep,
        scope=AldersUfoereEtterlatteAvtalefestetOgKrigspensjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 280, 3
        ),
    )
)

AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ufoeregrad"),
        Heltall,
        scope=AldersUfoereEtterlatteAvtalefestetOgKrigspensjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 281, 3
        ),
    )
)

AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "pensjonsgrad"),
        Heltall,
        scope=AldersUfoereEtterlatteAvtalefestetOgKrigspensjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 282, 3
        ),
    )
)

AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "heravEtterlattepensjon"),
        Beloep,
        scope=AldersUfoereEtterlatteAvtalefestetOgKrigspensjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 283, 3
        ),
    )
)

AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "tidsrom"),
        Periode,
        scope=AldersUfoereEtterlatteAvtalefestetOgKrigspensjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 284, 3
        ),
    )
)


def _BuildAutomaton_25():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 279, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 280, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 281, 3
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 282, 3
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 283, 3
        ),
    )
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 284, 3
        ),
    )
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "grunnpensjonsbeloep")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 279, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "tilleggspensjonsbeloep")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 280, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "ufoeregrad")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 281, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "pensjonsgrad")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 282, 3
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(
        AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "heravEtterlattepensjon")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 283, 3
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(
        AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "tidsrom")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 284, 3
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_5, True)]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


AldersUfoereEtterlatteAvtalefestetOgKrigspensjon._Automaton = _BuildAutomaton_25()


ReiseKostOgLosji._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "persontype"),
        PersontypeForReiseKostLosji,
        scope=ReiseKostOgLosji,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 289, 3
        ),
    )
)

ReiseKostOgLosji._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "antallReiser"),
        Heltall,
        scope=ReiseKostOgLosji,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 290, 3
        ),
    )
)


def _BuildAutomaton_26():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 289, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 290, 3
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        ReiseKostOgLosji._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "persontype")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 289, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        ReiseKostOgLosji._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "antallReiser")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 290, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


ReiseKostOgLosji._Automaton = _BuildAutomaton_26()


UtenlandskArtist._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "inntektsaar"),
        AArstall,
        scope=UtenlandskArtist,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 295, 3
        ),
    )
)

UtenlandskArtist._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "oppgrossingsgrunnlag"),
        Beloep,
        scope=UtenlandskArtist,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 296, 3
        ),
    )
)

UtenlandskArtist._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "trukketArtistskatt"),
        BeloepSomHeltall,
        scope=UtenlandskArtist,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 297, 3
        ),
    )
)


def _BuildAutomaton_27():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        UtenlandskArtist._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "inntektsaar")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 295, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        UtenlandskArtist._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "oppgrossingsgrunnlag")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 296, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        UtenlandskArtist._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "trukketArtistskatt")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 297, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


UtenlandskArtist._Automaton = _BuildAutomaton_27()


BonusFraForsvaret._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "aaretUtbetalingenGjelderFor"),
        AArstall,
        scope=BonusFraForsvaret,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 302, 3
        ),
    )
)


def _BuildAutomaton_28():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 302, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        BonusFraForsvaret._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "aaretUtbetalingenGjelderFor")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 302, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


BonusFraForsvaret._Automaton = _BuildAutomaton_28()


Spesifikasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "skattemessigBosattILand"),
        Landkode,
        scope=Spesifikasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 307, 3
        ),
    )
)

Spesifikasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "opptjeningsland"),
        Landkode,
        scope=Spesifikasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 308, 3
        ),
    )
)

Spesifikasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "erOpptjentPaaHjelpefartoey"),
        Boolsk,
        scope=Spesifikasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 309, 3
        ),
    )
)

Spesifikasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "erOpptjentPaaKontinentalsokkel"),
        Boolsk,
        scope=Spesifikasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 310, 3
        ),
    )
)


def _BuildAutomaton_29():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 307, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 308, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 309, 3
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 310, 3
        ),
    )
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        Spesifikasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "skattemessigBosattILand")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 307, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        Spesifikasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "opptjeningsland")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 308, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        Spesifikasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "erOpptjentPaaHjelpefartoey")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 309, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        Spesifikasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "erOpptjentPaaKontinentalsokkel")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 310, 3
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_3, True)]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Spesifikasjon._Automaton = _BuildAutomaton_29()


YtelseFraOffentlige._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "beskrivelse"),
        YtelseFraOffentligeBeskrivelse,
        scope=YtelseFraOffentlige,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 315, 3
        ),
    )
)

YtelseFraOffentlige._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "tilleggsinformasjon"),
        Tilleggsinformasjon,
        scope=YtelseFraOffentlige,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 316, 3
        ),
    )
)


def _BuildAutomaton_30():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 316, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        YtelseFraOffentlige._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "beskrivelse")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 315, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        YtelseFraOffentlige._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "tilleggsinformasjon")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 316, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


YtelseFraOffentlige._Automaton = _BuildAutomaton_30()


PensjonEllerTrygd._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "beskrivelse"),
        PensjonEllerTrygdebeskrivelse,
        scope=PensjonEllerTrygd,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 324, 3
        ),
    )
)

PensjonEllerTrygd._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "tilleggsinformasjon"),
        Tilleggsinformasjon,
        scope=PensjonEllerTrygd,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 325, 3
        ),
    )
)


def _BuildAutomaton_31():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 325, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        PensjonEllerTrygd._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "beskrivelse")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 324, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        PensjonEllerTrygd._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "tilleggsinformasjon")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 325, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


PensjonEllerTrygd._Automaton = _BuildAutomaton_31()


Naeringsinntekt._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "beskrivelse"),
        Naeringsinntektsbeskrivelse,
        scope=Naeringsinntekt,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 333, 3
        ),
    )
)

Naeringsinntekt._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "tilleggsinformasjon"),
        Tilleggsinformasjon,
        scope=Naeringsinntekt,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 334, 3
        ),
    )
)


def _BuildAutomaton_32():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 334, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Naeringsinntekt._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "beskrivelse")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 333, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        Naeringsinntekt._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "tilleggsinformasjon")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 334, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Naeringsinntekt._Automaton = _BuildAutomaton_32()


SjoefolksrelatertInformasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "antallDoegnOmbord"),
        Heltall,
        scope=SjoefolksrelatertInformasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 345, 3
        ),
    )
)

SjoefolksrelatertInformasjon._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(
            Namespace, "antallDoegnOmbordUtenDekkedeSmaautgifter"
        ),
        Heltall,
        scope=SjoefolksrelatertInformasjon,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 346, 3
        ),
    )
)


def _BuildAutomaton_33():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 345, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 346, 3
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        SjoefolksrelatertInformasjon._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "antallDoegnOmbord")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 345, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        SjoefolksrelatertInformasjon._UseForTag(
            pyxb.namespace.ExpandedName(
                Namespace, "antallDoegnOmbordUtenDekkedeSmaautgifter"
            )
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 346, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


SjoefolksrelatertInformasjon._Automaton = _BuildAutomaton_33()


OppholdPaaSvalbardJanMayenOgBilandene._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "oppholdsId"),
        Identifikator,
        scope=OppholdPaaSvalbardJanMayenOgBilandene,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 351, 3
        ),
    )
)

OppholdPaaSvalbardJanMayenOgBilandene._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "startdato"),
        Dato,
        scope=OppholdPaaSvalbardJanMayenOgBilandene,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 352, 3
        ),
    )
)

OppholdPaaSvalbardJanMayenOgBilandene._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "sluttdato"),
        Dato,
        scope=OppholdPaaSvalbardJanMayenOgBilandene,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 353, 3
        ),
    )
)

OppholdPaaSvalbardJanMayenOgBilandene._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "beskrivelse"),
        OppholdsbeskrivelseForSvalbardJanMayenOgBilandene,
        scope=OppholdPaaSvalbardJanMayenOgBilandene,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 354, 3
        ),
    )
)


def _BuildAutomaton_34():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 353, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        OppholdPaaSvalbardJanMayenOgBilandene._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "oppholdsId")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 351, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        OppholdPaaSvalbardJanMayenOgBilandene._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "startdato")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 352, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        OppholdPaaSvalbardJanMayenOgBilandene._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "sluttdato")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 353, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        OppholdPaaSvalbardJanMayenOgBilandene._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "beskrivelse")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 354, 3
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


OppholdPaaSvalbardJanMayenOgBilandene._Automaton = _BuildAutomaton_34()


Arbeidsgiveravgift._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "loennOgGodtgjoerelse"),
        Arbeidsgiveravgiftsgrunnlag,
        scope=Arbeidsgiveravgift,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 359, 3
        ),
    )
)

Arbeidsgiveravgift._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "tilskuddOgPremieTilPensjon"),
        Arbeidsgiveravgiftsgrunnlag,
        scope=Arbeidsgiveravgift,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 360, 3
        ),
    )
)

Arbeidsgiveravgift._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "utenlandskeMedSaerskiltProsentsats"),
        UtenlandskeMedSaerskiltProsentsats,
        scope=Arbeidsgiveravgift,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 361, 3
        ),
    )
)

Arbeidsgiveravgift._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "utenlandskeMedFastAvgiftsbeloep"),
        UtenlandskeMedFastAvgiftsbeloep,
        scope=Arbeidsgiveravgift,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 362, 3
        ),
    )
)

Arbeidsgiveravgift._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "fradragIGrunnlagetForSone"),
        FradragIGrunnlaget,
        scope=Arbeidsgiveravgift,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 363, 3
        ),
    )
)

Arbeidsgiveravgift._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "fradragIGrunnlagetForUtenlandsk"),
        FradragIGrunnlagetForUtenlandsk,
        scope=Arbeidsgiveravgift,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 364, 3
        ),
    )
)


def _BuildAutomaton_35():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 359, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 360, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 361, 3
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 362, 3
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 363, 3
        ),
    )
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 364, 3
        ),
    )
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsgiveravgift._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "loennOgGodtgjoerelse")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 359, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsgiveravgift._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "tilskuddOgPremieTilPensjon")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 360, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsgiveravgift._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "utenlandskeMedSaerskiltProsentsats")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 361, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsgiveravgift._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "utenlandskeMedFastAvgiftsbeloep")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 362, 3
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsgiveravgift._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "fradragIGrunnlagetForSone")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 363, 3
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsgiveravgift._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "fradragIGrunnlagetForUtenlandsk")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 364, 3
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_5, True)]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Arbeidsgiveravgift._Automaton = _BuildAutomaton_35()


Arbeidsgiveravgiftsgrunnlag._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "beregningskodeForArbeidsgiveravgift"),
        BeregningskodeForArbeidsgiveravgift,
        scope=Arbeidsgiveravgiftsgrunnlag,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 369, 3
        ),
    )
)

Arbeidsgiveravgiftsgrunnlag._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "sone"),
        Arbeidsgiveravgiftsone,
        scope=Arbeidsgiveravgiftsgrunnlag,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 370, 3
        ),
    )
)

Arbeidsgiveravgiftsgrunnlag._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "avgiftsgrunnlagBeloep"),
        Beloep,
        scope=Arbeidsgiveravgiftsgrunnlag,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 371, 3
        ),
    )
)

Arbeidsgiveravgiftsgrunnlag._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "prosentsatsForAvgiftsberegning"),
        Grunnlagsprosent,
        scope=Arbeidsgiveravgiftsgrunnlag,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 372, 3
        ),
    )
)


def _BuildAutomaton_36():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsgiveravgiftsgrunnlag._UseForTag(
            pyxb.namespace.ExpandedName(
                Namespace, "beregningskodeForArbeidsgiveravgift"
            )
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 369, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsgiveravgiftsgrunnlag._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "sone")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 370, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsgiveravgiftsgrunnlag._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "avgiftsgrunnlagBeloep")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 371, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Arbeidsgiveravgiftsgrunnlag._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "prosentsatsForAvgiftsberegning")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 372, 3
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Arbeidsgiveravgiftsgrunnlag._Automaton = _BuildAutomaton_36()


UtenlandskeMedSaerskiltProsentsats._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "avgiftsgrunnlagBeloep"),
        Beloep,
        scope=UtenlandskeMedSaerskiltProsentsats,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 392, 3
        ),
    )
)

UtenlandskeMedSaerskiltProsentsats._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "prosentsatsForAvgiftsberegning"),
        GrunnlagsprosentForUtenlandske,
        scope=UtenlandskeMedSaerskiltProsentsats,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 393, 3
        ),
    )
)


def _BuildAutomaton_37():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        UtenlandskeMedSaerskiltProsentsats._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "avgiftsgrunnlagBeloep")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 392, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        UtenlandskeMedSaerskiltProsentsats._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "prosentsatsForAvgiftsberegning")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 393, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


UtenlandskeMedSaerskiltProsentsats._Automaton = _BuildAutomaton_37()


UtenlandskeMedFastAvgiftsbeloep._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "antallAvgiftsgrunnlagPersoner"),
        Heltall,
        scope=UtenlandskeMedFastAvgiftsbeloep,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 398, 3
        ),
    )
)

UtenlandskeMedFastAvgiftsbeloep._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "beloepssatsForAvgiftsberegning"),
        GrunnlagsbeloepForUtenlandske,
        scope=UtenlandskeMedFastAvgiftsbeloep,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 399, 3
        ),
    )
)


def _BuildAutomaton_38():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        UtenlandskeMedFastAvgiftsbeloep._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "antallAvgiftsgrunnlagPersoner")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 398, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        UtenlandskeMedFastAvgiftsbeloep._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "beloepssatsForAvgiftsberegning")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 399, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


UtenlandskeMedFastAvgiftsbeloep._Automaton = _BuildAutomaton_38()


FradragIGrunnlaget._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "beregningskodeForArbeidsgiveravgift"),
        BeregningskodeForArbeidsgiveravgift,
        scope=FradragIGrunnlaget,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 404, 3
        ),
    )
)

FradragIGrunnlaget._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "sone"),
        Arbeidsgiveravgiftsone,
        scope=FradragIGrunnlaget,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 405, 3
        ),
    )
)

FradragIGrunnlaget._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "avgiftsfradragBeloep"),
        Beloep,
        scope=FradragIGrunnlaget,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 406, 3
        ),
    )
)

FradragIGrunnlaget._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "prosentsatsForAvgiftsberegning"),
        Grunnlagsprosent,
        scope=FradragIGrunnlaget,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 407, 3
        ),
    )
)


def _BuildAutomaton_39():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        FradragIGrunnlaget._UseForTag(
            pyxb.namespace.ExpandedName(
                Namespace, "beregningskodeForArbeidsgiveravgift"
            )
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 404, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        FradragIGrunnlaget._UseForTag(pyxb.namespace.ExpandedName(Namespace, "sone")),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 405, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        FradragIGrunnlaget._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "avgiftsfradragBeloep")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 406, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        FradragIGrunnlaget._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "prosentsatsForAvgiftsberegning")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 407, 3
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


FradragIGrunnlaget._Automaton = _BuildAutomaton_39()


FradragIGrunnlagetForUtenlandsk._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "avgiftsfradragBeloep"),
        Beloep,
        scope=FradragIGrunnlagetForUtenlandsk,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 412, 3
        ),
    )
)

FradragIGrunnlagetForUtenlandsk._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "prosentsatsForAvgiftsberegning"),
        GrunnlagsprosentForUtenlandske,
        scope=FradragIGrunnlagetForUtenlandsk,
        location=pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 413, 3
        ),
    )
)


def _BuildAutomaton_40():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        FradragIGrunnlagetForUtenlandsk._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "avgiftsfradragBeloep")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 412, 3
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        FradragIGrunnlagetForUtenlandsk._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "prosentsatsForAvgiftsberegning")
        ),
        pyxb.utils.utility.Location(
            "C:\\users\\henrik\\Downloads\\a-melding_v2_1_xsd.xml", 413, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


FradragIGrunnlagetForUtenlandsk._Automaton = _BuildAutomaton_40()
