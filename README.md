# nbpipeline: Stateful notebooks with interaction

nbpipeline provides some simple features for using Jupyter notebooks for pipeline data analysis.
It was designed to allow multiple users to have multiple ways of using or interacting with a pipeline notebook.
nbpipeline assumes that a "base" notebook has been created that encompasses stages of a pipeline analysis
as cells to be executed. Visualizations may be embedded in the notebook to create a notebook-as-data-product,
or the notebook may produce secondary products outside the notebook.

While nbconvert can execute notebooks, I found a gap in my use case when I wanted to share notebooks
to allow collaborators a chance to interact with pipeline output. In some cases, collaborators wanted to
modify pipeline parameters and update visualizations. 

Managing a distributed collaboration required saving some state of the processing.
nbpipeline provides a way to preserve the state of processing (for Python kernel users). The state (e.g., a
parameter of the pipeline) can have a default defined or may be defined via interactive widgets (via ipywidgets),
which allows nbconvert to run automatically, but also provides for interaction after that.

A simple example script is provided to compile a base notebook and convert it to html. The ipynb version 
can be served by Jupyter to use widgets and interact, while the html is a static view of the default pipeline output.

