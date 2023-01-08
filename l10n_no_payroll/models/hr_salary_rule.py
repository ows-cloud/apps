from odoo import fields, models


class SalaryRule(models.Model):
    _inherit = "hr.salary.rule"

    json = fields.Serialized()
    l10n_no_BeregnAga = fields.Selection(
        string="Beregn arbeidsgiveravgift",
        sparse="json",
        selection=[
            ("loennOgGodtgjoerelse", "Lønn og godtgjørelse"),
            ("tilskuddOgPremieTilPensjon", "Tilskudd og premie til pensjon"),
            ("fradragIGrunnlagetForSone", "Fradrag"),
        ],
    )
    l10n_no_BeregnFP = fields.Boolean(
        string="Beregn feriepenger",
        sparse="json",
        selection=[

        ],
    )
    l10n_no_BeregnTrekk = fields.Selection(
        string="Beregn skattetrekk",
        sparse="json",
        selection=[
            ("tabelltrekk", "Tabelltrekk"),
            ("prosenttrekk", "Prosenttrekk"),
            ("skattepliktUtenTrekk", "Ingen trekk, men skatteplikt"),
        ],
    )
    l10n_no_Fordel = fields.Selection(
        string="Fordel",
        sparse="json",
        selection=[
            ("kontantytelse", "kontantytelse"),
            ("naturalytelse", "naturalytelse"),
            ("utgiftsgodtgjoerelse", "utgiftsgodtgjoerelse"),
        ],
    )
    l10n_no_Forskuddstrekkbeskrivelse = fields.Selection(
        string="Forskuddstrekkbeskrivelse",
        sparse="json",
        selection=[
            ("betaltTrygdeavgiftTilJanMayen", "betaltTrygdeavgiftTilJanMayen"),
            ("janMayenOgBilandene", "janMayenOgBilandene"),
            ("kildeskattPaaPensjon", "kildeskattPaaPensjon"),
            ("svalbard", "svalbard"),
            ("barnepensjon", "barnepensjon"),
            ("refusjonNegativeEtteroppgjoer", "refusjonNegativeEtteroppgjoer"),
            ("refusjonNegativeEtteroppgjoerKildeskatt", "refusjonNegativeEtteroppgjoerKildeskatt"),
            ("refusjonNegativeEtteroppgjoerSvalbard", "refusjonNegativeEtteroppgjoerSvalbard"),
        ],
    )
    l10n_no_Loennsbeskrivelse = fields.Selection(
        string="Loennsbeskrivelse",
        sparse="json",
        selection=[
            ("administrativForpleining", "administrativForpleining"),
            ("aksjerGrunnfondsbevisTilUnderkurs", "aksjerGrunnfondsbevisTilUnderkurs"),
            ("annet", "annet"),
            ("arbeidsoppholdKost", "arbeidsoppholdKost"),
            ("arbeidsoppholdLosji", "arbeidsoppholdLosji"),
            ("bedriftsbarnehageplass", "bedriftsbarnehageplass"),
            ("beregnetSkatt", "beregnetSkatt"),
            ("besoeksreiserHjemmetAnnet", "besoeksreiserHjemmetAnnet"),
            ("besoeksreiserHjemmetKilometergodtgjoerelseBil", "besoeksreiserHjemmetKilometergodtgjoerelseBil"),
            ("besoeksreiserHjemmetKost", "besoeksreiserHjemmetKost"),
            ("bil", "bil"),
            ("bolig", "bolig"),
            ("bonus", "bonus"),
            ("bonusFraForsvaret", "bonusFraForsvaret"),
            ("elektroniskKommunikasjon", "elektroniskKommunikasjon"),
            ("fastBilgodtgjoerelse", "fastBilgodtgjoerelse"),
            ("fastTillegg", "fastTillegg"),
            ("fastloenn", "fastloenn"),
            ("feriepenger", "feriepenger"),
            ("flyttegodtgjoerelse", "flyttegodtgjoerelse"),
            ("fondForIdrettsutoevere", "fondForIdrettsutoevere"),
            ("friTransport", "friTransport"),
            ("godtgjoerelseSaeravtaleUtland", "godtgjoerelseSaeravtaleUtland"),
            ("helligdagstillegg", "helligdagstillegg"),
            ("hyretillegg", "hyretillegg"),
            ("ikkeSkattepliktigLoennFraUtenlandskDiplomKonsulStasjon", "ikkeSkattepliktigLoennFraUtenlandskDiplomKonsulStasjon"),
            ("kapitalInntekt", "kapitalInntekt"),
            ("kilometergodtgjoerelseAndreFremkomstmidler", "kilometergodtgjoerelseAndreFremkomstmidler"),
            ("kilometergodtgjoerelseBil", "kilometergodtgjoerelseBil"),
            ("kilometergodtgjoerelseElBil", "kilometergodtgjoerelseElBil"),
            ("kilometergodtgjoerelsePassasjertillegg", "kilometergodtgjoerelsePassasjertillegg"),
            ("kommunalOmsorgsloennOgFosterhjemsgodtgjoerelse", "kommunalOmsorgsloennOgFosterhjemsgodtgjoerelse"),
            ("kompensasjonstilleggBolig", "kompensasjonstilleggBolig"),
            ("kostDager", "kostDager"),
            ("kostDoegn", "kostDoegn"),
            ("kostbesparelseIHjemmet", "kostbesparelseIHjemmet"),
            ("losji", "losji"),
            ("losjiEgenBrakkeCampingvogn", "losjiEgenBrakkeCampingvogn"),
            ("loennForBarnepassIBarnetsHjem", "loennForBarnepassIBarnetsHjem"),
            ("loennTilPrivatpersonerForArbeidIHjemmet", "loennTilPrivatpersonerForArbeidIHjemmet"),
            ("loennUtbetaltAvVeldedigEllerAllmennyttigInstitusjonEllerOrganisasjon", "loennUtbetaltAvVeldedigEllerAllmennyttigInstitusjonEllerOrganisasjon"),
            ("loennUtenlandskArtist", "loennUtenlandskArtist"),
            ("opsjoner", "opsjoner"),
            ("overtidsgodtgjoerelse", "overtidsgodtgjoerelse"),
            ("overtidsmat", "overtidsmat"),
            ("reiseAnnet", "reiseAnnet"),
            ("reiseKost", "reiseKost"),
            ("reiseKostMedOvernatting", "reiseKostMedOvernatting"),
            ("reiseKostMedOvernattingPaaHotell", "reiseKostMedOvernattingPaaHotell"),
            ("reiseKostMedOvernattingPaaHotellBeordringUtover28Doegn", "reiseKostMedOvernattingPaaHotellBeordringUtover28Doegn"),
            ("reiseKostMedOvernattingPaaHybelBrakkePrivat", "reiseKostMedOvernattingPaaHybelBrakkePrivat"),
            ("reiseKostMedOvernattingPaaPensjonat", "reiseKostMedOvernattingPaaPensjonat"),
            ("reiseKostMedOvernattingTilLangtransportsjaafoerForKjoeringIUtlandet", "reiseKostMedOvernattingTilLangtransportsjaafoerForKjoeringIUtlandet"),
            ("reiseKostUtenOvernatting", "reiseKostUtenOvernatting"),
            ("reiseLosji", "reiseLosji"),
            ("reiseNattillegg", "reiseNattillegg"),
            ("rentefordelLaan", "rentefordelLaan"),
            ("skattefriErstatning", "skattefriErstatning"),
            ("skattefrieUtbetalinger", "skattefrieUtbetalinger"),
            ("skattepliktigDelForsikringer", "skattepliktigDelForsikringer"),
            ("sluttvederlag", "sluttvederlag"),
            ("smusstillegg", "smusstillegg"),
            ("stipend", "stipend"),
            ("styrehonorarOgGodtgjoerelseVerv", "styrehonorarOgGodtgjoerelseVerv"),
            ("tilskuddBarnehageplass", "tilskuddBarnehageplass"),
            ("timeloenn", "timeloenn"),
            ("uregelmessigeTilleggKnyttetTilArbeidetTid", "uregelmessigeTilleggKnyttetTilArbeidetTid"),
            ("uregelmessigeTilleggKnyttetTilIkkeArbeidetTid", "uregelmessigeTilleggKnyttetTilIkkeArbeidetTid"),
            ("loennEtterDoedsfall", "loennEtterDoedsfall"),
            ("yrkebilTjenestligbehovKilometer", "yrkebilTjenestligbehovKilometer"),
            ("yrkebilTjenestligbehovListepris", "yrkebilTjenestligbehovListepris"),
            ("innbetalingTilUtenlandskPensjonsordning", "innbetalingTilUtenlandskPensjonsordning"),
            ("loennTilVergeFraFylkesmannen", "loennTilVergeFraFylkesmannen"),
            ("trekkILoennForFerie", "trekkILoennForFerie"),
            ("betaltUtenlandskSkatt", "betaltUtenlandskSkatt"),
            ("honorarAkkordProsentProvisjon", "honorarAkkordProsentProvisjon"),
        ],
    )
    l10n_no_RegelType = fields.Selection(
        string="Regeltype",
        sparse="json",
        selection=[
            ("loennsinntekt", "Lønnsinntekt"),
            ("ytelseFraOffentlige", "Ytelser fra det offentlige"),
            ("pensjonEllerTrygd", "Pensjon eller trygd"),
            ("naeringsinntekt", "Naeringsinntekt"),
            ("fradrag", "Fradrag"),
            ("forskuddstrekk", "Forskuddstrekk"),
        ],
    )
    l10n_no_SkatteOgAvgiftsregel = fields.Selection(
        string="SkatteOgAvgiftsregel",
        sparse="json",
        selection=[
            ("janMayenOgBilandene", "janMayenOgBilandene"),
            ("kildeskattPaaPensjoner", "kildeskattPaaPensjoner"),
            ("nettoloenn", "nettoloenn"),
            ("svalbard", "svalbard"),
            ("saerskiltFradragForSjoefolk", "saerskiltFradragForSjoefolk"),
            ("nettoloennForSjoefolk", "nettoloennForSjoefolk"),
            ("skattefriOrganisasjon", "skattefriOrganisasjon"),
        ],
    )
