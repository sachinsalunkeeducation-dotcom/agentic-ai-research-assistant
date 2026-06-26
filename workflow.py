class Workflow:

    def __init__(self):

        self.batches = {

            "Batch 1": [
                "planner",
                "retriever"
            ],

            "Batch 2": [
                "opportunity",
                "risk"
            ],

            "Batch 3": [
                "writer"
            ]

        }

    def get_batches(self):

        return self.batches