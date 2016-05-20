# nbpipeline: Stateful notebooks with interaction

Jupyter notebooks are a good way to document output from pipeline data analysis. The notebook can produce products or can hold visualizations to become a data product itself. In my pipelined analysis, there are batches of processing that might fall in either the nominal or interesting group (with maybe a 90%/10% split). How does one share the work of inspecting the 10% of cases that are interesting?

`nbpipeline` is designed to allow groups to interact with notebooks by preserving (Python) state for a notebook pipeline. This assumes that a "base" notebook has been created that functions like a pipeline script. Visualizations may be embedded, if one wishes the notebook to be a documented pipeline work flow or the notebook may produce secondary products outside the notebook. Multiple users may execute the notebook, modify pipeline parameters as ipywidgets, and update visualizations. 

Goals:
- allow nbconvert to compile a notebook, but also provides for interaction after that.
- use widgets for simple interaction for people unfamiliar with Jupyter.
- provides a simple example script to compile a base notebook and convert it to html.
