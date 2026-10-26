{% if snake_case_section_title not in design.sections.hide_titles_for %}
== {{section_title}}
{% else %}
#heading(level: 2)[]
{% endif %}
{% if entry_type in ["ReversedNumberedEntry"] %}

#reversed-numbered-entries(
  [
{% endif %}
