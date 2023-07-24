# CSS Cheat Sheet

This document is a quick reference for CSS. It is not meant to be a comprehensive guide, but rather a quick reference for small syntactical details that are easy to forget. Still, there are a few introductory sections to give a brief overview of the main structures of CSS. It is recommended that any CSS beginner starts by reviewing the [w3schools CSS Tutorial](https://www.w3schools.com/css/default.asp) and the [Mozilla Developer Network CSS Tutorial](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/What_is_CSS).

## Selectors

Selectors are used to select the elements that a rule applies to. Below we will review some of the most common types of selectors and provide some examples of helpful selectors.

### Classes

Classes are used to select elements with a specific class attribute. Classes are prefixed with a `.`. Multiple classes can be selected by separating them with a comma. They can be used in conjunction with other selectors to select elements with specific attributes, classes, and/or ids.

### IDs

IDs are used to select elements with a specific id attribute. IDs are prefixed with a `#`. Like classes, multiple IDs can be selected by separating them with a comma, and they can be used in conjunction with other selector types to select elements with specific attributes, classes, and/or ids.

### Examples

- `*` - Selects all elements
  - e.g. `* { color: red; }` will make all text red on the page
- `element` - Selects all elements of the given type (like `p`, `div`, `h1`, etc.)
  - e.g. `p { color: red; }` will make all text in paragraphs red
- `#id` - Selects the element with the given id
  - e.g. `#main { color: red; }` will make all text in the element with the id `main` red
- `.class` - Selects all elements with the given class
  - e.g. `.main { color: red; }` will make all text in elements with the class `main` red
- `element, element` - Selects all elements of the given type
  - e.g. `p, h1 { color: red; }` will make all text in paragraphs and headings red
- `element element` - Selects all elements that are descendants of the given type
  - e.g. `div p { color: red; }` will make all text in paragraphs that are descendants of a div red
- `element > element` - Selects all elements that are direct children of the given type
  - e.g. `div > p { color: red; }` will make all text in paragraphs that are direct children of a div red, so not just any paragraph that is a descendant of a div
- `element + element` - Selects all elements that are the next sibling of the given type
  - e.g. `div + p { color: red; }` will make all text in paragraphs that are the next sibling of a div red
- `element ~ element` - Selects all elements that are siblings of the given type
  - e.g. `div ~ p { color: red; }` will make all text in paragraphs that are siblings of a div red
- `[attribute]` - Selects all elements that have the given attribute
  - e.g. `[href] { color: red; }` will make all text in elements that have an href attribute red
- `[attribute=value]` - Selects all elements that have the given attribute with the given value
  - e.g. `[href="http://www.google.com"] { color: red; }` will make all text in elements that have an href attribute with the value `http://www.google.com` red
- `:link` - Selects all links that have not been visited
  - e.g. `a:link { color: red; }` will make all text in links that have not been visited red
- `:visited` - Selects all links that have been visited
  - e.g. `a:visited { color: red; }` will make all text in links that have been visited red
- `:active` - Selects the active link
  - e.g. `a:active { color: red; }` will make all text in the active link red
- `:hover` - Selects all links that are being hovered over
  - e.g. `a:hover { color: red; }` will make all text in links that are being hovered over red
- `:focus` - Selects the element that has focus
  - e.g. `input:focus { color: red; }` will make all text in the input that has focus red
- `:first-child` - Selects all elements that are the first child of their parent
  - e.g. `p:first-child { color: red; }` will make all text in paragraphs that are the first child of their parent red
- `:last-child` - Selects all elements that are the last child of their parent
  - e.g. `p:last-child { color: red; }` will make all text in paragraphs that are the last child of their parent red
- `:only-child` - Selects all elements that are the only child of their parent
  - e.g. `p:only-child { color: red; }` will make all text in paragraphs that are the only child of their parent red
- `:first-of-type` - Selects all elements that are the first of their type
  - e.g. `p:first-of-type { color: red; }` will make all text in paragraphs that are the first of their type red
- `:last-of-type` - Selects all elements that are the last of their type
  - e.g. `p:last-of-type { color: red; }` will make all text in paragraphs that are the last of their type red
- `:only-of-type` - Selects all elements that are the only of their type
  - e.g. `p:only-of-type { color: red; }` will make all text in paragraphs that are the only of their type red
- `:empty` - Selects all elements that have no children
  - e.g. `p:empty { color: red; }` will make all text in paragraphs that have no children red
- `:root` - Selects the document's root element
  - e.g. `:root { color: red; }` will make all text in the document's root element red
- `:target` - Selects the current active #id
  - e.g. `#news:target { color: red; }` will make all text in the element with the id `news` red if the url contains `#news`
- `:enabled` - Selects all enabled elements
  - e.g. `input:enabled { color: red; }` will make all text in enabled inputs red
- `:disabled` - Selects all disabled elements
  - e.g. `input:disabled { color: red; }` will make all text in disabled inputs red
- `:checked` - Selects all checked elements
  - e.g. `input:checked { color: red; }` will make all text in checked inputs red
- `:not(selector)` - Selects all elements that are not matched by the given selector
  - e.g. `p:not(.intro) { color: red; }` will make all text in paragraphs that do not have the class `intro` red
- `::selection` - Selects the portion of an element that is selected by a user
  - e.g. `::selection { color: red; }` will make all text in the selected portion of an element red

## Pseudo-classes

For more information on pseudo-classes, see [this link](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes).

- `:nth-child(n)` - Selects every element that is the nth child of its parent
  - e.g. `p:nth-child(2) { color: red; }` will make all text in the second paragraph red
- `:nth-last-child(n)` - Selects every element that is the nth child of its parent, counting from the last one
  - e.g. `p:nth-last-child(2) { color: red; }` will make all text in the second to last paragraph red
- `:nth-of-type(n)` - Selects every element that is the nth of its type
  - e.g. `p:nth-of-type(2) { color: red; }` will make all text in the second paragraph of its type red
- `:nth-last-of-type(n)` - Selects every element that is the nth of its type, counting from the last one
  - e.g. `p:nth-last-of-type(2) { color: red; }` will make all text in the second to last paragraph of its type red
- `:nth-child(odd)` - Selects every odd element, same as `:nth-child(2n+1)`
  - e.g. `p:nth-child(odd) { color: red; }` will make all text in odd paragraphs red
- `:nth-child(even)` - Selects every even element, same as `:nth-child(2n)`
  - e.g. `p:nth-child(even) { color: red; }` will make all text in even paragraphs red

## Pseudo-elements

For more information on pseudo-elements, see [this page](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements).

- `::first-letter` - Selects the first letter of an element
  - e.g. `p::first-letter { color: red; }` will make the first letter of all paragraphs red
- `::first-line` - Selects the first line of an element
  - e.g. `p::first-line { color: red; }` will make the first line of all paragraphs red
- `::before` - Inserts content before an element
  - e.g. `p::before { content: "Hello "; }` will insert "Hello " before all paragraphs
- `::after` - Inserts content after an element
  - e.g. `p::after { content: " Hello"; }` will insert " Hello" after all paragraphs
- `::selection` - Selects the portion of an element that is selected by a user
  - e.g. `::selection { color: red; }` will make all text in the selected portion of an element red
- `::placeholder` - Selects the placeholder text of an element
  - e.g. `input::placeholder { color: red; }` will make the placeholder text of all inputs red
- `::backdrop` - Selects the backdrop of an element
  - e.g. `dialog::backdrop { color: red; }` will make the backdrop of all dialogs red
- `::marker` - Selects the list item marker of an element
  - e.g. `li::marker { color: red; }` will make the list item marker of all list items red
- `::spelling-error` - Selects misspelled words
  - e.g. `::spelling-error { color: red; }` will make all misspelled words red
- `::grammar-error` - Selects grammatically incorrect words
  - e.g. `::grammar-error { color: red; }` will make all grammatically incorrect words red
- `::cue` - Selects the cue of a media element
  - e.g. `video::cue { color: red; }` will make the cue of all videos red
- `::cue-region` - Selects the cue region of a media element
  - e.g. `video::cue-region { color: red; }` will make the cue region of all videos red
- `::part(name)` - Selects the part of an element
  - e.g. `p::part(name) { color: red; }` will make the part of all paragraphs with the name `name` red
- `::theme(name)` - Selects the theme of an element
  - e.g. `p::theme(name) { color: red; }` will make the theme of all paragraphs with the name `name` red

## Common CSS Properties

For more information on CSS properties, see [this link](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference).
