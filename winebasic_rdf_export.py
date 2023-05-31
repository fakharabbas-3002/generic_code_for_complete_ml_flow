# Imports ----------------------------------------------------------------------
from data_catalog._rdf_profile_creator import exportStatisticsAsRDF
from dataset import loadDataset
from util import exportDictionaryAsJSON

# Workflow steps ---------------------------------------------------------------


def exampleWorkflow():

    dataset = loadDataset("WhiteWineQuality")
    print(exportDictionaryAsJSON(dataset.getProfile()))

    dataset = dataset.sample(10000)

    print(exportDictionaryAsJSON(dataset.getProfile()))

    print(exportStatisticsAsRDF(dataset))


if __name__ == "__main__":
    exampleWorkflow()
