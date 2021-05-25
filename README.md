# UESBOT

Simple demo bot to follow a enrollment process.

# Prerequisites


## Virtual Environment

Create a venv using the following command:

`python3 -m venv env`

This will generate a env directory inside project's root folder.

Start the environment using:

`source env/bin/activate`

Now, install the dependencies:

`pip install -r requirements.txt`

This will take some time to complete, be patient


# Train model

We need to train the model so we can use it on the application:

`rasa train`

This will generate a models directory containing a `tar.gz` file. We need to "unzip" this folder.

The following structure is presented:
```
├── core
│   ├── domain.json
│   ├── domain.yml
│   ├── metadata.json
│   ├── policy_0_MemoizationPolicy
│   │   ├── featurizer.json
│   │   └── memorized_turns.json
│   └── policy_1_TEDPolicy
│       ├── checkpoint
│       ├── featurizer.json
│       ├── ted_policy.data_example.pkl
│       ├── ted_policy.entity_tag_specs.json
│       ├── ted_policy.fake_features.pkl
│       ├── ted_policy.label_data.pkl
│       ├── ted_policy.meta.pkl
│       ├── ted_policy.priority.pkl
│       ├── ted_policy.tf_model.data-00000-of-00001
│       └── ted_policy.tf_model.index
├── fingerprint.json
└── nlu
    ├── checkpoint
    ├── component_1_RegexFeaturizer.patterns.pkl
    ├── component_1_RegexFeaturizer.vocabulary_stats.pkl
    ├── component_2_LexicalSyntacticFeaturizer.feature_to_idx_dict.pkl
    ├── component_3_CountVectorsFeaturizer.pkl
    ├── component_4_CountVectorsFeaturizer.pkl
    ├── component_5_DIETClassifier.data_example.pkl
    ├── component_5_DIETClassifier.entity_tag_specs.json
    ├── component_5_DIETClassifier.index_label_id_mapping.json
    ├── component_5_DIETClassifier.label_data.pkl
    ├── component_5_DIETClassifier.tf_model.data-00000-of-00001
    ├── component_5_DIETClassifier.tf_model.index
    └── metadata.json

```

We need to copy the following route: `models/<what ever your timestamp model folder is>/nlu`

and paste on `App/Translator.py`:

```
    model_path = "models/<what ever your timestamp model folder is>/nlu"
    interpreter = None
    dispatcher = Dispatcher()
```

## Running

To run the app type the following (using the virtual env created before):

`python App/main.py`

and following the instructions.

# Aditional info (Optional)

To test the model you can run:

`rasa test`


