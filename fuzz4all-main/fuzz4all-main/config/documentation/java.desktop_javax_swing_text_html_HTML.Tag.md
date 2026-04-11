# Class HTML.Tag

**Source:** `java.desktop\javax\swing\text\html\HTML.Tag.html`

### Class Description

```java
public static class
HTML.Tag

extends
Object
```

Typesafe enumeration for an HTML tag. Although the
set of HTML tags is a closed set, we have left the
set open so that people can add their own tag types
to their custom parser and still communicate to the
reader.

**Direct Known Subclasses:** HTML.UnknownTag

---

### Field Details

#### public static final
HTML.Tag
A

Tag <a>

---

#### public static final
HTML.Tag
ADDRESS

Tag <address>

---

#### public static final
HTML.Tag
APPLET

Tag <applet>

---

#### public static final
HTML.Tag
AREA

Tag <area>

---

#### public static final
HTML.Tag
B

Tag <b>

---

#### public static final
HTML.Tag
BASE

Tag <base>

---

#### public static final
HTML.Tag
BASEFONT

Tag <basefont>

---

#### public static final
HTML.Tag
BIG

Tag <big>

---

#### public static final
HTML.Tag
BLOCKQUOTE

Tag <blockquote>

---

#### public static final
HTML.Tag
BODY

Tag <body>

---

#### public static final
HTML.Tag
BR

Tag <br>

---

#### public static final
HTML.Tag
CAPTION

Tag <caption>

---

#### public static final
HTML.Tag
CENTER

Tag <center>

---

#### public static final
HTML.Tag
CITE

Tag <cite>

---

#### public static final
HTML.Tag
CODE

Tag <code>

---

#### public static final
HTML.Tag
DD

Tag <dd>

---

#### public static final
HTML.Tag
DFN

Tag <dfn>

---

#### public static final
HTML.Tag
DIR

Tag <dir>

---

#### public static final
HTML.Tag
DIV

Tag <div>

---

#### public static final
HTML.Tag
DL

Tag <dl>

---

#### public static final
HTML.Tag
DT

Tag <dt>

---

#### public static final
HTML.Tag
EM

Tag <em>

---

#### public static final
HTML.Tag
FONT

Tag <font>

---

#### public static final
HTML.Tag
FORM

Tag <form>

---

#### public static final
HTML.Tag
FRAME

Tag <frame>

---

#### public static final
HTML.Tag
FRAMESET

Tag <frameset>

---

#### public static final
HTML.Tag
H1

Tag <h1>

---

#### public static final
HTML.Tag
H2

Tag <h2>

---

#### public static final
HTML.Tag
H3

Tag <h3>

---

#### public static final
HTML.Tag
H4

Tag <h4>

---

#### public static final
HTML.Tag
H5

Tag <h5>

---

#### public static final
HTML.Tag
H6

Tag <h6>

---

#### public static final
HTML.Tag
HEAD

Tag <head>

---

#### public static final
HTML.Tag
HR

Tag <hr>

---

#### public static final
HTML.Tag
HTML

Tag <html>

---

#### public static final
HTML.Tag
I

Tag <i>

---

#### public static final
HTML.Tag
IMG

Tag <img>

---

#### public static final
HTML.Tag
INPUT

Tag <input>

---

#### public static final
HTML.Tag
ISINDEX

Tag <isindex>

---

#### public static final
HTML.Tag
KBD

Tag <kbd>

---

#### public static final
HTML.Tag
LI

Tag <li>

---

#### public static final
HTML.Tag
LINK

Tag <link>

---

#### public static final
HTML.Tag
MAP

Tag <map>

---

#### public static final
HTML.Tag
MENU

Tag <menu>

---

#### public static final
HTML.Tag
META

Tag <meta>

---

#### public static final
HTML.Tag
NOFRAMES

Tag <noframes>

---

#### public static final
HTML.Tag
OBJECT

Tag <object>

---

#### public static final
HTML.Tag
OL

Tag <ol>

---

#### public static final
HTML.Tag
OPTION

Tag <option>

---

#### public static final
HTML.Tag
P

Tag <p>

---

#### public static final
HTML.Tag
PARAM

Tag <param>

---

#### public static final
HTML.Tag
PRE

Tag <pre>

---

#### public static final
HTML.Tag
SAMP

Tag <samp>

---

#### public static final
HTML.Tag
SCRIPT

Tag <script>

---

#### public static final
HTML.Tag
SELECT

Tag <select>

---

#### public static final
HTML.Tag
SMALL

Tag <small>

---

#### public static final
HTML.Tag
SPAN

Tag <span>

---

#### public static final
HTML.Tag
STRIKE

Tag <strike>

---

#### public static final
HTML.Tag
S

Tag <s>

---

#### public static final
HTML.Tag
STRONG

Tag <strong>

---

#### public static final
HTML.Tag
STYLE

Tag <style>

---

#### public static final
HTML.Tag
SUB

Tag <sub>

---

#### public static final
HTML.Tag
SUP

Tag <sup>

---

#### public static final
HTML.Tag
TABLE

Tag <table>

---

#### public static final
HTML.Tag
TD

Tag <td>

---

#### public static final
HTML.Tag
TEXTAREA

Tag <textarea>

---

#### public static final
HTML.Tag
TH

Tag <th>

---

#### public static final
HTML.Tag
TITLE

Tag <title>

---

#### public static final
HTML.Tag
TR

Tag <tr>

---

#### public static final
HTML.Tag
TT

Tag <tt>

---

#### public static final
HTML.Tag
U

Tag <u>

---

#### public static final
HTML.Tag
UL

Tag <ul>

---

#### public static final
HTML.Tag
VAR

Tag <var>

---

#### public static final
HTML.Tag
IMPLIED

All text content must be in a paragraph element.
If a paragraph didn't exist when content was
encountered, a paragraph is manufactured.

This is a tag synthesized by the HTML reader.
Since elements are identified by their tag type,
we create a some fake tag types to mark the elements
that were manufactured.

---

#### public static final
HTML.Tag
CONTENT

All text content is labeled with this tag.

This is a tag synthesized by the HTML reader.
Since elements are identified by their tag type,
we create a some fake tag types to mark the elements
that were manufactured.

---

#### public static final
HTML.Tag
COMMENT

All comments are labeled with this tag.

This is a tag synthesized by the HTML reader.
Since elements are identified by their tag type,
we create a some fake tag types to mark the elements
that were manufactured.

---

### Constructor Details

#### public Tag()

**Since:**
- 1.3

---

#### protected Tag​(
String
id)

Creates a new

Tag

with the specified

id

,
and with

causesBreak

and

isBlock

set to

false

.

**Parameters:**
- id

- the id of the new tag

---

#### protected Tag​(
String
id,
boolean causesBreak,
boolean isBlock)

Creates a new

Tag

with the specified

id

;

causesBreak

and

isBlock

are defined
by the user.

**Parameters:**
- id

- the id of the new tag
- causesBreak

-

true

if this tag
causes a break to the flow of data
- isBlock

-

true

if the tag is used
to add structure to a document

---

### Method Details

#### public boolean isBlock()

Returns

true

if this tag is a block
tag, which is a tag used to add structure to a
document.

**Returns:**
- true

if this tag is a block
tag, otherwise returns

false

---

#### public boolean breaksFlow()

Returns

true

if this tag causes a
line break to the flow of data, otherwise returns

false

.

**Returns:**
- true

if this tag causes a
line break to the flow of data, otherwise returns

false

---

#### public boolean isPreformatted()

Returns

true

if this tag is pre-formatted,
which is true if the tag is either

PRE

or

TEXTAREA

.

**Returns:**
- true

if this tag is pre-formatted,
otherwise returns

false

---

#### public
String
toString()

Returns the string representation of the
tag.

**Overrides:**
- toString

in class

Object

**Returns:**
- the

String

representation of the tag

---

### Additional Sections

#### Class HTML.Tag

java.lang.Object

- javax.swing.text.html.HTML.Tag

javax.swing.text.html.HTML.Tag

**Direct Known Subclasses:** HTML.UnknownTag

**Enclosing class:** HTML

```java
public static class
HTML.Tag

extends
Object
```

Typesafe enumeration for an HTML tag. Although the
set of HTML tags is a closed set, we have left the
set open so that people can add their own tag types
to their custom parser and still communicate to the
reader.

public static class

HTML.Tag

extends

Object

Typesafe enumeration for an HTML tag. Although the
set of HTML tags is a closed set, we have left the
set open so that people can add their own tag types
to their custom parser and still communicate to the
reader.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

HTML.Tag

A

Tag <a>

static

HTML.Tag

ADDRESS

Tag <address>

static

HTML.Tag

APPLET

Tag <applet>

static

HTML.Tag

AREA

Tag <area>

static

HTML.Tag

B

Tag <b>

static

HTML.Tag

BASE

Tag <base>

static

HTML.Tag

BASEFONT

Tag <basefont>

static

HTML.Tag

BIG

Tag <big>

static

HTML.Tag

BLOCKQUOTE

Tag <blockquote>

static

HTML.Tag

BODY

Tag <body>

static

HTML.Tag

BR

Tag <br>

static

HTML.Tag

CAPTION

Tag <caption>

static

HTML.Tag

CENTER

Tag <center>

static

HTML.Tag

CITE

Tag <cite>

static

HTML.Tag

CODE

Tag <code>

static

HTML.Tag

COMMENT

All comments are labeled with this tag.

static

HTML.Tag

CONTENT

All text content is labeled with this tag.

static

HTML.Tag

DD

Tag <dd>

static

HTML.Tag

DFN

Tag <dfn>

static

HTML.Tag

DIR

Tag <dir>

static

HTML.Tag

DIV

Tag <div>

static

HTML.Tag

DL

Tag <dl>

static

HTML.Tag

DT

Tag <dt>

static

HTML.Tag

EM

Tag <em>

static

HTML.Tag

FONT

Tag <font>

static

HTML.Tag

FORM

Tag <form>

static

HTML.Tag

FRAME

Tag <frame>

static

HTML.Tag

FRAMESET

Tag <frameset>

static

HTML.Tag

H1

Tag <h1>

static

HTML.Tag

H2

Tag <h2>

static

HTML.Tag

H3

Tag <h3>

static

HTML.Tag

H4

Tag <h4>

static

HTML.Tag

H5

Tag <h5>

static

HTML.Tag

H6

Tag <h6>

static

HTML.Tag

HEAD

Tag <head>

static

HTML.Tag

HR

Tag <hr>

static

HTML.Tag

HTML

Tag <html>

static

HTML.Tag

I

Tag <i>

static

HTML.Tag

IMG

Tag <img>

static

HTML.Tag

IMPLIED

All text content must be in a paragraph element.

static

HTML.Tag

INPUT

Tag <input>

static

HTML.Tag

ISINDEX

Tag <isindex>

static

HTML.Tag

KBD

Tag <kbd>

static

HTML.Tag

LI

Tag <li>

static

HTML.Tag

LINK

Tag <link>

static

HTML.Tag

MAP

Tag <map>

static

HTML.Tag

MENU

Tag <menu>

static

HTML.Tag

META

Tag <meta>

static

HTML.Tag

NOFRAMES

Tag <noframes>

static

HTML.Tag

OBJECT

Tag <object>

static

HTML.Tag

OL

Tag <ol>

static

HTML.Tag

OPTION

Tag <option>

static

HTML.Tag

P

Tag <p>

static

HTML.Tag

PARAM

Tag <param>

static

HTML.Tag

PRE

Tag <pre>

static

HTML.Tag

S

Tag <s>

static

HTML.Tag

SAMP

Tag <samp>

static

HTML.Tag

SCRIPT

Tag <script>

static

HTML.Tag

SELECT

Tag <select>

static

HTML.Tag

SMALL

Tag <small>

static

HTML.Tag

SPAN

Tag <span>

static

HTML.Tag

STRIKE

Tag <strike>

static

HTML.Tag

STRONG

Tag <strong>

static

HTML.Tag

STYLE

Tag <style>

static

HTML.Tag

SUB

Tag <sub>

static

HTML.Tag

SUP

Tag <sup>

static

HTML.Tag

TABLE

Tag <table>

static

HTML.Tag

TD

Tag <td>

static

HTML.Tag

TEXTAREA

Tag <textarea>

static

HTML.Tag

TH

Tag <th>

static

HTML.Tag

TITLE

Tag <title>

static

HTML.Tag

TR

Tag <tr>

static

HTML.Tag

TT

Tag <tt>

static

HTML.Tag

U

Tag <u>

static

HTML.Tag

UL

Tag <ul>

static

HTML.Tag

VAR

Tag <var>

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

Tag

()

protected

Tag

​(

String

id)

Creates a new

Tag

with the specified

id

,
and with

causesBreak

and

isBlock

set to

false

.

protected

Tag

​(

String

id,
boolean causesBreak,
boolean isBlock)

Creates a new

Tag

with the specified

id

;

causesBreak

and

isBlock

are defined
by the user.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

breaksFlow

()

Returns

true

if this tag causes a
line break to the flow of data, otherwise returns

false

.

boolean

isBlock

()

Returns

true

if this tag is a block
tag, which is a tag used to add structure to a
document.

boolean

isPreformatted

()

Returns

true

if this tag is pre-formatted,
which is true if the tag is either

PRE

or

TEXTAREA

.

String

toString

()

Returns the string representation of the
tag.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

static

HTML.Tag

A

Tag <a>

static

HTML.Tag

ADDRESS

Tag <address>

static

HTML.Tag

APPLET

Tag <applet>

static

HTML.Tag

AREA

Tag <area>

static

HTML.Tag

B

Tag <b>

static

HTML.Tag

BASE

Tag <base>

static

HTML.Tag

BASEFONT

Tag <basefont>

static

HTML.Tag

BIG

Tag <big>

static

HTML.Tag

BLOCKQUOTE

Tag <blockquote>

static

HTML.Tag

BODY

Tag <body>

static

HTML.Tag

BR

Tag <br>

static

HTML.Tag

CAPTION

Tag <caption>

static

HTML.Tag

CENTER

Tag <center>

static

HTML.Tag

CITE

Tag <cite>

static

HTML.Tag

CODE

Tag <code>

static

HTML.Tag

COMMENT

All comments are labeled with this tag.

static

HTML.Tag

CONTENT

All text content is labeled with this tag.

static

HTML.Tag

DD

Tag <dd>

static

HTML.Tag

DFN

Tag <dfn>

static

HTML.Tag

DIR

Tag <dir>

static

HTML.Tag

DIV

Tag <div>

static

HTML.Tag

DL

Tag <dl>

static

HTML.Tag

DT

Tag <dt>

static

HTML.Tag

EM

Tag <em>

static

HTML.Tag

FONT

Tag <font>

static

HTML.Tag

FORM

Tag <form>

static

HTML.Tag

FRAME

Tag <frame>

static

HTML.Tag

FRAMESET

Tag <frameset>

static

HTML.Tag

H1

Tag <h1>

static

HTML.Tag

H2

Tag <h2>

static

HTML.Tag

H3

Tag <h3>

static

HTML.Tag

H4

Tag <h4>

static

HTML.Tag

H5

Tag <h5>

static

HTML.Tag

H6

Tag <h6>

static

HTML.Tag

HEAD

Tag <head>

static

HTML.Tag

HR

Tag <hr>

static

HTML.Tag

HTML

Tag <html>

static

HTML.Tag

I

Tag <i>

static

HTML.Tag

IMG

Tag <img>

static

HTML.Tag

IMPLIED

All text content must be in a paragraph element.

static

HTML.Tag

INPUT

Tag <input>

static

HTML.Tag

ISINDEX

Tag <isindex>

static

HTML.Tag

KBD

Tag <kbd>

static

HTML.Tag

LI

Tag <li>

static

HTML.Tag

LINK

Tag <link>

static

HTML.Tag

MAP

Tag <map>

static

HTML.Tag

MENU

Tag <menu>

static

HTML.Tag

META

Tag <meta>

static

HTML.Tag

NOFRAMES

Tag <noframes>

static

HTML.Tag

OBJECT

Tag <object>

static

HTML.Tag

OL

Tag <ol>

static

HTML.Tag

OPTION

Tag <option>

static

HTML.Tag

P

Tag <p>

static

HTML.Tag

PARAM

Tag <param>

static

HTML.Tag

PRE

Tag <pre>

static

HTML.Tag

S

Tag <s>

static

HTML.Tag

SAMP

Tag <samp>

static

HTML.Tag

SCRIPT

Tag <script>

static

HTML.Tag

SELECT

Tag <select>

static

HTML.Tag

SMALL

Tag <small>

static

HTML.Tag

SPAN

Tag <span>

static

HTML.Tag

STRIKE

Tag <strike>

static

HTML.Tag

STRONG

Tag <strong>

static

HTML.Tag

STYLE

Tag <style>

static

HTML.Tag

SUB

Tag <sub>

static

HTML.Tag

SUP

Tag <sup>

static

HTML.Tag

TABLE

Tag <table>

static

HTML.Tag

TD

Tag <td>

static

HTML.Tag

TEXTAREA

Tag <textarea>

static

HTML.Tag

TH

Tag <th>

static

HTML.Tag

TITLE

Tag <title>

static

HTML.Tag

TR

Tag <tr>

static

HTML.Tag

TT

Tag <tt>

static

HTML.Tag

U

Tag <u>

static

HTML.Tag

UL

Tag <ul>

static

HTML.Tag

VAR

Tag <var>

---

#### Field Summary

Tag <a>

Tag <address>

Tag <applet>

Tag <area>

Tag <b>

Tag <base>

Tag <basefont>

Tag <big>

Tag <blockquote>

Tag <body>

Tag <br>

Tag <caption>

Tag <center>

Tag <cite>

Tag <code>

All comments are labeled with this tag.

All text content is labeled with this tag.

Tag <dd>

Tag <dfn>

Tag <dir>

Tag <div>

Tag <dl>

Tag <dt>

Tag <em>

Tag <font>

Tag <form>

Tag <frame>

Tag <frameset>

Tag <h1>

Tag <h2>

Tag <h3>

Tag <h4>

Tag <h5>

Tag <h6>

Tag <head>

Tag <hr>

Tag <html>

Tag <i>

Tag <img>

All text content must be in a paragraph element.

Tag <input>

Tag <isindex>

Tag <kbd>

Tag <li>

Tag <link>

Tag <map>

Tag <menu>

Tag <meta>

Tag <noframes>

Tag <object>

Tag <ol>

Tag <option>

Tag <p>

Tag <param>

Tag <pre>

Tag <s>

Tag <samp>

Tag <script>

Tag <select>

Tag <small>

Tag <span>

Tag <strike>

Tag <strong>

Tag <style>

Tag <sub>

Tag <sup>

Tag <table>

Tag <td>

Tag <textarea>

Tag <th>

Tag <title>

Tag <tr>

Tag <tt>

Tag <u>

Tag <ul>

Tag <var>

Constructor Summary

Constructors

Modifier

Constructor

Description

Tag

()

protected

Tag

​(

String

id)

Creates a new

Tag

with the specified

id

,
and with

causesBreak

and

isBlock

set to

false

.

protected

Tag

​(

String

id,
boolean causesBreak,
boolean isBlock)

Creates a new

Tag

with the specified

id

;

causesBreak

and

isBlock

are defined
by the user.

---

#### Constructor Summary

Creates a new

Tag

with the specified

id

,
and with

causesBreak

and

isBlock

set to

false

.

Creates a new

Tag

with the specified

id

;

causesBreak

and

isBlock

are defined
by the user.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

breaksFlow

()

Returns

true

if this tag causes a
line break to the flow of data, otherwise returns

false

.

boolean

isBlock

()

Returns

true

if this tag is a block
tag, which is a tag used to add structure to a
document.

boolean

isPreformatted

()

Returns

true

if this tag is pre-formatted,
which is true if the tag is either

PRE

or

TEXTAREA

.

String

toString

()

Returns the string representation of the
tag.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Returns

true

if this tag causes a
line break to the flow of data, otherwise returns

false

.

Returns

true

if this tag is a block
tag, which is a tag used to add structure to a
document.

Returns

true

if this tag is pre-formatted,
which is true if the tag is either

PRE

or

TEXTAREA

.

Returns the string representation of the
tag.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- A

```java
public static final
HTML.Tag
A
```

Tag <a>

- ADDRESS

```java
public static final
HTML.Tag
ADDRESS
```

Tag <address>

- APPLET

```java
public static final
HTML.Tag
APPLET
```

Tag <applet>

- AREA

```java
public static final
HTML.Tag
AREA
```

Tag <area>

- B

```java
public static final
HTML.Tag
B
```

Tag <b>

- BASE

```java
public static final
HTML.Tag
BASE
```

Tag <base>

- BASEFONT

```java
public static final
HTML.Tag
BASEFONT
```

Tag <basefont>

- BIG

```java
public static final
HTML.Tag
BIG
```

Tag <big>

- BLOCKQUOTE

```java
public static final
HTML.Tag
BLOCKQUOTE
```

Tag <blockquote>

- BODY

```java
public static final
HTML.Tag
BODY
```

Tag <body>

- BR

```java
public static final
HTML.Tag
BR
```

Tag <br>

- CAPTION

```java
public static final
HTML.Tag
CAPTION
```

Tag <caption>

- CENTER

```java
public static final
HTML.Tag
CENTER
```

Tag <center>

- CITE

```java
public static final
HTML.Tag
CITE
```

Tag <cite>

- CODE

```java
public static final
HTML.Tag
CODE
```

Tag <code>

- DD

```java
public static final
HTML.Tag
DD
```

Tag <dd>

- DFN

```java
public static final
HTML.Tag
DFN
```

Tag <dfn>

- DIR

```java
public static final
HTML.Tag
DIR
```

Tag <dir>

- DIV

```java
public static final
HTML.Tag
DIV
```

Tag <div>

- DL

```java
public static final
HTML.Tag
DL
```

Tag <dl>

- DT

```java
public static final
HTML.Tag
DT
```

Tag <dt>

- EM

```java
public static final
HTML.Tag
EM
```

Tag <em>

- FONT

```java
public static final
HTML.Tag
FONT
```

Tag <font>

- FORM

```java
public static final
HTML.Tag
FORM
```

Tag <form>

- FRAME

```java
public static final
HTML.Tag
FRAME
```

Tag <frame>

- FRAMESET

```java
public static final
HTML.Tag
FRAMESET
```

Tag <frameset>

- H1

```java
public static final
HTML.Tag
H1
```

Tag <h1>

- H2

```java
public static final
HTML.Tag
H2
```

Tag <h2>

- H3

```java
public static final
HTML.Tag
H3
```

Tag <h3>

- H4

```java
public static final
HTML.Tag
H4
```

Tag <h4>

- H5

```java
public static final
HTML.Tag
H5
```

Tag <h5>

- H6

```java
public static final
HTML.Tag
H6
```

Tag <h6>

- HEAD

```java
public static final
HTML.Tag
HEAD
```

Tag <head>

- HR

```java
public static final
HTML.Tag
HR
```

Tag <hr>

- HTML

```java
public static final
HTML.Tag
HTML
```

Tag <html>

- I

```java
public static final
HTML.Tag
I
```

Tag <i>

- IMG

```java
public static final
HTML.Tag
IMG
```

Tag <img>

- INPUT

```java
public static final
HTML.Tag
INPUT
```

Tag <input>

- ISINDEX

```java
public static final
HTML.Tag
ISINDEX
```

Tag <isindex>

- KBD

```java
public static final
HTML.Tag
KBD
```

Tag <kbd>

- LI

```java
public static final
HTML.Tag
LI
```

Tag <li>

- LINK

```java
public static final
HTML.Tag
LINK
```

Tag <link>

- MAP

```java
public static final
HTML.Tag
MAP
```

Tag <map>

- MENU

```java
public static final
HTML.Tag
MENU
```

Tag <menu>

- META

```java
public static final
HTML.Tag
META
```

Tag <meta>

- NOFRAMES

```java
public static final
HTML.Tag
NOFRAMES
```

Tag <noframes>

- OBJECT

```java
public static final
HTML.Tag
OBJECT
```

Tag <object>

- OL

```java
public static final
HTML.Tag
OL
```

Tag <ol>

- OPTION

```java
public static final
HTML.Tag
OPTION
```

Tag <option>

- P

```java
public static final
HTML.Tag
P
```

Tag <p>

- PARAM

```java
public static final
HTML.Tag
PARAM
```

Tag <param>

- PRE

```java
public static final
HTML.Tag
PRE
```

Tag <pre>

- SAMP

```java
public static final
HTML.Tag
SAMP
```

Tag <samp>

- SCRIPT

```java
public static final
HTML.Tag
SCRIPT
```

Tag <script>

- SELECT

```java
public static final
HTML.Tag
SELECT
```

Tag <select>

- SMALL

```java
public static final
HTML.Tag
SMALL
```

Tag <small>

- SPAN

```java
public static final
HTML.Tag
SPAN
```

Tag <span>

- STRIKE

```java
public static final
HTML.Tag
STRIKE
```

Tag <strike>

- S

```java
public static final
HTML.Tag
S
```

Tag <s>

- STRONG

```java
public static final
HTML.Tag
STRONG
```

Tag <strong>

- STYLE

```java
public static final
HTML.Tag
STYLE
```

Tag <style>

- SUB

```java
public static final
HTML.Tag
SUB
```

Tag <sub>

- SUP

```java
public static final
HTML.Tag
SUP
```

Tag <sup>

- TABLE

```java
public static final
HTML.Tag
TABLE
```

Tag <table>

- TD

```java
public static final
HTML.Tag
TD
```

Tag <td>

- TEXTAREA

```java
public static final
HTML.Tag
TEXTAREA
```

Tag <textarea>

- TH

```java
public static final
HTML.Tag
TH
```

Tag <th>

- TITLE

```java
public static final
HTML.Tag
TITLE
```

Tag <title>

- TR

```java
public static final
HTML.Tag
TR
```

Tag <tr>

- TT

```java
public static final
HTML.Tag
TT
```

Tag <tt>

- U

```java
public static final
HTML.Tag
U
```

Tag <u>

- UL

```java
public static final
HTML.Tag
UL
```

Tag <ul>

- VAR

```java
public static final
HTML.Tag
VAR
```

Tag <var>

- IMPLIED

```java
public static final
HTML.Tag
IMPLIED
```

All text content must be in a paragraph element.
If a paragraph didn't exist when content was
encountered, a paragraph is manufactured.

This is a tag synthesized by the HTML reader.
Since elements are identified by their tag type,
we create a some fake tag types to mark the elements
that were manufactured.

- CONTENT

```java
public static final
HTML.Tag
CONTENT
```

All text content is labeled with this tag.

This is a tag synthesized by the HTML reader.
Since elements are identified by their tag type,
we create a some fake tag types to mark the elements
that were manufactured.

- COMMENT

```java
public static final
HTML.Tag
COMMENT
```

All comments are labeled with this tag.

This is a tag synthesized by the HTML reader.
Since elements are identified by their tag type,
we create a some fake tag types to mark the elements
that were manufactured.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Tag

```java
public Tag()
```

**Since:** 1.3

- Tag

```java
protected Tag​(
String
id)
```

Creates a new

Tag

with the specified

id

,
and with

causesBreak

and

isBlock

set to

false

.

**Parameters:** id

- the id of the new tag

- Tag

```java
protected Tag​(
String
id,
boolean causesBreak,
boolean isBlock)
```

Creates a new

Tag

with the specified

id

;

causesBreak

and

isBlock

are defined
by the user.

**Parameters:** id

- the id of the new tag
**Parameters:** causesBreak

-

true

if this tag
causes a break to the flow of data
**Parameters:** isBlock

-

true

if the tag is used
to add structure to a document

============ METHOD DETAIL ==========

- Method Detail

- isBlock

```java
public boolean isBlock()
```

Returns

true

if this tag is a block
tag, which is a tag used to add structure to a
document.

**Returns:** true

if this tag is a block
tag, otherwise returns

false

- breaksFlow

```java
public boolean breaksFlow()
```

Returns

true

if this tag causes a
line break to the flow of data, otherwise returns

false

.

**Returns:** true

if this tag causes a
line break to the flow of data, otherwise returns

false

- isPreformatted

```java
public boolean isPreformatted()
```

Returns

true

if this tag is pre-formatted,
which is true if the tag is either

PRE

or

TEXTAREA

.

**Returns:** true

if this tag is pre-formatted,
otherwise returns

false

- toString

```java
public
String
toString()
```

Returns the string representation of the
tag.

**Overrides:** toString

in class

Object
**Returns:** the

String

representation of the tag

Field Detail

- A

```java
public static final
HTML.Tag
A
```

Tag <a>

- ADDRESS

```java
public static final
HTML.Tag
ADDRESS
```

Tag <address>

- APPLET

```java
public static final
HTML.Tag
APPLET
```

Tag <applet>

- AREA

```java
public static final
HTML.Tag
AREA
```

Tag <area>

- B

```java
public static final
HTML.Tag
B
```

Tag <b>

- BASE

```java
public static final
HTML.Tag
BASE
```

Tag <base>

- BASEFONT

```java
public static final
HTML.Tag
BASEFONT
```

Tag <basefont>

- BIG

```java
public static final
HTML.Tag
BIG
```

Tag <big>

- BLOCKQUOTE

```java
public static final
HTML.Tag
BLOCKQUOTE
```

Tag <blockquote>

- BODY

```java
public static final
HTML.Tag
BODY
```

Tag <body>

- BR

```java
public static final
HTML.Tag
BR
```

Tag <br>

- CAPTION

```java
public static final
HTML.Tag
CAPTION
```

Tag <caption>

- CENTER

```java
public static final
HTML.Tag
CENTER
```

Tag <center>

- CITE

```java
public static final
HTML.Tag
CITE
```

Tag <cite>

- CODE

```java
public static final
HTML.Tag
CODE
```

Tag <code>

- DD

```java
public static final
HTML.Tag
DD
```

Tag <dd>

- DFN

```java
public static final
HTML.Tag
DFN
```

Tag <dfn>

- DIR

```java
public static final
HTML.Tag
DIR
```

Tag <dir>

- DIV

```java
public static final
HTML.Tag
DIV
```

Tag <div>

- DL

```java
public static final
HTML.Tag
DL
```

Tag <dl>

- DT

```java
public static final
HTML.Tag
DT
```

Tag <dt>

- EM

```java
public static final
HTML.Tag
EM
```

Tag <em>

- FONT

```java
public static final
HTML.Tag
FONT
```

Tag <font>

- FORM

```java
public static final
HTML.Tag
FORM
```

Tag <form>

- FRAME

```java
public static final
HTML.Tag
FRAME
```

Tag <frame>

- FRAMESET

```java
public static final
HTML.Tag
FRAMESET
```

Tag <frameset>

- H1

```java
public static final
HTML.Tag
H1
```

Tag <h1>

- H2

```java
public static final
HTML.Tag
H2
```

Tag <h2>

- H3

```java
public static final
HTML.Tag
H3
```

Tag <h3>

- H4

```java
public static final
HTML.Tag
H4
```

Tag <h4>

- H5

```java
public static final
HTML.Tag
H5
```

Tag <h5>

- H6

```java
public static final
HTML.Tag
H6
```

Tag <h6>

- HEAD

```java
public static final
HTML.Tag
HEAD
```

Tag <head>

- HR

```java
public static final
HTML.Tag
HR
```

Tag <hr>

- HTML

```java
public static final
HTML.Tag
HTML
```

Tag <html>

- I

```java
public static final
HTML.Tag
I
```

Tag <i>

- IMG

```java
public static final
HTML.Tag
IMG
```

Tag <img>

- INPUT

```java
public static final
HTML.Tag
INPUT
```

Tag <input>

- ISINDEX

```java
public static final
HTML.Tag
ISINDEX
```

Tag <isindex>

- KBD

```java
public static final
HTML.Tag
KBD
```

Tag <kbd>

- LI

```java
public static final
HTML.Tag
LI
```

Tag <li>

- LINK

```java
public static final
HTML.Tag
LINK
```

Tag <link>

- MAP

```java
public static final
HTML.Tag
MAP
```

Tag <map>

- MENU

```java
public static final
HTML.Tag
MENU
```

Tag <menu>

- META

```java
public static final
HTML.Tag
META
```

Tag <meta>

- NOFRAMES

```java
public static final
HTML.Tag
NOFRAMES
```

Tag <noframes>

- OBJECT

```java
public static final
HTML.Tag
OBJECT
```

Tag <object>

- OL

```java
public static final
HTML.Tag
OL
```

Tag <ol>

- OPTION

```java
public static final
HTML.Tag
OPTION
```

Tag <option>

- P

```java
public static final
HTML.Tag
P
```

Tag <p>

- PARAM

```java
public static final
HTML.Tag
PARAM
```

Tag <param>

- PRE

```java
public static final
HTML.Tag
PRE
```

Tag <pre>

- SAMP

```java
public static final
HTML.Tag
SAMP
```

Tag <samp>

- SCRIPT

```java
public static final
HTML.Tag
SCRIPT
```

Tag <script>

- SELECT

```java
public static final
HTML.Tag
SELECT
```

Tag <select>

- SMALL

```java
public static final
HTML.Tag
SMALL
```

Tag <small>

- SPAN

```java
public static final
HTML.Tag
SPAN
```

Tag <span>

- STRIKE

```java
public static final
HTML.Tag
STRIKE
```

Tag <strike>

- S

```java
public static final
HTML.Tag
S
```

Tag <s>

- STRONG

```java
public static final
HTML.Tag
STRONG
```

Tag <strong>

- STYLE

```java
public static final
HTML.Tag
STYLE
```

Tag <style>

- SUB

```java
public static final
HTML.Tag
SUB
```

Tag <sub>

- SUP

```java
public static final
HTML.Tag
SUP
```

Tag <sup>

- TABLE

```java
public static final
HTML.Tag
TABLE
```

Tag <table>

- TD

```java
public static final
HTML.Tag
TD
```

Tag <td>

- TEXTAREA

```java
public static final
HTML.Tag
TEXTAREA
```

Tag <textarea>

- TH

```java
public static final
HTML.Tag
TH
```

Tag <th>

- TITLE

```java
public static final
HTML.Tag
TITLE
```

Tag <title>

- TR

```java
public static final
HTML.Tag
TR
```

Tag <tr>

- TT

```java
public static final
HTML.Tag
TT
```

Tag <tt>

- U

```java
public static final
HTML.Tag
U
```

Tag <u>

- UL

```java
public static final
HTML.Tag
UL
```

Tag <ul>

- VAR

```java
public static final
HTML.Tag
VAR
```

Tag <var>

- IMPLIED

```java
public static final
HTML.Tag
IMPLIED
```

All text content must be in a paragraph element.
If a paragraph didn't exist when content was
encountered, a paragraph is manufactured.

This is a tag synthesized by the HTML reader.
Since elements are identified by their tag type,
we create a some fake tag types to mark the elements
that were manufactured.

- CONTENT

```java
public static final
HTML.Tag
CONTENT
```

All text content is labeled with this tag.

This is a tag synthesized by the HTML reader.
Since elements are identified by their tag type,
we create a some fake tag types to mark the elements
that were manufactured.

- COMMENT

```java
public static final
HTML.Tag
COMMENT
```

All comments are labeled with this tag.

This is a tag synthesized by the HTML reader.
Since elements are identified by their tag type,
we create a some fake tag types to mark the elements
that were manufactured.

---

#### Field Detail

A

```java
public static final
HTML.Tag
A
```

Tag <a>

---

#### A

public static final

HTML.Tag

A

Tag <a>

ADDRESS

```java
public static final
HTML.Tag
ADDRESS
```

Tag <address>

---

#### ADDRESS

public static final

HTML.Tag

ADDRESS

Tag <address>

APPLET

```java
public static final
HTML.Tag
APPLET
```

Tag <applet>

---

#### APPLET

public static final

HTML.Tag

APPLET

Tag <applet>

AREA

```java
public static final
HTML.Tag
AREA
```

Tag <area>

---

#### AREA

public static final

HTML.Tag

AREA

Tag <area>

B

```java
public static final
HTML.Tag
B
```

Tag <b>

---

#### B

public static final

HTML.Tag

B

Tag <b>

BASE

```java
public static final
HTML.Tag
BASE
```

Tag <base>

---

#### BASE

public static final

HTML.Tag

BASE

Tag <base>

BASEFONT

```java
public static final
HTML.Tag
BASEFONT
```

Tag <basefont>

---

#### BASEFONT

public static final

HTML.Tag

BASEFONT

Tag <basefont>

BIG

```java
public static final
HTML.Tag
BIG
```

Tag <big>

---

#### BIG

public static final

HTML.Tag

BIG

Tag <big>

BLOCKQUOTE

```java
public static final
HTML.Tag
BLOCKQUOTE
```

Tag <blockquote>

---

#### BLOCKQUOTE

public static final

HTML.Tag

BLOCKQUOTE

Tag <blockquote>

BODY

```java
public static final
HTML.Tag
BODY
```

Tag <body>

---

#### BODY

public static final

HTML.Tag

BODY

Tag <body>

BR

```java
public static final
HTML.Tag
BR
```

Tag <br>

---

#### BR

public static final

HTML.Tag

BR

Tag <br>

CAPTION

```java
public static final
HTML.Tag
CAPTION
```

Tag <caption>

---

#### CAPTION

public static final

HTML.Tag

CAPTION

Tag <caption>

CENTER

```java
public static final
HTML.Tag
CENTER
```

Tag <center>

---

#### CENTER

public static final

HTML.Tag

CENTER

Tag <center>

CITE

```java
public static final
HTML.Tag
CITE
```

Tag <cite>

---

#### CITE

public static final

HTML.Tag

CITE

Tag <cite>

CODE

```java
public static final
HTML.Tag
CODE
```

Tag <code>

---

#### CODE

public static final

HTML.Tag

CODE

Tag <code>

DD

```java
public static final
HTML.Tag
DD
```

Tag <dd>

---

#### DD

public static final

HTML.Tag

DD

Tag <dd>

DFN

```java
public static final
HTML.Tag
DFN
```

Tag <dfn>

---

#### DFN

public static final

HTML.Tag

DFN

Tag <dfn>

DIR

```java
public static final
HTML.Tag
DIR
```

Tag <dir>

---

#### DIR

public static final

HTML.Tag

DIR

Tag <dir>

DIV

```java
public static final
HTML.Tag
DIV
```

Tag <div>

---

#### DIV

public static final

HTML.Tag

DIV

Tag <div>

DL

```java
public static final
HTML.Tag
DL
```

Tag <dl>

---

#### DL

public static final

HTML.Tag

DL

Tag <dl>

DT

```java
public static final
HTML.Tag
DT
```

Tag <dt>

---

#### DT

public static final

HTML.Tag

DT

Tag <dt>

EM

```java
public static final
HTML.Tag
EM
```

Tag <em>

---

#### EM

public static final

HTML.Tag

EM

Tag <em>

FONT

```java
public static final
HTML.Tag
FONT
```

Tag <font>

---

#### FONT

public static final

HTML.Tag

FONT

Tag <font>

FORM

```java
public static final
HTML.Tag
FORM
```

Tag <form>

---

#### FORM

public static final

HTML.Tag

FORM

Tag <form>

FRAME

```java
public static final
HTML.Tag
FRAME
```

Tag <frame>

---

#### FRAME

public static final

HTML.Tag

FRAME

Tag <frame>

FRAMESET

```java
public static final
HTML.Tag
FRAMESET
```

Tag <frameset>

---

#### FRAMESET

public static final

HTML.Tag

FRAMESET

Tag <frameset>

H1

```java
public static final
HTML.Tag
H1
```

Tag <h1>

---

#### H1

public static final

HTML.Tag

H1

Tag <h1>

H2

```java
public static final
HTML.Tag
H2
```

Tag <h2>

---

#### H2

public static final

HTML.Tag

H2

Tag <h2>

H3

```java
public static final
HTML.Tag
H3
```

Tag <h3>

---

#### H3

public static final

HTML.Tag

H3

Tag <h3>

H4

```java
public static final
HTML.Tag
H4
```

Tag <h4>

---

#### H4

public static final

HTML.Tag

H4

Tag <h4>

H5

```java
public static final
HTML.Tag
H5
```

Tag <h5>

---

#### H5

public static final

HTML.Tag

H5

Tag <h5>

H6

```java
public static final
HTML.Tag
H6
```

Tag <h6>

---

#### H6

public static final

HTML.Tag

H6

Tag <h6>

HEAD

```java
public static final
HTML.Tag
HEAD
```

Tag <head>

---

#### HEAD

public static final

HTML.Tag

HEAD

Tag <head>

HR

```java
public static final
HTML.Tag
HR
```

Tag <hr>

---

#### HR

public static final

HTML.Tag

HR

Tag <hr>

HTML

```java
public static final
HTML.Tag
HTML
```

Tag <html>

---

#### HTML

public static final

HTML.Tag

HTML

Tag <html>

I

```java
public static final
HTML.Tag
I
```

Tag <i>

---

#### I

public static final

HTML.Tag

I

Tag <i>

IMG

```java
public static final
HTML.Tag
IMG
```

Tag <img>

---

#### IMG

public static final

HTML.Tag

IMG

Tag <img>

INPUT

```java
public static final
HTML.Tag
INPUT
```

Tag <input>

---

#### INPUT

public static final

HTML.Tag

INPUT

Tag <input>

ISINDEX

```java
public static final
HTML.Tag
ISINDEX
```

Tag <isindex>

---

#### ISINDEX

public static final

HTML.Tag

ISINDEX

Tag <isindex>

KBD

```java
public static final
HTML.Tag
KBD
```

Tag <kbd>

---

#### KBD

public static final

HTML.Tag

KBD

Tag <kbd>

LI

```java
public static final
HTML.Tag
LI
```

Tag <li>

---

#### LI

public static final

HTML.Tag

LI

Tag <li>

LINK

```java
public static final
HTML.Tag
LINK
```

Tag <link>

---

#### LINK

public static final

HTML.Tag

LINK

Tag <link>

MAP

```java
public static final
HTML.Tag
MAP
```

Tag <map>

---

#### MAP

public static final

HTML.Tag

MAP

Tag <map>

MENU

```java
public static final
HTML.Tag
MENU
```

Tag <menu>

---

#### MENU

public static final

HTML.Tag

MENU

Tag <menu>

META

```java
public static final
HTML.Tag
META
```

Tag <meta>

---

#### META

public static final

HTML.Tag

META

Tag <meta>

NOFRAMES

```java
public static final
HTML.Tag
NOFRAMES
```

Tag <noframes>

---

#### NOFRAMES

public static final

HTML.Tag

NOFRAMES

Tag <noframes>

OBJECT

```java
public static final
HTML.Tag
OBJECT
```

Tag <object>

---

#### OBJECT

public static final

HTML.Tag

OBJECT

Tag <object>

OL

```java
public static final
HTML.Tag
OL
```

Tag <ol>

---

#### OL

public static final

HTML.Tag

OL

Tag <ol>

OPTION

```java
public static final
HTML.Tag
OPTION
```

Tag <option>

---

#### OPTION

public static final

HTML.Tag

OPTION

Tag <option>

P

```java
public static final
HTML.Tag
P
```

Tag <p>

---

#### P

public static final

HTML.Tag

P

Tag <p>

PARAM

```java
public static final
HTML.Tag
PARAM
```

Tag <param>

---

#### PARAM

public static final

HTML.Tag

PARAM

Tag <param>

PRE

```java
public static final
HTML.Tag
PRE
```

Tag <pre>

---

#### PRE

public static final

HTML.Tag

PRE

Tag <pre>

SAMP

```java
public static final
HTML.Tag
SAMP
```

Tag <samp>

---

#### SAMP

public static final

HTML.Tag

SAMP

Tag <samp>

SCRIPT

```java
public static final
HTML.Tag
SCRIPT
```

Tag <script>

---

#### SCRIPT

public static final

HTML.Tag

SCRIPT

Tag <script>

SELECT

```java
public static final
HTML.Tag
SELECT
```

Tag <select>

---

#### SELECT

public static final

HTML.Tag

SELECT

Tag <select>

SMALL

```java
public static final
HTML.Tag
SMALL
```

Tag <small>

---

#### SMALL

public static final

HTML.Tag

SMALL

Tag <small>

SPAN

```java
public static final
HTML.Tag
SPAN
```

Tag <span>

---

#### SPAN

public static final

HTML.Tag

SPAN

Tag <span>

STRIKE

```java
public static final
HTML.Tag
STRIKE
```

Tag <strike>

---

#### STRIKE

public static final

HTML.Tag

STRIKE

Tag <strike>

S

```java
public static final
HTML.Tag
S
```

Tag <s>

---

#### S

public static final

HTML.Tag

S

Tag <s>

STRONG

```java
public static final
HTML.Tag
STRONG
```

Tag <strong>

---

#### STRONG

public static final

HTML.Tag

STRONG

Tag <strong>

STYLE

```java
public static final
HTML.Tag
STYLE
```

Tag <style>

---

#### STYLE

public static final

HTML.Tag

STYLE

Tag <style>

SUB

```java
public static final
HTML.Tag
SUB
```

Tag <sub>

---

#### SUB

public static final

HTML.Tag

SUB

Tag <sub>

SUP

```java
public static final
HTML.Tag
SUP
```

Tag <sup>

---

#### SUP

public static final

HTML.Tag

SUP

Tag <sup>

TABLE

```java
public static final
HTML.Tag
TABLE
```

Tag <table>

---

#### TABLE

public static final

HTML.Tag

TABLE

Tag <table>

TD

```java
public static final
HTML.Tag
TD
```

Tag <td>

---

#### TD

public static final

HTML.Tag

TD

Tag <td>

TEXTAREA

```java
public static final
HTML.Tag
TEXTAREA
```

Tag <textarea>

---

#### TEXTAREA

public static final

HTML.Tag

TEXTAREA

Tag <textarea>

TH

```java
public static final
HTML.Tag
TH
```

Tag <th>

---

#### TH

public static final

HTML.Tag

TH

Tag <th>

TITLE

```java
public static final
HTML.Tag
TITLE
```

Tag <title>

---

#### TITLE

public static final

HTML.Tag

TITLE

Tag <title>

TR

```java
public static final
HTML.Tag
TR
```

Tag <tr>

---

#### TR

public static final

HTML.Tag

TR

Tag <tr>

TT

```java
public static final
HTML.Tag
TT
```

Tag <tt>

---

#### TT

public static final

HTML.Tag

TT

Tag <tt>

U

```java
public static final
HTML.Tag
U
```

Tag <u>

---

#### U

public static final

HTML.Tag

U

Tag <u>

UL

```java
public static final
HTML.Tag
UL
```

Tag <ul>

---

#### UL

public static final

HTML.Tag

UL

Tag <ul>

VAR

```java
public static final
HTML.Tag
VAR
```

Tag <var>

---

#### VAR

public static final

HTML.Tag

VAR

Tag <var>

IMPLIED

```java
public static final
HTML.Tag
IMPLIED
```

All text content must be in a paragraph element.
If a paragraph didn't exist when content was
encountered, a paragraph is manufactured.

This is a tag synthesized by the HTML reader.
Since elements are identified by their tag type,
we create a some fake tag types to mark the elements
that were manufactured.

---

#### IMPLIED

public static final

HTML.Tag

IMPLIED

All text content must be in a paragraph element.
If a paragraph didn't exist when content was
encountered, a paragraph is manufactured.

This is a tag synthesized by the HTML reader.
Since elements are identified by their tag type,
we create a some fake tag types to mark the elements
that were manufactured.

This is a tag synthesized by the HTML reader.
Since elements are identified by their tag type,
we create a some fake tag types to mark the elements
that were manufactured.

CONTENT

```java
public static final
HTML.Tag
CONTENT
```

All text content is labeled with this tag.

This is a tag synthesized by the HTML reader.
Since elements are identified by their tag type,
we create a some fake tag types to mark the elements
that were manufactured.

---

#### CONTENT

public static final

HTML.Tag

CONTENT

All text content is labeled with this tag.

This is a tag synthesized by the HTML reader.
Since elements are identified by their tag type,
we create a some fake tag types to mark the elements
that were manufactured.

This is a tag synthesized by the HTML reader.
Since elements are identified by their tag type,
we create a some fake tag types to mark the elements
that were manufactured.

COMMENT

```java
public static final
HTML.Tag
COMMENT
```

All comments are labeled with this tag.

This is a tag synthesized by the HTML reader.
Since elements are identified by their tag type,
we create a some fake tag types to mark the elements
that were manufactured.

---

#### COMMENT

public static final

HTML.Tag

COMMENT

All comments are labeled with this tag.

This is a tag synthesized by the HTML reader.
Since elements are identified by their tag type,
we create a some fake tag types to mark the elements
that were manufactured.

This is a tag synthesized by the HTML reader.
Since elements are identified by their tag type,
we create a some fake tag types to mark the elements
that were manufactured.

Constructor Detail

- Tag

```java
public Tag()
```

**Since:** 1.3

- Tag

```java
protected Tag​(
String
id)
```

Creates a new

Tag

with the specified

id

,
and with

causesBreak

and

isBlock

set to

false

.

**Parameters:** id

- the id of the new tag

- Tag

```java
protected Tag​(
String
id,
boolean causesBreak,
boolean isBlock)
```

Creates a new

Tag

with the specified

id

;

causesBreak

and

isBlock

are defined
by the user.

**Parameters:** id

- the id of the new tag
**Parameters:** causesBreak

-

true

if this tag
causes a break to the flow of data
**Parameters:** isBlock

-

true

if the tag is used
to add structure to a document

---

#### Constructor Detail

Tag

```java
public Tag()
```

**Since:** 1.3

---

#### Tag

public Tag()

Tag

```java
protected Tag​(
String
id)
```

Creates a new

Tag

with the specified

id

,
and with

causesBreak

and

isBlock

set to

false

.

**Parameters:** id

- the id of the new tag

---

#### Tag

protected Tag​(

String

id)

Creates a new

Tag

with the specified

id

,
and with

causesBreak

and

isBlock

set to

false

.

Tag

```java
protected Tag​(
String
id,
boolean causesBreak,
boolean isBlock)
```

Creates a new

Tag

with the specified

id

;

causesBreak

and

isBlock

are defined
by the user.

**Parameters:** id

- the id of the new tag
**Parameters:** causesBreak

-

true

if this tag
causes a break to the flow of data
**Parameters:** isBlock

-

true

if the tag is used
to add structure to a document

---

#### Tag

protected Tag​(

String

id,
boolean causesBreak,
boolean isBlock)

Creates a new

Tag

with the specified

id

;

causesBreak

and

isBlock

are defined
by the user.

Method Detail

- isBlock

```java
public boolean isBlock()
```

Returns

true

if this tag is a block
tag, which is a tag used to add structure to a
document.

**Returns:** true

if this tag is a block
tag, otherwise returns

false

- breaksFlow

```java
public boolean breaksFlow()
```

Returns

true

if this tag causes a
line break to the flow of data, otherwise returns

false

.

**Returns:** true

if this tag causes a
line break to the flow of data, otherwise returns

false

- isPreformatted

```java
public boolean isPreformatted()
```

Returns

true

if this tag is pre-formatted,
which is true if the tag is either

PRE

or

TEXTAREA

.

**Returns:** true

if this tag is pre-formatted,
otherwise returns

false

- toString

```java
public
String
toString()
```

Returns the string representation of the
tag.

**Overrides:** toString

in class

Object
**Returns:** the

String

representation of the tag

---

#### Method Detail

isBlock

```java
public boolean isBlock()
```

Returns

true

if this tag is a block
tag, which is a tag used to add structure to a
document.

**Returns:** true

if this tag is a block
tag, otherwise returns

false

---

#### isBlock

public boolean isBlock()

Returns

true

if this tag is a block
tag, which is a tag used to add structure to a
document.

breaksFlow

```java
public boolean breaksFlow()
```

Returns

true

if this tag causes a
line break to the flow of data, otherwise returns

false

.

**Returns:** true

if this tag causes a
line break to the flow of data, otherwise returns

false

---

#### breaksFlow

public boolean breaksFlow()

Returns

true

if this tag causes a
line break to the flow of data, otherwise returns

false

.

isPreformatted

```java
public boolean isPreformatted()
```

Returns

true

if this tag is pre-formatted,
which is true if the tag is either

PRE

or

TEXTAREA

.

**Returns:** true

if this tag is pre-formatted,
otherwise returns

false

---

#### isPreformatted

public boolean isPreformatted()

Returns

true

if this tag is pre-formatted,
which is true if the tag is either

PRE

or

TEXTAREA

.

toString

```java
public
String
toString()
```

Returns the string representation of the
tag.

**Overrides:** toString

in class

Object
**Returns:** the

String

representation of the tag

---

#### toString

public

String

toString()

Returns the string representation of the
tag.

---

