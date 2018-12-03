from protocols.protocol_7_0.cva import EvidenceEntryAndVariants, VariantsCoordinates, Assembly, Property, \
    ModeOfInheritance, Penetrance, HeritableTrait
from protocols.protocol_7_0.opencb import GenomicFeature, FeatureTypes, VariantClassification, EvidenceEntry, \
    EvidenceSource
from protocols.protocol_7_0.reports import DrugResponseClassification
from protocols.protocol_7_0.reports import VariantCoordinates, Actions, Therapy, DrugResponse

coordinates = VariantCoordinates(
    assembly=Assembly.GRCh38, reference='C', alternate='T', chromosome='1', position=97450058
)

marker_coordinates = VariantCoordinates(
    assembly=Assembly.GRCh38, reference='C', alternate='T', chromosome='1', position=97450058
)

genomic_feature = GenomicFeature(
    featureType=FeatureTypes.transcript,
    ensemblId="ENST00000370192.7"
)


actions = Actions(therapies=
    Therapy(drugResponse=
        DrugResponse(
            TreatmentAgent="the drug",
            drugResponseClassification=DrugResponseClassification.increased_risk_of_toxicity
        ),
        variantActionable=True,
        referenceUrl="https://something.com/db.html"
    )
)


source = EvidenceSource(
    date="today",
    name="genomics-england-phamacogenomics",
    version="v1.0"
)


pharmGKB_id = Property(
    id="data:2649",
    name="PharmGKB ID",
    value="PA166153760"
)


instance = EvidenceEntryAndVariants(
    evidenceEntry=EvidenceEntry(
        source=source,
        ethnicity='Z',
        genomicFeatures=[genomic_feature],
        heritable_trait=[],
        penetrance=Penetrance.complete,
        additionalProperties=[pharmGKB_id]
    ),
    variantsCoordinates=VariantsCoordinates(variants=[coordinates]),
    markersCoordinates=VariantsCoordinates(variants=[marker_coordinates]),  # we will add this
    actions=actions  # requires a model change
)


validation_object = instance.validate(instance.toJsonDict(), verbose=True)
is_valid = validation_object.result
if not is_valid:
    print validation_object.messages
else:
    print("it was valid")


# predicted consequences come from the variant annotation in cancer teiring so I don't think we need them.
# same for population frequencies
# same for germline frequencies
# read depth from the VCF
# same for genomtype

