"""HTML slide show Exporter class"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from copy import deepcopy
from warnings import warn

from traitlets import Unicode, default

from .html import HTMLExporter

def prepare(nb):
    """Add some convenience metadata on cells for the slide template."""
    nb = deepcopy(nb)

    for cell in nb.cells:
        # Make sure every cell has a slide_type
        cell.metadata.slide_type = cell.metadata.get('slideshow', {}).get('slide_type', '-')

    # Find the first visible cell
    for index, cell in enumerate(nb.cells):
        if cell.metadata.slide_type not in {'notes', 'skip'}:
            cell.metadata.slide_type = 'slide'
            cell.metadata.slide_start = True
            cell.metadata.subslide_start = True
            first_slide_ix = index
            break
    else:
        raise ValueError("All cells are hidden, cannot create slideshow")

    in_fragment = False

    for index, cell in enumerate(nb.cells[first_slide_ix+1:],
                                 start=(first_slide_ix+1)):

        previous_cell = nb.cells[index - 1]

        # Slides are <section> elements in the HTML, subslides (the vertically
        # stacked slides) are also <section> elements inside the slides,
        # and fragments are <div>s within subslides. Subslide and fragment
        # elements can contain content:
        # <section>
        #   <section>
        #     (content)
        #     <div class="fragment">(content)</div>
        #   </section>
        # </section>

        # Get the slide type. If type is subslide or slide,
        # end the last slide/subslide/fragment as applicable.
        if cell.metadata.slide_type == 'slide':
            previous_cell.metadata.slide_end = True
            cell.metadata.slide_start = True
        if cell.metadata.slide_type in {'subslide', 'slide'}:
            previous_cell.metadata.fragment_end = in_fragment
            previous_cell.metadata.subslide_end = True
            cell.metadata.subslide_start = True
            in_fragment = False

        elif cell.metadata.slide_type == 'fragment':
            cell.metadata.fragment_start = True
            if in_fragment:
                previous_cell.metadata.fragment_end = True
            else:
                in_fragment  = True

    # The last cell will always be the end of a slide
    nb.cells[-1].metadata.fragment_end = in_fragment
    nb.cells[-1].metadata.subslide_end = True
    nb.cells[-1].metadata.slide_end = True

    return nb

class SlidesExporter(HTMLExporter):
    """Exports HTML slides with reveal.js"""

    reveal_url_prefix = Unicode(
        help="""The URL prefix for reveal.js.
        This can be a a relative URL for a local copy of reveal.js,
        or point to a CDN.

        For speaker notes to work, a local reveal.js prefix must be used.
        """
    ).tag(config=True)

    @default('reveal_url_prefix')
    def _reveal_url_prefix_default(self):
        if 'RevealHelpPreprocessor.url_prefix' in self.config:
            warn("Please update RevealHelpPreprocessor.url_prefix to "
                 "SlidesExporter.reveal_url_prefix in config files.")
            return self.config.RevealHelpPreprocessor.url_prefix
        return 'reveal.js'

    reveal_theme = Unicode('simple',
        help="""
        Name of the reveal.js theme to use.

        We look for a file with this name under `reveal_url_prefix`/css/theme/`reveal_theme`.css.

        https://github.com/hakimel/reveal.js/tree/master/css/theme has
        list of themes that ship by default with reveal.js.
        """
    ).tag(config=True)

    require_js_url = Unicode(
        "https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js",
        help="""
        URL to load require.js from.

        Defaults to loading from cdnjs.
        """
    ).tag(config=True)

    jquery_url = Unicode(
        "https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js",
        help="""
        URL to load jQuery from.

        Defaults to loading from cdnjs.
        """
    ).tag(config=True)

    font_awesome_url = Unicode(
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.1.0/css/font-awesome.css",
        help="""
        URL to load font awesome from.

        Defaults to loading from cdnjs.
        """
    ).tag(config=True)

    @default('file_extension')
    def _file_extension_default(self):
        return '.slides.html'

    @default('template_file')
    def _template_file_default(self):
        return 'slides_reveal'

    output_mimetype = 'text/html'

    def from_notebook_node(self, nb, resources=None, **kw):
        resources = self._init_resources(resources)
        if 'reveal' not in resources:
            resources['reveal'] = {}
        resources['reveal']['url_prefix'] = self.reveal_url_prefix
        resources['reveal']['theme'] = self.reveal_theme
        resources['reveal']['require_js_url'] = self.require_js_url
        resources['reveal']['jquery_url'] = self.jquery_url
        resources['reveal']['font_awesome_url'] = self.font_awesome_url

        nb = prepare(nb)

        return super(SlidesExporter, self).from_notebook_node(nb, resources=resources, **kw)
