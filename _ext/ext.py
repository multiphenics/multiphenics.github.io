import os
import subprocess
from docutils import nodes
from docutils.parsers.rst import Directive
from tutorials import tutorials
import sphinx_material

class Tutorials(Directive):

    def run(self):
        output = list()
        # General text
        intro = f"""
<p>
<b>multiphenicsx</b> is accompanied by several tutorials, that can be run on JupyterLab through a local installation of the library, or on cloud computing platforms such as Google Colab and Kaggle.
</p>
"""
        output.append(nodes.raw(text=intro, format="html"))
        # Tutorials
        cards = list()
        for num in tutorials.keys():
            data = tutorials[num]
            buttons = ""
            if "steps" in data:
                steps = data["steps"]
                for step_description in steps:
                    step_files = steps[step_description]
                    if len(step_files) == 1:
                        buttons += self._button(step_description, step_files)
                    else:
                        buttons += self._dropdown(step_description, step_files)

            card_num = self._card(
                num=num,
                title=data["title"],
                description=data["description"],
                buttons=buttons
            )
            cards.append(card_num)
        output.append(nodes.raw(text=self._card_container(cards), format="html"))
        return output

    @staticmethod
    def _card_container(cards):
        card_container = """
<div class="tutorial-container">
  <div class="tutorial-row">
"""
        for card in cards:
            card_container += """
    <div class="tutorial-column">
""" + card + """
    </div>
"""
        card_container += """
  </div>
</div>
"""
        return card_container

    @staticmethod
    def _card(num, title, description, buttons):
        return f"""
<div class="tutorial-card">
  <div class="tutorial-number">
    {num}
  </div>
  <div class="tutorial-content">
    <h3 class="tutorial-title">
      {title}
    </h3>
    <div class="tutorial-description">
      <p>{description}</p>
    </div>
    <div class="tutorial-buttons">
      {buttons}
    </div>
  </div>
</div>
"""

    @classmethod
    def _dropdown(cls, step_description, step_title_url):
        dropdown = f"""
<div id="tutorial-dropdown-{cls._dropdown_id}" class="jq-dropdown jq-dropdown-tip">
    <ul class="jq-dropdown-menu">
"""
        for (title, url) in step_title_url.items():
            dropdown += f"""
        <li><a href="{url}" target="_blank">{title}</a></li>
"""
        dropdown += f"""
    </ul>
</div>
<div class="tutorial-button" data-jq-dropdown="#tutorial-dropdown-{cls._dropdown_id}">{step_description}</div>
"""
        cls._dropdown_id += 1
        return dropdown

    _dropdown_id = 1

    @classmethod
    def _button(cls, step_description, step_title_url):
        assert len(step_title_url) == 1
        title = list(step_title_url.keys())[0]
        url = step_title_url[title]
        assert step_description == "-"
        return f"""
    <a href="{url}" target="_blank"><div class="tutorial-button">{title}</div></a>
"""

def on_build_finished(app, exc):
    if exc is None and app.builder.format == "html":
        # Unescape at symbol
        subprocess.run(
            "find " + str(app.outdir) + " -type f -not -path '*/\.git/*' -exec sed -i 's/%40/@/g' {} +",
            shell=True)
        # Mark current page as active
        subprocess.run(
            "find " + str(app.outdir) + " -type f -not -path '*/\.git/*' -exec sed -i 's/"
            + '<li class="md-tabs__item"><a href="#" class="md-tabs__link">'
            + "/"
            + '<li class="md-tabs__item md-tabs__item_current"><a href="#" class="md-tabs__link">'
            + "/g' {} +",
            shell=True)
        # Disable going to submenus on mobile
        subprocess.run(
            "find " + str(app.outdir) + " -type f -not -path '*/\.git/*' -exec sed -i 's/"
            + 'id="__toc"'
            + "/"
            + 'id="__toc_disabled"'
            + "/g' {} +",
            shell=True)
        # Add further SEO tags
        seo_head = """
<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "@type": "SoftwareApplication",
  "name": "multiphenicsx - easy prototyping of multiphysics problems in FEniCSx",
  "description": "multiphenicsx is a python library that aims at providing tools in **FEniCSx** for an easy prototyping of multiphysics problems on conforming meshes. multiphenicsx is currently developed at Università Cattolica del Sacro Cuore by Dr. Francesco Ballarin.",
  "keywords": "multiphenicsx, multiphenics, FEniCSx, FEniCS, finite element, multiphysics",
  "softwareHelp": "https://multiphenics.github.io/",
  "operatingSystem": "Linux",
  "applicationCategory": "Simulation",
  "inLanguage": "en",
  "license": "https://opensource.org/licenses/lgpl-3.0",
  "url": "https://github.com/multiphenics/multiphenicsx"
}
</script>

<meta property="og:title" content="multiphenicsx - easy prototyping of multiphysics problems in FEniCSx" />
<meta property="og:description" content="multiphenicsx is a python library that aims at providing tools in **FEniCSx** for an easy prototyping of multiphysics problems on conforming meshes. multiphenicsx is currently developed at Università Cattolica del Sacro Cuore by Dr. Francesco Ballarin." />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="multiphenicsx" />
<meta property="og:url" content="https://multiphenics.github.io/" />
<meta property="og:image" content="https://multiphenics.github.io/_images/multiphenicsx-logo.png" />
"""
        index = os.path.join(app.outdir, "index.html")
        with open(index, "r") as f:
            index_content = f.read()
        index_content = index_content.replace("<head>", "<head>\n" + seo_head)
        with open(index, "w") as f:
            f.write(index_content)
        # Get tutorial nbconvert html files from git, if not already available
        for num in tutorials.keys():
            if "steps" in tutorials[num]:
                for step_files in tutorials[num]["steps"].values():
                    for url in step_files.values():
                        if not os.path.exists(os.path.join(app.outdir, url)):
                            html_generated = subprocess.run(
                                "mkdir -p " + os.path.dirname(os.path.join(app.outdir, url)) + " && " +
                                "git show origin/gh-pages:" + url + "> " + os.path.join(app.outdir, url),
                                shell=True, capture_output=True)
                            if html_generated.returncode != 0:
                                raise RuntimeError(
                                    "HTML generation of " + url + " not found\n"
                                    + "stdout contains " + html_generated.stdout.decode() + "\n"
                                    + "stderr contains " + html_generated.stderr.decode() + "\n")


create_sitemap_bak = sphinx_material.create_sitemap
def create_sitemap(app, exc):
    create_sitemap_bak(app, exc)
    if exc is None and app.builder.format == "html":
        # Add version and encoding to the top of sitemap.xml
        subprocess.run(
            "sed -i '1s/^/<?xml version=\"1.0\" encoding=\"UTF-8\"?>/' " + os.path.join(app.outdir, "sitemap.xml"),
            shell=True)
        # Remove trailing index.html from sitemap.xml
        subprocess.run(
            "sed -i 's|/index.html||g' " + os.path.join(app.outdir, "sitemap.xml"),
            shell=True)
sphinx_material.create_sitemap = create_sitemap


def setup(app):
    app.add_directive("tutorials", Tutorials)
    app.connect("build-finished", on_build_finished)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": False,
    }
