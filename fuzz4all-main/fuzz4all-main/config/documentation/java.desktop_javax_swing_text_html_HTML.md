# Class HTML

**Source:** `java.desktop\javax\swing\text\html\HTML.html`

### Class Description

```java
public class
HTML

extends
Object
```

Constants used in the

HTMLDocument

. These
are basically tag and attribute definitions.

---

### Field Details

#### public static final
String
NULL_ATTRIBUTE_VALUE

NULL_ATTRIBUTE_VALUE

used in cases where the value for the attribute has not
been specified.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public HTML()

*No description found.*

---

### Method Details

#### public static
HTML.Tag
[] getAllTags()

Returns the set of actual HTML tags that
are recognized by the default HTML reader.
This set does not include tags that are
manufactured by the reader.

**Returns:**
- the set of actual HTML tags that
are recognized by the default HTML reader

---

#### public static
HTML.Tag
getTag​(
String
tagName)

Fetches a tag constant for a well-known tag name (i.e. one of
the tags in the set {A, ADDRESS, APPLET, AREA, B,
BASE, BASEFONT, BIG,
BLOCKQUOTE, BODY, BR, CAPTION, CENTER, CITE, CODE,
DD, DFN, DIR, DIV, DL, DT, EM, FONT, FORM, FRAME,
FRAMESET, H1, H2, H3, H4, H5, H6, HEAD, HR, HTML,
I, IMG, INPUT, ISINDEX, KBD, LI, LINK, MAP, MENU,
META, NOBR, NOFRAMES, OBJECT, OL, OPTION, P, PARAM,
PRE, SAMP, SCRIPT, SELECT, SMALL, SPAN, STRIKE, S,
STRONG, STYLE, SUB, SUP, TABLE, TD, TEXTAREA,
TH, TITLE, TR, TT, U, UL, VAR}. If the given
name does not represent one of the well-known tags, then

null

will be returned.

**Parameters:**
- tagName

- the

String

name requested

**Returns:**
- a tag constant corresponding to the

tagName

,
or

null

if not found

---

#### public static int getIntegerAttributeValue​(
AttributeSet
attr,

HTML.Attribute
key,
int def)

Fetches an integer attribute value. Attribute values
are stored as a string, and this is a convenience method
to convert to an actual integer.

**Parameters:**
- attr

- the set of attributes to use to try to fetch a value
- key

- the key to use to fetch the value
- def

- the default value to use if the attribute isn't
defined or there is an error converting to an integer

**Returns:**
- an attribute value

---

#### public static
HTML.Attribute
[] getAllAttributeKeys()

Returns the set of HTML attributes recognized.

**Returns:**
- the set of HTML attributes recognized

---

#### public static
HTML.Attribute
getAttributeKey​(
String
attName)

Fetches an attribute constant for a well-known attribute name
(i.e. one of the attributes in the set {FACE, COMMENT, SIZE,
COLOR, CLEAR, BACKGROUND, BGCOLOR, TEXT, LINK, VLINK, ALINK,
WIDTH, HEIGHT, ALIGN, NAME, HREF, REL, REV, TITLE, TARGET,
SHAPE, COORDS, ISMAP, NOHREF, ALT, ID, SRC, HSPACE, VSPACE,
USEMAP, LOWSRC, CODEBASE, CODE, ARCHIVE, VALUE, VALUETYPE,
TYPE, CLASS, STYLE, LANG, DIR, DECLARE, CLASSID, DATA, CODETYPE,
STANDBY, BORDER, SHAPES, NOSHADE, COMPACT, START, ACTION, METHOD,
ENCTYPE, CHECKED, MAXLENGTH, MULTIPLE, SELECTED, ROWS, COLS,
DUMMY, CELLSPACING, CELLPADDING, VALIGN, HALIGN, NOWRAP, ROWSPAN,
COLSPAN, PROMPT, HTTPEQUIV, CONTENT, LANGUAGE, VERSION, N,
FRAMEBORDER, MARGINWIDTH, MARGINHEIGHT, SCROLLING, NORESIZE,
MEDIA, ENDTAG}).
If the given name does not represent one of the well-known attributes,
then

null

will be returned.

**Parameters:**
- attName

- the

String

requested

**Returns:**
- the

Attribute

corresponding to

attName

---

### Additional Sections

#### Class HTML

java.lang.Object

- javax.swing.text.html.HTML

javax.swing.text.html.HTML

```java
public class
HTML

extends
Object
```

Constants used in the

HTMLDocument

. These
are basically tag and attribute definitions.

public class

HTML

extends

Object

Constants used in the

HTMLDocument

. These
are basically tag and attribute definitions.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

HTML.Attribute

Typesafe enumeration representing an HTML
attribute.

static class

HTML.Tag

Typesafe enumeration for an HTML tag.

static class

HTML.UnknownTag

Class represents unknown HTML tag.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

NULL_ATTRIBUTE_VALUE

NULL_ATTRIBUTE_VALUE

used in cases where the value for the attribute has not
been specified.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

HTML

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

HTML.Attribute

[]

getAllAttributeKeys

()

Returns the set of HTML attributes recognized.

static

HTML.Tag

[]

getAllTags

()

Returns the set of actual HTML tags that
are recognized by the default HTML reader.

static

HTML.Attribute

getAttributeKey

​(

String

attName)

Fetches an attribute constant for a well-known attribute name
(i.e. one of the attributes in the set {FACE, COMMENT, SIZE,
COLOR, CLEAR, BACKGROUND, BGCOLOR, TEXT, LINK, VLINK, ALINK,
WIDTH, HEIGHT, ALIGN, NAME, HREF, REL, REV, TITLE, TARGET,
SHAPE, COORDS, ISMAP, NOHREF, ALT, ID, SRC, HSPACE, VSPACE,
USEMAP, LOWSRC, CODEBASE, CODE, ARCHIVE, VALUE, VALUETYPE,
TYPE, CLASS, STYLE, LANG, DIR, DECLARE, CLASSID, DATA, CODETYPE,
STANDBY, BORDER, SHAPES, NOSHADE, COMPACT, START, ACTION, METHOD,
ENCTYPE, CHECKED, MAXLENGTH, MULTIPLE, SELECTED, ROWS, COLS,
DUMMY, CELLSPACING, CELLPADDING, VALIGN, HALIGN, NOWRAP, ROWSPAN,
COLSPAN, PROMPT, HTTPEQUIV, CONTENT, LANGUAGE, VERSION, N,
FRAMEBORDER, MARGINWIDTH, MARGINHEIGHT, SCROLLING, NORESIZE,
MEDIA, ENDTAG}).

static int

getIntegerAttributeValue

​(

AttributeSet

attr,

HTML.Attribute

key,
int def)

Fetches an integer attribute value.

static

HTML.Tag

getTag

​(

String

tagName)

Fetches a tag constant for a well-known tag name (i.e. one of
the tags in the set {A, ADDRESS, APPLET, AREA, B,
BASE, BASEFONT, BIG,
BLOCKQUOTE, BODY, BR, CAPTION, CENTER, CITE, CODE,
DD, DFN, DIR, DIV, DL, DT, EM, FONT, FORM, FRAME,
FRAMESET, H1, H2, H3, H4, H5, H6, HEAD, HR, HTML,
I, IMG, INPUT, ISINDEX, KBD, LI, LINK, MAP, MENU,
META, NOBR, NOFRAMES, OBJECT, OL, OPTION, P, PARAM,
PRE, SAMP, SCRIPT, SELECT, SMALL, SPAN, STRIKE, S,
STRONG, STYLE, SUB, SUP, TABLE, TD, TEXTAREA,
TH, TITLE, TR, TT, U, UL, VAR}.

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

toString

,

wait

,

wait

,

wait

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

HTML.Attribute

Typesafe enumeration representing an HTML
attribute.

static class

HTML.Tag

Typesafe enumeration for an HTML tag.

static class

HTML.UnknownTag

Class represents unknown HTML tag.

---

#### Nested Class Summary

Typesafe enumeration representing an HTML
attribute.

Typesafe enumeration for an HTML tag.

Class represents unknown HTML tag.

Field Summary

Fields

Modifier and Type

Field

Description

static

String

NULL_ATTRIBUTE_VALUE

NULL_ATTRIBUTE_VALUE

used in cases where the value for the attribute has not
been specified.

---

#### Field Summary

NULL_ATTRIBUTE_VALUE

used in cases where the value for the attribute has not
been specified.

Constructor Summary

Constructors

Constructor

Description

HTML

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

HTML.Attribute

[]

getAllAttributeKeys

()

Returns the set of HTML attributes recognized.

static

HTML.Tag

[]

getAllTags

()

Returns the set of actual HTML tags that
are recognized by the default HTML reader.

static

HTML.Attribute

getAttributeKey

​(

String

attName)

Fetches an attribute constant for a well-known attribute name
(i.e. one of the attributes in the set {FACE, COMMENT, SIZE,
COLOR, CLEAR, BACKGROUND, BGCOLOR, TEXT, LINK, VLINK, ALINK,
WIDTH, HEIGHT, ALIGN, NAME, HREF, REL, REV, TITLE, TARGET,
SHAPE, COORDS, ISMAP, NOHREF, ALT, ID, SRC, HSPACE, VSPACE,
USEMAP, LOWSRC, CODEBASE, CODE, ARCHIVE, VALUE, VALUETYPE,
TYPE, CLASS, STYLE, LANG, DIR, DECLARE, CLASSID, DATA, CODETYPE,
STANDBY, BORDER, SHAPES, NOSHADE, COMPACT, START, ACTION, METHOD,
ENCTYPE, CHECKED, MAXLENGTH, MULTIPLE, SELECTED, ROWS, COLS,
DUMMY, CELLSPACING, CELLPADDING, VALIGN, HALIGN, NOWRAP, ROWSPAN,
COLSPAN, PROMPT, HTTPEQUIV, CONTENT, LANGUAGE, VERSION, N,
FRAMEBORDER, MARGINWIDTH, MARGINHEIGHT, SCROLLING, NORESIZE,
MEDIA, ENDTAG}).

static int

getIntegerAttributeValue

​(

AttributeSet

attr,

HTML.Attribute

key,
int def)

Fetches an integer attribute value.

static

HTML.Tag

getTag

​(

String

tagName)

Fetches a tag constant for a well-known tag name (i.e. one of
the tags in the set {A, ADDRESS, APPLET, AREA, B,
BASE, BASEFONT, BIG,
BLOCKQUOTE, BODY, BR, CAPTION, CENTER, CITE, CODE,
DD, DFN, DIR, DIV, DL, DT, EM, FONT, FORM, FRAME,
FRAMESET, H1, H2, H3, H4, H5, H6, HEAD, HR, HTML,
I, IMG, INPUT, ISINDEX, KBD, LI, LINK, MAP, MENU,
META, NOBR, NOFRAMES, OBJECT, OL, OPTION, P, PARAM,
PRE, SAMP, SCRIPT, SELECT, SMALL, SPAN, STRIKE, S,
STRONG, STYLE, SUB, SUP, TABLE, TD, TEXTAREA,
TH, TITLE, TR, TT, U, UL, VAR}.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the set of HTML attributes recognized.

Returns the set of actual HTML tags that
are recognized by the default HTML reader.

Fetches an attribute constant for a well-known attribute name
(i.e. one of the attributes in the set {FACE, COMMENT, SIZE,
COLOR, CLEAR, BACKGROUND, BGCOLOR, TEXT, LINK, VLINK, ALINK,
WIDTH, HEIGHT, ALIGN, NAME, HREF, REL, REV, TITLE, TARGET,
SHAPE, COORDS, ISMAP, NOHREF, ALT, ID, SRC, HSPACE, VSPACE,
USEMAP, LOWSRC, CODEBASE, CODE, ARCHIVE, VALUE, VALUETYPE,
TYPE, CLASS, STYLE, LANG, DIR, DECLARE, CLASSID, DATA, CODETYPE,
STANDBY, BORDER, SHAPES, NOSHADE, COMPACT, START, ACTION, METHOD,
ENCTYPE, CHECKED, MAXLENGTH, MULTIPLE, SELECTED, ROWS, COLS,
DUMMY, CELLSPACING, CELLPADDING, VALIGN, HALIGN, NOWRAP, ROWSPAN,
COLSPAN, PROMPT, HTTPEQUIV, CONTENT, LANGUAGE, VERSION, N,
FRAMEBORDER, MARGINWIDTH, MARGINHEIGHT, SCROLLING, NORESIZE,
MEDIA, ENDTAG}).

Fetches an integer attribute value.

Fetches a tag constant for a well-known tag name (i.e. one of
the tags in the set {A, ADDRESS, APPLET, AREA, B,
BASE, BASEFONT, BIG,
BLOCKQUOTE, BODY, BR, CAPTION, CENTER, CITE, CODE,
DD, DFN, DIR, DIV, DL, DT, EM, FONT, FORM, FRAME,
FRAMESET, H1, H2, H3, H4, H5, H6, HEAD, HR, HTML,
I, IMG, INPUT, ISINDEX, KBD, LI, LINK, MAP, MENU,
META, NOBR, NOFRAMES, OBJECT, OL, OPTION, P, PARAM,
PRE, SAMP, SCRIPT, SELECT, SMALL, SPAN, STRIKE, S,
STRONG, STYLE, SUB, SUP, TABLE, TD, TEXTAREA,
TH, TITLE, TR, TT, U, UL, VAR}.

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

toString

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

- NULL_ATTRIBUTE_VALUE

```java
public static final
String
NULL_ATTRIBUTE_VALUE
```

NULL_ATTRIBUTE_VALUE

used in cases where the value for the attribute has not
been specified.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- HTML

```java
public HTML()
```

============ METHOD DETAIL ==========

- Method Detail

- getAllTags

```java
public static
HTML.Tag
[] getAllTags()
```

Returns the set of actual HTML tags that
are recognized by the default HTML reader.
This set does not include tags that are
manufactured by the reader.

**Returns:** the set of actual HTML tags that
are recognized by the default HTML reader

- getTag

```java
public static
HTML.Tag
getTag​(
String
tagName)
```

Fetches a tag constant for a well-known tag name (i.e. one of
the tags in the set {A, ADDRESS, APPLET, AREA, B,
BASE, BASEFONT, BIG,
BLOCKQUOTE, BODY, BR, CAPTION, CENTER, CITE, CODE,
DD, DFN, DIR, DIV, DL, DT, EM, FONT, FORM, FRAME,
FRAMESET, H1, H2, H3, H4, H5, H6, HEAD, HR, HTML,
I, IMG, INPUT, ISINDEX, KBD, LI, LINK, MAP, MENU,
META, NOBR, NOFRAMES, OBJECT, OL, OPTION, P, PARAM,
PRE, SAMP, SCRIPT, SELECT, SMALL, SPAN, STRIKE, S,
STRONG, STYLE, SUB, SUP, TABLE, TD, TEXTAREA,
TH, TITLE, TR, TT, U, UL, VAR}. If the given
name does not represent one of the well-known tags, then

null

will be returned.

**Parameters:** tagName

- the

String

name requested
**Returns:** a tag constant corresponding to the

tagName

,
or

null

if not found

- getIntegerAttributeValue

```java
public static int getIntegerAttributeValue​(
AttributeSet
attr,

HTML.Attribute
key,
int def)
```

Fetches an integer attribute value. Attribute values
are stored as a string, and this is a convenience method
to convert to an actual integer.

**Parameters:** attr

- the set of attributes to use to try to fetch a value
**Parameters:** key

- the key to use to fetch the value
**Parameters:** def

- the default value to use if the attribute isn't
defined or there is an error converting to an integer
**Returns:** an attribute value

- getAllAttributeKeys

```java
public static
HTML.Attribute
[] getAllAttributeKeys()
```

Returns the set of HTML attributes recognized.

**Returns:** the set of HTML attributes recognized

- getAttributeKey

```java
public static
HTML.Attribute
getAttributeKey​(
String
attName)
```

Fetches an attribute constant for a well-known attribute name
(i.e. one of the attributes in the set {FACE, COMMENT, SIZE,
COLOR, CLEAR, BACKGROUND, BGCOLOR, TEXT, LINK, VLINK, ALINK,
WIDTH, HEIGHT, ALIGN, NAME, HREF, REL, REV, TITLE, TARGET,
SHAPE, COORDS, ISMAP, NOHREF, ALT, ID, SRC, HSPACE, VSPACE,
USEMAP, LOWSRC, CODEBASE, CODE, ARCHIVE, VALUE, VALUETYPE,
TYPE, CLASS, STYLE, LANG, DIR, DECLARE, CLASSID, DATA, CODETYPE,
STANDBY, BORDER, SHAPES, NOSHADE, COMPACT, START, ACTION, METHOD,
ENCTYPE, CHECKED, MAXLENGTH, MULTIPLE, SELECTED, ROWS, COLS,
DUMMY, CELLSPACING, CELLPADDING, VALIGN, HALIGN, NOWRAP, ROWSPAN,
COLSPAN, PROMPT, HTTPEQUIV, CONTENT, LANGUAGE, VERSION, N,
FRAMEBORDER, MARGINWIDTH, MARGINHEIGHT, SCROLLING, NORESIZE,
MEDIA, ENDTAG}).
If the given name does not represent one of the well-known attributes,
then

null

will be returned.

**Parameters:** attName

- the

String

requested
**Returns:** the

Attribute

corresponding to

attName

Field Detail

- NULL_ATTRIBUTE_VALUE

```java
public static final
String
NULL_ATTRIBUTE_VALUE
```

NULL_ATTRIBUTE_VALUE

used in cases where the value for the attribute has not
been specified.

**See Also:** Constant Field Values

---

#### Field Detail

NULL_ATTRIBUTE_VALUE

```java
public static final
String
NULL_ATTRIBUTE_VALUE
```

NULL_ATTRIBUTE_VALUE

used in cases where the value for the attribute has not
been specified.

**See Also:** Constant Field Values

---

#### NULL_ATTRIBUTE_VALUE

public static final

String

NULL_ATTRIBUTE_VALUE

NULL_ATTRIBUTE_VALUE

used in cases where the value for the attribute has not
been specified.

Constructor Detail

- HTML

```java
public HTML()
```

---

#### Constructor Detail

HTML

```java
public HTML()
```

---

#### HTML

public HTML()

Method Detail

- getAllTags

```java
public static
HTML.Tag
[] getAllTags()
```

Returns the set of actual HTML tags that
are recognized by the default HTML reader.
This set does not include tags that are
manufactured by the reader.

**Returns:** the set of actual HTML tags that
are recognized by the default HTML reader

- getTag

```java
public static
HTML.Tag
getTag​(
String
tagName)
```

Fetches a tag constant for a well-known tag name (i.e. one of
the tags in the set {A, ADDRESS, APPLET, AREA, B,
BASE, BASEFONT, BIG,
BLOCKQUOTE, BODY, BR, CAPTION, CENTER, CITE, CODE,
DD, DFN, DIR, DIV, DL, DT, EM, FONT, FORM, FRAME,
FRAMESET, H1, H2, H3, H4, H5, H6, HEAD, HR, HTML,
I, IMG, INPUT, ISINDEX, KBD, LI, LINK, MAP, MENU,
META, NOBR, NOFRAMES, OBJECT, OL, OPTION, P, PARAM,
PRE, SAMP, SCRIPT, SELECT, SMALL, SPAN, STRIKE, S,
STRONG, STYLE, SUB, SUP, TABLE, TD, TEXTAREA,
TH, TITLE, TR, TT, U, UL, VAR}. If the given
name does not represent one of the well-known tags, then

null

will be returned.

**Parameters:** tagName

- the

String

name requested
**Returns:** a tag constant corresponding to the

tagName

,
or

null

if not found

- getIntegerAttributeValue

```java
public static int getIntegerAttributeValue​(
AttributeSet
attr,

HTML.Attribute
key,
int def)
```

Fetches an integer attribute value. Attribute values
are stored as a string, and this is a convenience method
to convert to an actual integer.

**Parameters:** attr

- the set of attributes to use to try to fetch a value
**Parameters:** key

- the key to use to fetch the value
**Parameters:** def

- the default value to use if the attribute isn't
defined or there is an error converting to an integer
**Returns:** an attribute value

- getAllAttributeKeys

```java
public static
HTML.Attribute
[] getAllAttributeKeys()
```

Returns the set of HTML attributes recognized.

**Returns:** the set of HTML attributes recognized

- getAttributeKey

```java
public static
HTML.Attribute
getAttributeKey​(
String
attName)
```

Fetches an attribute constant for a well-known attribute name
(i.e. one of the attributes in the set {FACE, COMMENT, SIZE,
COLOR, CLEAR, BACKGROUND, BGCOLOR, TEXT, LINK, VLINK, ALINK,
WIDTH, HEIGHT, ALIGN, NAME, HREF, REL, REV, TITLE, TARGET,
SHAPE, COORDS, ISMAP, NOHREF, ALT, ID, SRC, HSPACE, VSPACE,
USEMAP, LOWSRC, CODEBASE, CODE, ARCHIVE, VALUE, VALUETYPE,
TYPE, CLASS, STYLE, LANG, DIR, DECLARE, CLASSID, DATA, CODETYPE,
STANDBY, BORDER, SHAPES, NOSHADE, COMPACT, START, ACTION, METHOD,
ENCTYPE, CHECKED, MAXLENGTH, MULTIPLE, SELECTED, ROWS, COLS,
DUMMY, CELLSPACING, CELLPADDING, VALIGN, HALIGN, NOWRAP, ROWSPAN,
COLSPAN, PROMPT, HTTPEQUIV, CONTENT, LANGUAGE, VERSION, N,
FRAMEBORDER, MARGINWIDTH, MARGINHEIGHT, SCROLLING, NORESIZE,
MEDIA, ENDTAG}).
If the given name does not represent one of the well-known attributes,
then

null

will be returned.

**Parameters:** attName

- the

String

requested
**Returns:** the

Attribute

corresponding to

attName

---

#### Method Detail

getAllTags

```java
public static
HTML.Tag
[] getAllTags()
```

Returns the set of actual HTML tags that
are recognized by the default HTML reader.
This set does not include tags that are
manufactured by the reader.

**Returns:** the set of actual HTML tags that
are recognized by the default HTML reader

---

#### getAllTags

public static

HTML.Tag

[] getAllTags()

Returns the set of actual HTML tags that
are recognized by the default HTML reader.
This set does not include tags that are
manufactured by the reader.

getTag

```java
public static
HTML.Tag
getTag​(
String
tagName)
```

Fetches a tag constant for a well-known tag name (i.e. one of
the tags in the set {A, ADDRESS, APPLET, AREA, B,
BASE, BASEFONT, BIG,
BLOCKQUOTE, BODY, BR, CAPTION, CENTER, CITE, CODE,
DD, DFN, DIR, DIV, DL, DT, EM, FONT, FORM, FRAME,
FRAMESET, H1, H2, H3, H4, H5, H6, HEAD, HR, HTML,
I, IMG, INPUT, ISINDEX, KBD, LI, LINK, MAP, MENU,
META, NOBR, NOFRAMES, OBJECT, OL, OPTION, P, PARAM,
PRE, SAMP, SCRIPT, SELECT, SMALL, SPAN, STRIKE, S,
STRONG, STYLE, SUB, SUP, TABLE, TD, TEXTAREA,
TH, TITLE, TR, TT, U, UL, VAR}. If the given
name does not represent one of the well-known tags, then

null

will be returned.

**Parameters:** tagName

- the

String

name requested
**Returns:** a tag constant corresponding to the

tagName

,
or

null

if not found

---

#### getTag

public static

HTML.Tag

getTag​(

String

tagName)

Fetches a tag constant for a well-known tag name (i.e. one of
the tags in the set {A, ADDRESS, APPLET, AREA, B,
BASE, BASEFONT, BIG,
BLOCKQUOTE, BODY, BR, CAPTION, CENTER, CITE, CODE,
DD, DFN, DIR, DIV, DL, DT, EM, FONT, FORM, FRAME,
FRAMESET, H1, H2, H3, H4, H5, H6, HEAD, HR, HTML,
I, IMG, INPUT, ISINDEX, KBD, LI, LINK, MAP, MENU,
META, NOBR, NOFRAMES, OBJECT, OL, OPTION, P, PARAM,
PRE, SAMP, SCRIPT, SELECT, SMALL, SPAN, STRIKE, S,
STRONG, STYLE, SUB, SUP, TABLE, TD, TEXTAREA,
TH, TITLE, TR, TT, U, UL, VAR}. If the given
name does not represent one of the well-known tags, then

null

will be returned.

getIntegerAttributeValue

```java
public static int getIntegerAttributeValue​(
AttributeSet
attr,

HTML.Attribute
key,
int def)
```

Fetches an integer attribute value. Attribute values
are stored as a string, and this is a convenience method
to convert to an actual integer.

**Parameters:** attr

- the set of attributes to use to try to fetch a value
**Parameters:** key

- the key to use to fetch the value
**Parameters:** def

- the default value to use if the attribute isn't
defined or there is an error converting to an integer
**Returns:** an attribute value

---

#### getIntegerAttributeValue

public static int getIntegerAttributeValue​(

AttributeSet

attr,

HTML.Attribute

key,
int def)

Fetches an integer attribute value. Attribute values
are stored as a string, and this is a convenience method
to convert to an actual integer.

getAllAttributeKeys

```java
public static
HTML.Attribute
[] getAllAttributeKeys()
```

Returns the set of HTML attributes recognized.

**Returns:** the set of HTML attributes recognized

---

#### getAllAttributeKeys

public static

HTML.Attribute

[] getAllAttributeKeys()

Returns the set of HTML attributes recognized.

getAttributeKey

```java
public static
HTML.Attribute
getAttributeKey​(
String
attName)
```

Fetches an attribute constant for a well-known attribute name
(i.e. one of the attributes in the set {FACE, COMMENT, SIZE,
COLOR, CLEAR, BACKGROUND, BGCOLOR, TEXT, LINK, VLINK, ALINK,
WIDTH, HEIGHT, ALIGN, NAME, HREF, REL, REV, TITLE, TARGET,
SHAPE, COORDS, ISMAP, NOHREF, ALT, ID, SRC, HSPACE, VSPACE,
USEMAP, LOWSRC, CODEBASE, CODE, ARCHIVE, VALUE, VALUETYPE,
TYPE, CLASS, STYLE, LANG, DIR, DECLARE, CLASSID, DATA, CODETYPE,
STANDBY, BORDER, SHAPES, NOSHADE, COMPACT, START, ACTION, METHOD,
ENCTYPE, CHECKED, MAXLENGTH, MULTIPLE, SELECTED, ROWS, COLS,
DUMMY, CELLSPACING, CELLPADDING, VALIGN, HALIGN, NOWRAP, ROWSPAN,
COLSPAN, PROMPT, HTTPEQUIV, CONTENT, LANGUAGE, VERSION, N,
FRAMEBORDER, MARGINWIDTH, MARGINHEIGHT, SCROLLING, NORESIZE,
MEDIA, ENDTAG}).
If the given name does not represent one of the well-known attributes,
then

null

will be returned.

**Parameters:** attName

- the

String

requested
**Returns:** the

Attribute

corresponding to

attName

---

#### getAttributeKey

public static

HTML.Attribute

getAttributeKey​(

String

attName)

Fetches an attribute constant for a well-known attribute name
(i.e. one of the attributes in the set {FACE, COMMENT, SIZE,
COLOR, CLEAR, BACKGROUND, BGCOLOR, TEXT, LINK, VLINK, ALINK,
WIDTH, HEIGHT, ALIGN, NAME, HREF, REL, REV, TITLE, TARGET,
SHAPE, COORDS, ISMAP, NOHREF, ALT, ID, SRC, HSPACE, VSPACE,
USEMAP, LOWSRC, CODEBASE, CODE, ARCHIVE, VALUE, VALUETYPE,
TYPE, CLASS, STYLE, LANG, DIR, DECLARE, CLASSID, DATA, CODETYPE,
STANDBY, BORDER, SHAPES, NOSHADE, COMPACT, START, ACTION, METHOD,
ENCTYPE, CHECKED, MAXLENGTH, MULTIPLE, SELECTED, ROWS, COLS,
DUMMY, CELLSPACING, CELLPADDING, VALIGN, HALIGN, NOWRAP, ROWSPAN,
COLSPAN, PROMPT, HTTPEQUIV, CONTENT, LANGUAGE, VERSION, N,
FRAMEBORDER, MARGINWIDTH, MARGINHEIGHT, SCROLLING, NORESIZE,
MEDIA, ENDTAG}).
If the given name does not represent one of the well-known attributes,
then

null

will be returned.

---

