import trafilatura 

def html_remover(html_code):
    extracted=trafilatura.extract(
        html_code,
        include_comments=False,
        include_tables=False,
        favor_recall=False
    )
    return extracted