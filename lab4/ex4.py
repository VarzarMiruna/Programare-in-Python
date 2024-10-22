def build_xml_element(tag, content, **kwargs):
    attributes = " ".join(f'{key}="{value}"' for key, value in kwargs.items())
    complete = f'<{tag} {attributes}>{content}</{tag}>'
    return complete


result = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(result)

#string = "<a href="http://python.org "_class = " my-link " id = " someid "> Hello there </a>"

