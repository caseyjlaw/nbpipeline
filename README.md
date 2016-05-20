# nbpipeline: Stateful notebooks with interaction

Jupyter notebooks are a good way to document output from pipeline data analysis. The notebook can produce products or can hold visualizations to become a data product itself. In my pipelined analysis, there are batches of processing that might fall in either the nominal or interesting group (with maybe a 90%/10% split). How does one share the work of refining the analysis of the 10% of cases that are interesting?

`nbpipeline` is designed to allow groups to interact with pipeline notebooks and preserve (Python) state. To use this, crate a "base" notebook that functions like a pipeline script. Visualizations may be embedded, if one wishes the notebook to be a documented pipeline work flow or the notebook may produce secondary products outside the notebook. The base notebook can use the `nbpipeline` state object to create inputs to the pipeline and save their state. Once the base.ipynb is ready, it can be compiled with nbconvert into ipynb and html format. Multiple users may execute the notebook, modify pipeline parameters via the widgets, and update visualizations. 

Goals:
- allow nbconvert to compile a notebook, but also provides for interaction after that.
- use widgets as a simple way for people unfamiliar with Jupyter to update pipeline parameters.
- provides a simple example script to compile a base notebook and convert it to html.
