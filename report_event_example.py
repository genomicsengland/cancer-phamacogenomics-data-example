from protocols.protocol_7_0.cva import ReportEvent, Phenotypes, ModeOfInheritance
from protocols.protocol_7_0.reports import VariantClassification, DrugResponseClassification, InterpretedGenome, \
    ReportVersionControl, SmallVariant, VariantCoordinates, Assembly, VariantConsequence, VariantCall, Zygosity, \
    Penetrance, VariantAttributes, AlleleFrequency, VariantIdentifiers, Identifier, Tier, \
    AlgorithmBasedVariantClassification, Actions, Therapy, DrugResponse

coordinates = VariantCoordinates(
    assembly=Assembly.GRCh38, reference='C', alternate='T', chromosome='1', position=97450058
)

marker_coordinates = VariantCoordinates(
    assembly=Assembly.GRCh38, reference='C', alternate='T', chromosome='1', position=97450058
)

therapy = Therapy(
    drugResponse=DrugResponse(
        TreatmentAgent="the drug",
        drugResponseClassification=DrugResponseClassification.increased_risk_of_toxicity),
    variantActionable=True,
    referenceUrl="",
    conditions=[]
)

actions = Actions(therapies=[therapy])

report_event = ReportEvent(
    reportEventId="someID",
    phenotypes=Phenotypes(),
    variantConsequences=[VariantConsequence(id="SO:0000162", name="splice_site")],
    modeOfInheritance=ModeOfInheritance.monoallelic,
    genomicEntities=[],
    actions=actions,
    penetrance=Penetrance.complete,
    groupOfVariants=12,
    tier=Tier.TIERA
)

marker_report_event = ReportEvent(
    reportEventId="otherID",
    phenotypes=Phenotypes(),
    variantConsequences=[VariantConsequence(id="SO:0000162", name="splice_site")],
    modeOfInheritance=ModeOfInheritance.monoallelic,
    genomicEntities=[],
    actions=actions,
    penetrance=Penetrance.complete,
    groupOfVariants=12,
    tier=Tier.TIERB,
    algorithmBasedVariantClassifications=AlgorithmBasedVariantClassification(
        algorithmName="pharmacogenomics-cancer",
        classification="marker"
    )

)

variant_call = VariantCall(
    participantId="personID",
    sampleId="sampleId",
    zygosity=Zygosity.heterozygous,
    depthAlternate=10,
    depthReference=5
)

marker_variant_call = VariantCall(
    participantId="personID",
    sampleId="sampleId",
    zygosity=Zygosity.heterozygous,
    depthAlternate=10,
    depthReference=5
)

allele_frequency = AlleleFrequency(
    study="study",
    population="populate",
    alternateFrequency=0.0003
)

marker_allele_frequency = AlleleFrequency(
    study="study",
    population="populate",
    alternateFrequency=0.0003
)

variant_identifiers = VariantIdentifiers(
    otherIds=[Identifier(
        source="PharmGKB",
        identifier="PA166153760"
    )]
)

variant_attributes = VariantAttributes(
    cdnaChanges=["c.1905+1G>A"],
    proteinChanges=["p.Ile560Ser"],
    alleleFrequencies=[allele_frequency],
    variantIdentifiers=variant_identifiers,
    additionalTextualVariantAnnotations={"genotype": "0/1"}
)

marker_variant_attributes = VariantAttributes(
    cdnaChanges=["c.whatever makes sense"],
    proteinChanges=[],
    alleleFrequencies=[marker_allele_frequency],
    variantIdentifiers=variant_identifiers,
    additionalTextualVariantAnnotations={"genotype": "1/1"}
)

variant = SmallVariant(
    variantCoordinates=coordinates,
    variantCalls=[variant_call],
    reportEvents=[report_event],
    variantAttributes=variant_attributes
)

marker_variant = SmallVariant(
    variantCoordinates=marker_coordinates,
    variantCalls=[marker_variant_call],
    reportEvents=[marker_report_event],
    variantAttributes=marker_variant_attributes
)

interpreted_genome = InterpretedGenome(
    versionControl=ReportVersionControl(),
    interpretationRequestId="1",
    interpretationRequestVersion=1,
    interpretationService="pharmacogenomics-cancer",
    variants=[variant, marker_variant],
    referenceDatabasesVersions={},
    softwareVersions={}
)


def validate(item):
    validation_object = item.validate(item.toJsonDict(), verbose=True)
    is_valid = validation_object.result
    if not is_valid:
        print(validation_object.messages)
    else:
        print("it was valid")


validate(variant_identifiers)
validate(report_event)
validate(variant_call)
validate(variant)
validate(variant_attributes)
validate(interpreted_genome)

validate(therapy)

print(therapy.validate_parts())