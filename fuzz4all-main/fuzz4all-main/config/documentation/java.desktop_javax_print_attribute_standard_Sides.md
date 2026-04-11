# Class Sides

**Source:** `java.desktop\javax\print\attribute\standard\Sides.html`

### Class Description

```java
public final class
Sides

extends
EnumSyntax

implements
DocAttribute
,
PrintRequestAttribute
,
PrintJobAttribute
```

Class

Sides

is a printing attribute class, an enumeration, that
specifies how print-stream pages are to be imposed upon the sides of an
instance of a selected medium, i.e., an impression.

The effect of a

Sides

attribute on a multidoc print job (a job with
multiple documents) depends on whether all the docs have the same sides
values specified or whether different docs have different sides values
specified, and on the (perhaps defaulted) value of the

MultipleDocumentHandling

attribute.

- If all the docs have the same sides value

n

specified, then any
value of

MultipleDocumentHandling

makes
sense, and the printer's processing depends on the

MultipleDocumentHandling

value:

- SINGLE_DOCUMENT

-- All the input docs will be combined
together into one output document. Each media sheet will consist of

n

impressions from the output document.

SINGLE_DOCUMENT_NEW_SHEET

-- All the input docs will be
combined together into one output document. Each media sheet will consist
of

n

impressions from the output document. However, the first
impression of each input doc will always start on a new media sheet; this
means the last media sheet of an input doc may have only one impression
on it.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

-- The input docs will
remain separate. Each media sheet will consist of

n

impressions
from the input doc. Since the input docs are separate, the first
impression of each input doc will always start on a new media sheet; this
means the last media sheet of an input doc may have only one impression
on it.

SEPARATE_DOCUMENTS_COLLATED_COPIES

-- The input docs will
remain separate. Each media sheet will consist of

n

impressions
from the input doc. Since the input docs are separate, the first
impression of each input doc will always start on a new media sheet; this
means the last media sheet of an input doc may have only one impression
on it.

- SINGLE_DOCUMENT

-- All the input docs will be combined
together into one output document. Each media sheet will consist of

n

i

impressions from the output document, where

i

is the number of the input doc corresponding to that point in the output
document. When the next input doc has a different sides value from the
previous input doc, the first print-stream page of the next input doc
goes at the start of the next media sheet, possibly leaving only one
impression on the previous media sheet.

SINGLE_DOCUMENT_NEW_SHEET

-- All the input docs will be
combined together into one output document. Each media sheet will consist
of

n

impressions from the output document. However, the first
impression of each input doc will always start on a new media sheet; this
means the last impression of an input doc may have only one impression on
it.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

-- The input docs will
remain separate. For input doc

i,

each media sheet will consist of

n

i

impressions from the input doc. Since the input docs
are separate, the first impression of each input doc will always start on
a new media sheet; this means the last media sheet of an input doc may
have only one impression on it.

SEPARATE_DOCUMENTS_COLLATED_COPIES

-- The input docs will
remain separate. For input doc

i,

each media sheet will consist of

n

i

impressions from the input doc. Since the input docs
are separate, the first impression of each input doc will always start on
a new media sheet; this means the last media sheet of an input doc may
have only one impression on it.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

DocAttribute

,

PrintJobAttribute

,

PrintRequestAttribute

---

### Field Details

#### public static final
Sides
ONE_SIDED

Imposes each consecutive print-stream page upon the same side of
consecutive media sheets.

---

#### public static final
Sides
TWO_SIDED_LONG_EDGE

Imposes each consecutive pair of print-stream pages upon front and back
sides of consecutive media sheets, such that the orientation of each pair
of print-stream pages on the medium would be correct for the reader as if
for binding on the long edge. This imposition is also known as "duplex"
(see

DUPLEX

).

---

#### public static final
Sides
TWO_SIDED_SHORT_EDGE

Imposes each consecutive pair of print-stream pages upon front and back
sides of consecutive media sheets, such that the orientation of each pair
of print-stream pages on the medium would be correct for the reader as if
for binding on the short edge. This imposition is also known as "tumble"
(see

TUMBLE

).

---

#### public static final
Sides
DUPLEX

An alias for "two sided long edge" (see

TWO_SIDED_LONG_EDGE

).

---

#### public static final
Sides
TUMBLE

An alias for "two sided short edge" (see

TWO_SIDED_SHORT_EDGE

).

---

### Constructor Details

#### protected Sides​(int value)

Construct a new sides enumeration value with the given integer value.

**Parameters:**
- value

- Integer value

---

### Method Details

#### protected
String
[] getStringTable()

Returns the string table for class

Sides

.

**Overrides:**
- getStringTable

in class

EnumSyntax

**Returns:**
- the string table

---

#### protected
EnumSyntax
[] getEnumValueTable()

Returns the enumeration value table for class

Sides

.

**Overrides:**
- getEnumValueTable

in class

EnumSyntax

**Returns:**
- the value table

---

#### public final
Class
<? extends
Attribute
> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

Sides

, the category is class

Sides

itself.

**Specified by:**
- getCategory

in interface

Attribute

**Returns:**
- printing attribute class (category), an instance of class

java.lang.Class

---

#### public final
String
getName()

Get the name of the category of which this attribute value is an
instance.

For class

Sides

, the category name is

"sides"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class Sides

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.Sides

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.Sides

javax.print.attribute.standard.Sides

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

DocAttribute

,

PrintJobAttribute

,

PrintRequestAttribute

```java
public final class
Sides

extends
EnumSyntax

implements
DocAttribute
,
PrintRequestAttribute
,
PrintJobAttribute
```

Class

Sides

is a printing attribute class, an enumeration, that
specifies how print-stream pages are to be imposed upon the sides of an
instance of a selected medium, i.e., an impression.

The effect of a

Sides

attribute on a multidoc print job (a job with
multiple documents) depends on whether all the docs have the same sides
values specified or whether different docs have different sides values
specified, and on the (perhaps defaulted) value of the

MultipleDocumentHandling

attribute.

- If all the docs have the same sides value

n

specified, then any
value of

MultipleDocumentHandling

makes
sense, and the printer's processing depends on the

MultipleDocumentHandling

value:

- SINGLE_DOCUMENT

-- All the input docs will be combined
together into one output document. Each media sheet will consist of

n

impressions from the output document.

SINGLE_DOCUMENT_NEW_SHEET

-- All the input docs will be
combined together into one output document. Each media sheet will consist
of

n

impressions from the output document. However, the first
impression of each input doc will always start on a new media sheet; this
means the last media sheet of an input doc may have only one impression
on it.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

-- The input docs will
remain separate. Each media sheet will consist of

n

impressions
from the input doc. Since the input docs are separate, the first
impression of each input doc will always start on a new media sheet; this
means the last media sheet of an input doc may have only one impression
on it.

SEPARATE_DOCUMENTS_COLLATED_COPIES

-- The input docs will
remain separate. Each media sheet will consist of

n

impressions
from the input doc. Since the input docs are separate, the first
impression of each input doc will always start on a new media sheet; this
means the last media sheet of an input doc may have only one impression
on it.

- SINGLE_DOCUMENT

-- All the input docs will be combined
together into one output document. Each media sheet will consist of

n

i

impressions from the output document, where

i

is the number of the input doc corresponding to that point in the output
document. When the next input doc has a different sides value from the
previous input doc, the first print-stream page of the next input doc
goes at the start of the next media sheet, possibly leaving only one
impression on the previous media sheet.

SINGLE_DOCUMENT_NEW_SHEET

-- All the input docs will be
combined together into one output document. Each media sheet will consist
of

n

impressions from the output document. However, the first
impression of each input doc will always start on a new media sheet; this
means the last impression of an input doc may have only one impression on
it.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

-- The input docs will
remain separate. For input doc

i,

each media sheet will consist of

n

i

impressions from the input doc. Since the input docs
are separate, the first impression of each input doc will always start on
a new media sheet; this means the last media sheet of an input doc may
have only one impression on it.

SEPARATE_DOCUMENTS_COLLATED_COPIES

-- The input docs will
remain separate. For input doc

i,

each media sheet will consist of

n

i

impressions from the input doc. Since the input docs
are separate, the first impression of each input doc will always start on
a new media sheet; this means the last media sheet of an input doc may
have only one impression on it.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

**See Also:** Serialized Form

public final class

Sides

extends

EnumSyntax

implements

DocAttribute

,

PrintRequestAttribute

,

PrintJobAttribute

Class

Sides

is a printing attribute class, an enumeration, that
specifies how print-stream pages are to be imposed upon the sides of an
instance of a selected medium, i.e., an impression.

The effect of a

Sides

attribute on a multidoc print job (a job with
multiple documents) depends on whether all the docs have the same sides
values specified or whether different docs have different sides values
specified, and on the (perhaps defaulted) value of the

MultipleDocumentHandling

attribute.

- If all the docs have the same sides value

n

specified, then any
value of

MultipleDocumentHandling

makes
sense, and the printer's processing depends on the

MultipleDocumentHandling

value:

- SINGLE_DOCUMENT

-- All the input docs will be combined
together into one output document. Each media sheet will consist of

n

impressions from the output document.

SINGLE_DOCUMENT_NEW_SHEET

-- All the input docs will be
combined together into one output document. Each media sheet will consist
of

n

impressions from the output document. However, the first
impression of each input doc will always start on a new media sheet; this
means the last media sheet of an input doc may have only one impression
on it.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

-- The input docs will
remain separate. Each media sheet will consist of

n

impressions
from the input doc. Since the input docs are separate, the first
impression of each input doc will always start on a new media sheet; this
means the last media sheet of an input doc may have only one impression
on it.

SEPARATE_DOCUMENTS_COLLATED_COPIES

-- The input docs will
remain separate. Each media sheet will consist of

n

impressions
from the input doc. Since the input docs are separate, the first
impression of each input doc will always start on a new media sheet; this
means the last media sheet of an input doc may have only one impression
on it.

- SINGLE_DOCUMENT

-- All the input docs will be combined
together into one output document. Each media sheet will consist of

n

i

impressions from the output document, where

i

is the number of the input doc corresponding to that point in the output
document. When the next input doc has a different sides value from the
previous input doc, the first print-stream page of the next input doc
goes at the start of the next media sheet, possibly leaving only one
impression on the previous media sheet.

SINGLE_DOCUMENT_NEW_SHEET

-- All the input docs will be
combined together into one output document. Each media sheet will consist
of

n

impressions from the output document. However, the first
impression of each input doc will always start on a new media sheet; this
means the last impression of an input doc may have only one impression on
it.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

-- The input docs will
remain separate. For input doc

i,

each media sheet will consist of

n

i

impressions from the input doc. Since the input docs
are separate, the first impression of each input doc will always start on
a new media sheet; this means the last media sheet of an input doc may
have only one impression on it.

SEPARATE_DOCUMENTS_COLLATED_COPIES

-- The input docs will
remain separate. For input doc

i,

each media sheet will consist of

n

i

impressions from the input doc. Since the input docs
are separate, the first impression of each input doc will always start on
a new media sheet; this means the last media sheet of an input doc may
have only one impression on it.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

The effect of a

Sides

attribute on a multidoc print job (a job with
multiple documents) depends on whether all the docs have the same sides
values specified or whether different docs have different sides values
specified, and on the (perhaps defaulted) value of the

MultipleDocumentHandling

attribute.

- If all the docs have the same sides value

n

specified, then any
value of

MultipleDocumentHandling

makes
sense, and the printer's processing depends on the

MultipleDocumentHandling

value:

- SINGLE_DOCUMENT

-- All the input docs will be combined
together into one output document. Each media sheet will consist of

n

impressions from the output document.

SINGLE_DOCUMENT_NEW_SHEET

-- All the input docs will be
combined together into one output document. Each media sheet will consist
of

n

impressions from the output document. However, the first
impression of each input doc will always start on a new media sheet; this
means the last media sheet of an input doc may have only one impression
on it.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

-- The input docs will
remain separate. Each media sheet will consist of

n

impressions
from the input doc. Since the input docs are separate, the first
impression of each input doc will always start on a new media sheet; this
means the last media sheet of an input doc may have only one impression
on it.

SEPARATE_DOCUMENTS_COLLATED_COPIES

-- The input docs will
remain separate. Each media sheet will consist of

n

impressions
from the input doc. Since the input docs are separate, the first
impression of each input doc will always start on a new media sheet; this
means the last media sheet of an input doc may have only one impression
on it.

- SINGLE_DOCUMENT

-- All the input docs will be combined
together into one output document. Each media sheet will consist of

n

i

impressions from the output document, where

i

is the number of the input doc corresponding to that point in the output
document. When the next input doc has a different sides value from the
previous input doc, the first print-stream page of the next input doc
goes at the start of the next media sheet, possibly leaving only one
impression on the previous media sheet.

SINGLE_DOCUMENT_NEW_SHEET

-- All the input docs will be
combined together into one output document. Each media sheet will consist
of

n

impressions from the output document. However, the first
impression of each input doc will always start on a new media sheet; this
means the last impression of an input doc may have only one impression on
it.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

-- The input docs will
remain separate. For input doc

i,

each media sheet will consist of

n

i

impressions from the input doc. Since the input docs
are separate, the first impression of each input doc will always start on
a new media sheet; this means the last media sheet of an input doc may
have only one impression on it.

SEPARATE_DOCUMENTS_COLLATED_COPIES

-- The input docs will
remain separate. For input doc

i,

each media sheet will consist of

n

i

impressions from the input doc. Since the input docs
are separate, the first impression of each input doc will always start on
a new media sheet; this means the last media sheet of an input doc may
have only one impression on it.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

If all the docs have the same sides value

n

specified, then any
value of

MultipleDocumentHandling

makes
sense, and the printer's processing depends on the

MultipleDocumentHandling

value:

- SINGLE_DOCUMENT

-- All the input docs will be combined
together into one output document. Each media sheet will consist of

n

impressions from the output document.

SINGLE_DOCUMENT_NEW_SHEET

-- All the input docs will be
combined together into one output document. Each media sheet will consist
of

n

impressions from the output document. However, the first
impression of each input doc will always start on a new media sheet; this
means the last media sheet of an input doc may have only one impression
on it.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

-- The input docs will
remain separate. Each media sheet will consist of

n

impressions
from the input doc. Since the input docs are separate, the first
impression of each input doc will always start on a new media sheet; this
means the last media sheet of an input doc may have only one impression
on it.

SEPARATE_DOCUMENTS_COLLATED_COPIES

-- The input docs will
remain separate. Each media sheet will consist of

n

impressions
from the input doc. Since the input docs are separate, the first
impression of each input doc will always start on a new media sheet; this
means the last media sheet of an input doc may have only one impression
on it.

- SINGLE_DOCUMENT

-- All the input docs will be combined
together into one output document. Each media sheet will consist of

n

i

impressions from the output document, where

i

is the number of the input doc corresponding to that point in the output
document. When the next input doc has a different sides value from the
previous input doc, the first print-stream page of the next input doc
goes at the start of the next media sheet, possibly leaving only one
impression on the previous media sheet.

SINGLE_DOCUMENT_NEW_SHEET

-- All the input docs will be
combined together into one output document. Each media sheet will consist
of

n

impressions from the output document. However, the first
impression of each input doc will always start on a new media sheet; this
means the last impression of an input doc may have only one impression on
it.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

-- The input docs will
remain separate. For input doc

i,

each media sheet will consist of

n

i

impressions from the input doc. Since the input docs
are separate, the first impression of each input doc will always start on
a new media sheet; this means the last media sheet of an input doc may
have only one impression on it.

SEPARATE_DOCUMENTS_COLLATED_COPIES

-- The input docs will
remain separate. For input doc

i,

each media sheet will consist of

n

i

impressions from the input doc. Since the input docs
are separate, the first impression of each input doc will always start on
a new media sheet; this means the last media sheet of an input doc may
have only one impression on it.

SINGLE_DOCUMENT

-- All the input docs will be combined
together into one output document. Each media sheet will consist of

n

impressions from the output document.

SINGLE_DOCUMENT_NEW_SHEET

-- All the input docs will be
combined together into one output document. Each media sheet will consist
of

n

impressions from the output document. However, the first
impression of each input doc will always start on a new media sheet; this
means the last media sheet of an input doc may have only one impression
on it.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

-- The input docs will
remain separate. Each media sheet will consist of

n

impressions
from the input doc. Since the input docs are separate, the first
impression of each input doc will always start on a new media sheet; this
means the last media sheet of an input doc may have only one impression
on it.

SEPARATE_DOCUMENTS_COLLATED_COPIES

-- The input docs will
remain separate. Each media sheet will consist of

n

impressions
from the input doc. Since the input docs are separate, the first
impression of each input doc will always start on a new media sheet; this
means the last media sheet of an input doc may have only one impression
on it.

SINGLE_DOCUMENT

-- All the input docs will be combined
together into one output document. Each media sheet will consist of

n

i

impressions from the output document, where

i

is the number of the input doc corresponding to that point in the output
document. When the next input doc has a different sides value from the
previous input doc, the first print-stream page of the next input doc
goes at the start of the next media sheet, possibly leaving only one
impression on the previous media sheet.

SINGLE_DOCUMENT_NEW_SHEET

-- All the input docs will be
combined together into one output document. Each media sheet will consist
of

n

impressions from the output document. However, the first
impression of each input doc will always start on a new media sheet; this
means the last impression of an input doc may have only one impression on
it.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

-- The input docs will
remain separate. For input doc

i,

each media sheet will consist of

n

i

impressions from the input doc. Since the input docs
are separate, the first impression of each input doc will always start on
a new media sheet; this means the last media sheet of an input doc may
have only one impression on it.

SEPARATE_DOCUMENTS_COLLATED_COPIES

-- The input docs will
remain separate. For input doc

i,

each media sheet will consist of

n

i

impressions from the input doc. Since the input docs
are separate, the first impression of each input doc will always start on
a new media sheet; this means the last media sheet of an input doc may
have only one impression on it.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

Sides

DUPLEX

An alias for "two sided long edge" (see

TWO_SIDED_LONG_EDGE

).

static

Sides

ONE_SIDED

Imposes each consecutive print-stream page upon the same side of
consecutive media sheets.

static

Sides

TUMBLE

An alias for "two sided short edge" (see

TWO_SIDED_SHORT_EDGE

).

static

Sides

TWO_SIDED_LONG_EDGE

Imposes each consecutive pair of print-stream pages upon front and back
sides of consecutive media sheets, such that the orientation of each pair
of print-stream pages on the medium would be correct for the reader as if
for binding on the long edge.

static

Sides

TWO_SIDED_SHORT_EDGE

Imposes each consecutive pair of print-stream pages upon front and back
sides of consecutive media sheets, such that the orientation of each pair
of print-stream pages on the medium would be correct for the reader as if
for binding on the short edge.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Sides

​(int value)

Construct a new sides enumeration value with the given integer value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<? extends

Attribute

>

getCategory

()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

protected

EnumSyntax

[]

getEnumValueTable

()

Returns the enumeration value table for class

Sides

.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

protected

String

[]

getStringTable

()

Returns the string table for class

Sides

.

- Methods declared in class javax.print.attribute.

EnumSyntax

clone

,

getOffset

,

getValue

,

hashCode

,

readResolve

,

toString

- Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

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

Sides

DUPLEX

An alias for "two sided long edge" (see

TWO_SIDED_LONG_EDGE

).

static

Sides

ONE_SIDED

Imposes each consecutive print-stream page upon the same side of
consecutive media sheets.

static

Sides

TUMBLE

An alias for "two sided short edge" (see

TWO_SIDED_SHORT_EDGE

).

static

Sides

TWO_SIDED_LONG_EDGE

Imposes each consecutive pair of print-stream pages upon front and back
sides of consecutive media sheets, such that the orientation of each pair
of print-stream pages on the medium would be correct for the reader as if
for binding on the long edge.

static

Sides

TWO_SIDED_SHORT_EDGE

Imposes each consecutive pair of print-stream pages upon front and back
sides of consecutive media sheets, such that the orientation of each pair
of print-stream pages on the medium would be correct for the reader as if
for binding on the short edge.

---

#### Field Summary

An alias for "two sided long edge" (see

TWO_SIDED_LONG_EDGE

).

Imposes each consecutive print-stream page upon the same side of
consecutive media sheets.

An alias for "two sided short edge" (see

TWO_SIDED_SHORT_EDGE

).

Imposes each consecutive pair of print-stream pages upon front and back
sides of consecutive media sheets, such that the orientation of each pair
of print-stream pages on the medium would be correct for the reader as if
for binding on the long edge.

Imposes each consecutive pair of print-stream pages upon front and back
sides of consecutive media sheets, such that the orientation of each pair
of print-stream pages on the medium would be correct for the reader as if
for binding on the short edge.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Sides

​(int value)

Construct a new sides enumeration value with the given integer value.

---

#### Constructor Summary

Construct a new sides enumeration value with the given integer value.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<? extends

Attribute

>

getCategory

()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

protected

EnumSyntax

[]

getEnumValueTable

()

Returns the enumeration value table for class

Sides

.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

protected

String

[]

getStringTable

()

Returns the string table for class

Sides

.

- Methods declared in class javax.print.attribute.

EnumSyntax

clone

,

getOffset

,

getValue

,

hashCode

,

readResolve

,

toString

- Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

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

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

Returns the enumeration value table for class

Sides

.

Get the name of the category of which this attribute value is an
instance.

Returns the string table for class

Sides

.

Methods declared in class javax.print.attribute.

EnumSyntax

clone

,

getOffset

,

getValue

,

hashCode

,

readResolve

,

toString

---

#### Methods declared in class javax.print.attribute. EnumSyntax

Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

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

- ONE_SIDED

```java
public static final
Sides
ONE_SIDED
```

Imposes each consecutive print-stream page upon the same side of
consecutive media sheets.

- TWO_SIDED_LONG_EDGE

```java
public static final
Sides
TWO_SIDED_LONG_EDGE
```

Imposes each consecutive pair of print-stream pages upon front and back
sides of consecutive media sheets, such that the orientation of each pair
of print-stream pages on the medium would be correct for the reader as if
for binding on the long edge. This imposition is also known as "duplex"
(see

DUPLEX

).

- TWO_SIDED_SHORT_EDGE

```java
public static final
Sides
TWO_SIDED_SHORT_EDGE
```

Imposes each consecutive pair of print-stream pages upon front and back
sides of consecutive media sheets, such that the orientation of each pair
of print-stream pages on the medium would be correct for the reader as if
for binding on the short edge. This imposition is also known as "tumble"
(see

TUMBLE

).

- DUPLEX

```java
public static final
Sides
DUPLEX
```

An alias for "two sided long edge" (see

TWO_SIDED_LONG_EDGE

).

- TUMBLE

```java
public static final
Sides
TUMBLE
```

An alias for "two sided short edge" (see

TWO_SIDED_SHORT_EDGE

).

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Sides

```java
protected Sides​(int value)
```

Construct a new sides enumeration value with the given integer value.

**Parameters:** value

- Integer value

============ METHOD DETAIL ==========

- Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

Sides

.

**Overrides:** getStringTable

in class

EnumSyntax
**Returns:** the string table

- getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

Sides

.

**Overrides:** getEnumValueTable

in class

EnumSyntax
**Returns:** the value table

- getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

Sides

, the category is class

Sides

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

- getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

Sides

, the category name is

"sides"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Field Detail

- ONE_SIDED

```java
public static final
Sides
ONE_SIDED
```

Imposes each consecutive print-stream page upon the same side of
consecutive media sheets.

- TWO_SIDED_LONG_EDGE

```java
public static final
Sides
TWO_SIDED_LONG_EDGE
```

Imposes each consecutive pair of print-stream pages upon front and back
sides of consecutive media sheets, such that the orientation of each pair
of print-stream pages on the medium would be correct for the reader as if
for binding on the long edge. This imposition is also known as "duplex"
(see

DUPLEX

).

- TWO_SIDED_SHORT_EDGE

```java
public static final
Sides
TWO_SIDED_SHORT_EDGE
```

Imposes each consecutive pair of print-stream pages upon front and back
sides of consecutive media sheets, such that the orientation of each pair
of print-stream pages on the medium would be correct for the reader as if
for binding on the short edge. This imposition is also known as "tumble"
(see

TUMBLE

).

- DUPLEX

```java
public static final
Sides
DUPLEX
```

An alias for "two sided long edge" (see

TWO_SIDED_LONG_EDGE

).

- TUMBLE

```java
public static final
Sides
TUMBLE
```

An alias for "two sided short edge" (see

TWO_SIDED_SHORT_EDGE

).

---

#### Field Detail

ONE_SIDED

```java
public static final
Sides
ONE_SIDED
```

Imposes each consecutive print-stream page upon the same side of
consecutive media sheets.

---

#### ONE_SIDED

public static final

Sides

ONE_SIDED

Imposes each consecutive print-stream page upon the same side of
consecutive media sheets.

TWO_SIDED_LONG_EDGE

```java
public static final
Sides
TWO_SIDED_LONG_EDGE
```

Imposes each consecutive pair of print-stream pages upon front and back
sides of consecutive media sheets, such that the orientation of each pair
of print-stream pages on the medium would be correct for the reader as if
for binding on the long edge. This imposition is also known as "duplex"
(see

DUPLEX

).

---

#### TWO_SIDED_LONG_EDGE

public static final

Sides

TWO_SIDED_LONG_EDGE

Imposes each consecutive pair of print-stream pages upon front and back
sides of consecutive media sheets, such that the orientation of each pair
of print-stream pages on the medium would be correct for the reader as if
for binding on the long edge. This imposition is also known as "duplex"
(see

DUPLEX

).

TWO_SIDED_SHORT_EDGE

```java
public static final
Sides
TWO_SIDED_SHORT_EDGE
```

Imposes each consecutive pair of print-stream pages upon front and back
sides of consecutive media sheets, such that the orientation of each pair
of print-stream pages on the medium would be correct for the reader as if
for binding on the short edge. This imposition is also known as "tumble"
(see

TUMBLE

).

---

#### TWO_SIDED_SHORT_EDGE

public static final

Sides

TWO_SIDED_SHORT_EDGE

Imposes each consecutive pair of print-stream pages upon front and back
sides of consecutive media sheets, such that the orientation of each pair
of print-stream pages on the medium would be correct for the reader as if
for binding on the short edge. This imposition is also known as "tumble"
(see

TUMBLE

).

DUPLEX

```java
public static final
Sides
DUPLEX
```

An alias for "two sided long edge" (see

TWO_SIDED_LONG_EDGE

).

---

#### DUPLEX

public static final

Sides

DUPLEX

An alias for "two sided long edge" (see

TWO_SIDED_LONG_EDGE

).

TUMBLE

```java
public static final
Sides
TUMBLE
```

An alias for "two sided short edge" (see

TWO_SIDED_SHORT_EDGE

).

---

#### TUMBLE

public static final

Sides

TUMBLE

An alias for "two sided short edge" (see

TWO_SIDED_SHORT_EDGE

).

Constructor Detail

- Sides

```java
protected Sides​(int value)
```

Construct a new sides enumeration value with the given integer value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

Sides

```java
protected Sides​(int value)
```

Construct a new sides enumeration value with the given integer value.

**Parameters:** value

- Integer value

---

#### Sides

protected Sides​(int value)

Construct a new sides enumeration value with the given integer value.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

Sides

.

**Overrides:** getStringTable

in class

EnumSyntax
**Returns:** the string table

- getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

Sides

.

**Overrides:** getEnumValueTable

in class

EnumSyntax
**Returns:** the value table

- getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

Sides

, the category is class

Sides

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

- getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

Sides

, the category name is

"sides"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

---

#### Method Detail

getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

Sides

.

**Overrides:** getStringTable

in class

EnumSyntax
**Returns:** the string table

---

#### getStringTable

protected

String

[] getStringTable()

Returns the string table for class

Sides

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

Sides

.

**Overrides:** getEnumValueTable

in class

EnumSyntax
**Returns:** the value table

---

#### getEnumValueTable

protected

EnumSyntax

[] getEnumValueTable()

Returns the enumeration value table for class

Sides

.

getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

Sides

, the category is class

Sides

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

---

#### getCategory

public final

Class

<? extends

Attribute

> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

Sides

, the category is class

Sides

itself.

For class

Sides

, the category is class

Sides

itself.

getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

Sides

, the category name is

"sides"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

---

#### getName

public final

String

getName()

Get the name of the category of which this attribute value is an
instance.

For class

Sides

, the category name is

"sides"

.

For class

Sides

, the category name is

"sides"

.

---

