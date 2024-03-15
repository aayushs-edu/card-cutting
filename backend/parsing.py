import docx

class Card:
    def __init__(self, title):
        self.sources : list[docx.text.paragraph.Paragraph] = []
        self.bodies : list[docx.text.paragraph.Paragraph]  = []
        self.title = title

    def set_tagline(self, tagline):
        self.tagline = tagline

    def add_evidence(self, source : docx.text.paragraph.Paragraph, body : docx.text.paragraph.Paragraph):
        self.sources.append(source)
        new_body = Body(body)

        self.bodies.append(new_body)

class Body:
    def __init__(self, body : docx.text.paragraph.Paragraph) -> None:
        self.body = body
        self.text = body.text
        self.runs = body.runs
    
    def parse(self):
        self.underlined = []
        self.normal = []
        self.highlighted = []
        for run in self.runs:
            style = run.style.name
            if not run.style or not run.text: continue
            if style == 'Style Bold Underline':
                self.underlined.append(run.text)
            elif style == 'Emphasis' or run.font.highlight_color != None:
                self.highlighted.append(run.text)
            else:
                self.normal.append(run.text)
