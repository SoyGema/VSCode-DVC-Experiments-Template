## [PIPELINE STAGES](https://dvc.org/doc/user-guide/pipelines/defining-pipelines#defining-pipelines)

# What are stages ?

## Each one of the data workflows that
## we reproduce reliably to ensure consistent results.
## Might include Feature engineering , train , evaluation

# How are stages defined ?

## The [stages](https://dvc.org/doc/user-guide/project-structure/dvcyaml-files#stage-entries) entries are
##    cmd: python path that wraps executable shell command.
##    params: loads parameters. Related to params.yaml file
##    deps: dependencies. Might contain Stages that might be executed first
##    outs: outputs, they can be data or even the model



stages:
    load:
        cmd: 
        params:
        outs:

    normalization:
        cmd:
        params:
        outs:
    
    train


    evaluate

    