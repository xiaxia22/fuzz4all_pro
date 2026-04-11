# Class SheetCollate

**Source:** `java.desktop\javax\print\attribute\standard\SheetCollate.html`

### Class Description

```java
public final class
SheetCollate

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

SheetCollate

is a printing attribute class, an enumeration,
that specifies whether or not the media sheets of each copy of each printed
document in a job are to be in sequence, when multiple copies of the document
are specified by the

Copies

attribute. When

SheetCollate

is

COLLATED

, each copy of each document is
printed with the print-stream sheets in sequence. When

SheetCollate

is

UNCOLLATED

, each print-stream sheet is printed a number of times
equal to the value of the

Copies

attribute in succession. For
example, suppose a document produces two media sheets as output,

Copies

is 6, and

SheetCollate

is UNCOLLATED; in this
case six copies of the first media sheet are printed followed by six copies
of the second media sheet.

Whether the effect of sheet collation is achieved by placing copies of a
document in multiple output bins or in the same output bin with
implementation defined document separation is implementation dependent. Also
whether it is achieved by making multiple passes over the job or by using an
output sorter is implementation dependent.

If a printer does not support the

SheetCollate

attribute (meaning the
client cannot specify any particular sheet collation), the printer must
behave as though

SheetCollate

were always set to

COLLATED

.

The

SheetCollate

attribute interacts with the

MultipleDocumentHandling

attribute. The

MultipleDocumentHandling

attribute describes
the collation of entire documents, and the

SheetCollate

attribute
describes the semantics of collating individual pages within a document.

The effect of a

SheetCollate

attribute on a multidoc print job (a job
with multiple documents) depends on whether all the docs have the same sheet
collation specified or whether different docs have different sheet collations
specified, and on the (perhaps defaulted) value of the

MultipleDocumentHandling

attribute.

- If all the docs have the same sheet collation specified, then the
following combinations of

SheetCollate

and

MultipleDocumentHandling

are permitted,
and the printer reports an error when the job is submitted if any other
combination is specified:

- SheetCollate = COLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT -- All the input docs will be
combined into one output document. Multiple copies of the output document
will be produced with pages in collated order, i.e. pages 1, 2, 3, . . .,
1, 2, 3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT_NEW_SHEET -- All the input
docs will be combined into one output document, and the first impression
of each input doc will always start on a new media sheet. Multiple copies
of the output document will be produced with pages in collated order,
i.e. pages 1, 2, 3, . . ., 1, 2, 3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in collated order, but the documents themselves in
uncollated order, i.e. pages A1, A2, A3, . . ., A1, A2, A3, . . ., B1,
B2, B3, . . ., B1, B2, B3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_COLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in collated order, with the documents themselves also in
collated order, i.e. pages A1, A2, A3, . . ., B1, B2, B3, . . ., A1, A2,
A3, . . ., B1, B2, B3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT -- All the input docs will be
combined into one output document. Multiple copies of the output document
will be produced with pages in uncollated order, i.e. pages 1, 1, . . .,
2, 2, . . ., 3, 3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT_NEW_SHEET -- All the input
docs will be combined into one output document, and the first impression
of each input doc will always start on a new media sheet. Multiple copies
of the output document will be produced with pages in uncollated order,
i.e. pages 1, 1, . . ., 2, 2, . . ., 3, 3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in uncollated order, with the documents themselves also
in uncollated order, i.e. pages A1, A1, . . ., A2, A2, . . ., A3, A3, . .
., B1, B1, . . ., B2, B2, . . ., B3, B3, . . .

If different docs have different sheet collations specified, then only
one value of

MultipleDocumentHandling

is
permitted, and the printer reports an error when the job is submitted if
any other value is specified:

- MultipleDocumentHandling

=
SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each input doc will remain a
separate output document. Multiple copies of each output document (call
them A, B, . . .) will be produced with each document's pages in collated
or uncollated order as the corresponding input doc's SheetCollate
attribute specifies, and with the documents themselves in uncollated
order. If document A had SheetCollate = UNCOLLATED and document B had
SheetCollate = COLLATED, the following pages would be produced: A1, A1, .
. ., A2, A2, . . ., A3, A3, . . ., B1, B2, B3, . . ., B1, B2, B3, . . .

IPP Compatibility:

SheetCollate is not an IPP attribute at present.

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
SheetCollate
UNCOLLATED

Sheets within a document appear in uncollated order when multiple copies
are printed.

---

#### public static final
SheetCollate
COLLATED

Sheets within a document appear in collated order when multiple copies
are printed.

---

### Constructor Details

#### protected SheetCollate​(int value)

Construct a new sheet collate enumeration value with the given integer
value.

**Parameters:**
- value

- Integer value

---

### Method Details

#### protected
String
[] getStringTable()

Returns the string table for class

SheetCollate

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

SheetCollate

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

SheetCollate

, the category is class

SheetCollate

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

SheetCollate

, the category name is

"sheet-collate"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class SheetCollate

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.SheetCollate

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.SheetCollate

javax.print.attribute.standard.SheetCollate

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
SheetCollate

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

SheetCollate

is a printing attribute class, an enumeration,
that specifies whether or not the media sheets of each copy of each printed
document in a job are to be in sequence, when multiple copies of the document
are specified by the

Copies

attribute. When

SheetCollate

is

COLLATED

, each copy of each document is
printed with the print-stream sheets in sequence. When

SheetCollate

is

UNCOLLATED

, each print-stream sheet is printed a number of times
equal to the value of the

Copies

attribute in succession. For
example, suppose a document produces two media sheets as output,

Copies

is 6, and

SheetCollate

is UNCOLLATED; in this
case six copies of the first media sheet are printed followed by six copies
of the second media sheet.

Whether the effect of sheet collation is achieved by placing copies of a
document in multiple output bins or in the same output bin with
implementation defined document separation is implementation dependent. Also
whether it is achieved by making multiple passes over the job or by using an
output sorter is implementation dependent.

If a printer does not support the

SheetCollate

attribute (meaning the
client cannot specify any particular sheet collation), the printer must
behave as though

SheetCollate

were always set to

COLLATED

.

The

SheetCollate

attribute interacts with the

MultipleDocumentHandling

attribute. The

MultipleDocumentHandling

attribute describes
the collation of entire documents, and the

SheetCollate

attribute
describes the semantics of collating individual pages within a document.

The effect of a

SheetCollate

attribute on a multidoc print job (a job
with multiple documents) depends on whether all the docs have the same sheet
collation specified or whether different docs have different sheet collations
specified, and on the (perhaps defaulted) value of the

MultipleDocumentHandling

attribute.

- If all the docs have the same sheet collation specified, then the
following combinations of

SheetCollate

and

MultipleDocumentHandling

are permitted,
and the printer reports an error when the job is submitted if any other
combination is specified:

- SheetCollate = COLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT -- All the input docs will be
combined into one output document. Multiple copies of the output document
will be produced with pages in collated order, i.e. pages 1, 2, 3, . . .,
1, 2, 3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT_NEW_SHEET -- All the input
docs will be combined into one output document, and the first impression
of each input doc will always start on a new media sheet. Multiple copies
of the output document will be produced with pages in collated order,
i.e. pages 1, 2, 3, . . ., 1, 2, 3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in collated order, but the documents themselves in
uncollated order, i.e. pages A1, A2, A3, . . ., A1, A2, A3, . . ., B1,
B2, B3, . . ., B1, B2, B3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_COLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in collated order, with the documents themselves also in
collated order, i.e. pages A1, A2, A3, . . ., B1, B2, B3, . . ., A1, A2,
A3, . . ., B1, B2, B3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT -- All the input docs will be
combined into one output document. Multiple copies of the output document
will be produced with pages in uncollated order, i.e. pages 1, 1, . . .,
2, 2, . . ., 3, 3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT_NEW_SHEET -- All the input
docs will be combined into one output document, and the first impression
of each input doc will always start on a new media sheet. Multiple copies
of the output document will be produced with pages in uncollated order,
i.e. pages 1, 1, . . ., 2, 2, . . ., 3, 3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in uncollated order, with the documents themselves also
in uncollated order, i.e. pages A1, A1, . . ., A2, A2, . . ., A3, A3, . .
., B1, B1, . . ., B2, B2, . . ., B3, B3, . . .

If different docs have different sheet collations specified, then only
one value of

MultipleDocumentHandling

is
permitted, and the printer reports an error when the job is submitted if
any other value is specified:

- MultipleDocumentHandling

=
SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each input doc will remain a
separate output document. Multiple copies of each output document (call
them A, B, . . .) will be produced with each document's pages in collated
or uncollated order as the corresponding input doc's SheetCollate
attribute specifies, and with the documents themselves in uncollated
order. If document A had SheetCollate = UNCOLLATED and document B had
SheetCollate = COLLATED, the following pages would be produced: A1, A1, .
. ., A2, A2, . . ., A3, A3, . . ., B1, B2, B3, . . ., B1, B2, B3, . . .

IPP Compatibility:

SheetCollate is not an IPP attribute at present.

**See Also:** MultipleDocumentHandling

,

Serialized Form

public final class

SheetCollate

extends

EnumSyntax

implements

DocAttribute

,

PrintRequestAttribute

,

PrintJobAttribute

Class

SheetCollate

is a printing attribute class, an enumeration,
that specifies whether or not the media sheets of each copy of each printed
document in a job are to be in sequence, when multiple copies of the document
are specified by the

Copies

attribute. When

SheetCollate

is

COLLATED

, each copy of each document is
printed with the print-stream sheets in sequence. When

SheetCollate

is

UNCOLLATED

, each print-stream sheet is printed a number of times
equal to the value of the

Copies

attribute in succession. For
example, suppose a document produces two media sheets as output,

Copies

is 6, and

SheetCollate

is UNCOLLATED; in this
case six copies of the first media sheet are printed followed by six copies
of the second media sheet.

Whether the effect of sheet collation is achieved by placing copies of a
document in multiple output bins or in the same output bin with
implementation defined document separation is implementation dependent. Also
whether it is achieved by making multiple passes over the job or by using an
output sorter is implementation dependent.

If a printer does not support the

SheetCollate

attribute (meaning the
client cannot specify any particular sheet collation), the printer must
behave as though

SheetCollate

were always set to

COLLATED

.

The

SheetCollate

attribute interacts with the

MultipleDocumentHandling

attribute. The

MultipleDocumentHandling

attribute describes
the collation of entire documents, and the

SheetCollate

attribute
describes the semantics of collating individual pages within a document.

The effect of a

SheetCollate

attribute on a multidoc print job (a job
with multiple documents) depends on whether all the docs have the same sheet
collation specified or whether different docs have different sheet collations
specified, and on the (perhaps defaulted) value of the

MultipleDocumentHandling

attribute.

- If all the docs have the same sheet collation specified, then the
following combinations of

SheetCollate

and

MultipleDocumentHandling

are permitted,
and the printer reports an error when the job is submitted if any other
combination is specified:

- SheetCollate = COLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT -- All the input docs will be
combined into one output document. Multiple copies of the output document
will be produced with pages in collated order, i.e. pages 1, 2, 3, . . .,
1, 2, 3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT_NEW_SHEET -- All the input
docs will be combined into one output document, and the first impression
of each input doc will always start on a new media sheet. Multiple copies
of the output document will be produced with pages in collated order,
i.e. pages 1, 2, 3, . . ., 1, 2, 3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in collated order, but the documents themselves in
uncollated order, i.e. pages A1, A2, A3, . . ., A1, A2, A3, . . ., B1,
B2, B3, . . ., B1, B2, B3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_COLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in collated order, with the documents themselves also in
collated order, i.e. pages A1, A2, A3, . . ., B1, B2, B3, . . ., A1, A2,
A3, . . ., B1, B2, B3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT -- All the input docs will be
combined into one output document. Multiple copies of the output document
will be produced with pages in uncollated order, i.e. pages 1, 1, . . .,
2, 2, . . ., 3, 3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT_NEW_SHEET -- All the input
docs will be combined into one output document, and the first impression
of each input doc will always start on a new media sheet. Multiple copies
of the output document will be produced with pages in uncollated order,
i.e. pages 1, 1, . . ., 2, 2, . . ., 3, 3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in uncollated order, with the documents themselves also
in uncollated order, i.e. pages A1, A1, . . ., A2, A2, . . ., A3, A3, . .
., B1, B1, . . ., B2, B2, . . ., B3, B3, . . .

If different docs have different sheet collations specified, then only
one value of

MultipleDocumentHandling

is
permitted, and the printer reports an error when the job is submitted if
any other value is specified:

- MultipleDocumentHandling

=
SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each input doc will remain a
separate output document. Multiple copies of each output document (call
them A, B, . . .) will be produced with each document's pages in collated
or uncollated order as the corresponding input doc's SheetCollate
attribute specifies, and with the documents themselves in uncollated
order. If document A had SheetCollate = UNCOLLATED and document B had
SheetCollate = COLLATED, the following pages would be produced: A1, A1, .
. ., A2, A2, . . ., A3, A3, . . ., B1, B2, B3, . . ., B1, B2, B3, . . .

IPP Compatibility:

SheetCollate is not an IPP attribute at present.

Whether the effect of sheet collation is achieved by placing copies of a
document in multiple output bins or in the same output bin with
implementation defined document separation is implementation dependent. Also
whether it is achieved by making multiple passes over the job or by using an
output sorter is implementation dependent.

If a printer does not support the

SheetCollate

attribute (meaning the
client cannot specify any particular sheet collation), the printer must
behave as though

SheetCollate

were always set to

COLLATED

.

The

SheetCollate

attribute interacts with the

MultipleDocumentHandling

attribute. The

MultipleDocumentHandling

attribute describes
the collation of entire documents, and the

SheetCollate

attribute
describes the semantics of collating individual pages within a document.

The effect of a

SheetCollate

attribute on a multidoc print job (a job
with multiple documents) depends on whether all the docs have the same sheet
collation specified or whether different docs have different sheet collations
specified, and on the (perhaps defaulted) value of the

MultipleDocumentHandling

attribute.

- If all the docs have the same sheet collation specified, then the
following combinations of

SheetCollate

and

MultipleDocumentHandling

are permitted,
and the printer reports an error when the job is submitted if any other
combination is specified:

- SheetCollate = COLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT -- All the input docs will be
combined into one output document. Multiple copies of the output document
will be produced with pages in collated order, i.e. pages 1, 2, 3, . . .,
1, 2, 3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT_NEW_SHEET -- All the input
docs will be combined into one output document, and the first impression
of each input doc will always start on a new media sheet. Multiple copies
of the output document will be produced with pages in collated order,
i.e. pages 1, 2, 3, . . ., 1, 2, 3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in collated order, but the documents themselves in
uncollated order, i.e. pages A1, A2, A3, . . ., A1, A2, A3, . . ., B1,
B2, B3, . . ., B1, B2, B3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_COLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in collated order, with the documents themselves also in
collated order, i.e. pages A1, A2, A3, . . ., B1, B2, B3, . . ., A1, A2,
A3, . . ., B1, B2, B3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT -- All the input docs will be
combined into one output document. Multiple copies of the output document
will be produced with pages in uncollated order, i.e. pages 1, 1, . . .,
2, 2, . . ., 3, 3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT_NEW_SHEET -- All the input
docs will be combined into one output document, and the first impression
of each input doc will always start on a new media sheet. Multiple copies
of the output document will be produced with pages in uncollated order,
i.e. pages 1, 1, . . ., 2, 2, . . ., 3, 3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in uncollated order, with the documents themselves also
in uncollated order, i.e. pages A1, A1, . . ., A2, A2, . . ., A3, A3, . .
., B1, B1, . . ., B2, B2, . . ., B3, B3, . . .

If different docs have different sheet collations specified, then only
one value of

MultipleDocumentHandling

is
permitted, and the printer reports an error when the job is submitted if
any other value is specified:

- MultipleDocumentHandling

=
SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each input doc will remain a
separate output document. Multiple copies of each output document (call
them A, B, . . .) will be produced with each document's pages in collated
or uncollated order as the corresponding input doc's SheetCollate
attribute specifies, and with the documents themselves in uncollated
order. If document A had SheetCollate = UNCOLLATED and document B had
SheetCollate = COLLATED, the following pages would be produced: A1, A1, .
. ., A2, A2, . . ., A3, A3, . . ., B1, B2, B3, . . ., B1, B2, B3, . . .

IPP Compatibility:

SheetCollate is not an IPP attribute at present.

If a printer does not support the

SheetCollate

attribute (meaning the
client cannot specify any particular sheet collation), the printer must
behave as though

SheetCollate

were always set to

COLLATED

.

The

SheetCollate

attribute interacts with the

MultipleDocumentHandling

attribute. The

MultipleDocumentHandling

attribute describes
the collation of entire documents, and the

SheetCollate

attribute
describes the semantics of collating individual pages within a document.

The effect of a

SheetCollate

attribute on a multidoc print job (a job
with multiple documents) depends on whether all the docs have the same sheet
collation specified or whether different docs have different sheet collations
specified, and on the (perhaps defaulted) value of the

MultipleDocumentHandling

attribute.

- If all the docs have the same sheet collation specified, then the
following combinations of

SheetCollate

and

MultipleDocumentHandling

are permitted,
and the printer reports an error when the job is submitted if any other
combination is specified:

- SheetCollate = COLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT -- All the input docs will be
combined into one output document. Multiple copies of the output document
will be produced with pages in collated order, i.e. pages 1, 2, 3, . . .,
1, 2, 3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT_NEW_SHEET -- All the input
docs will be combined into one output document, and the first impression
of each input doc will always start on a new media sheet. Multiple copies
of the output document will be produced with pages in collated order,
i.e. pages 1, 2, 3, . . ., 1, 2, 3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in collated order, but the documents themselves in
uncollated order, i.e. pages A1, A2, A3, . . ., A1, A2, A3, . . ., B1,
B2, B3, . . ., B1, B2, B3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_COLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in collated order, with the documents themselves also in
collated order, i.e. pages A1, A2, A3, . . ., B1, B2, B3, . . ., A1, A2,
A3, . . ., B1, B2, B3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT -- All the input docs will be
combined into one output document. Multiple copies of the output document
will be produced with pages in uncollated order, i.e. pages 1, 1, . . .,
2, 2, . . ., 3, 3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT_NEW_SHEET -- All the input
docs will be combined into one output document, and the first impression
of each input doc will always start on a new media sheet. Multiple copies
of the output document will be produced with pages in uncollated order,
i.e. pages 1, 1, . . ., 2, 2, . . ., 3, 3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in uncollated order, with the documents themselves also
in uncollated order, i.e. pages A1, A1, . . ., A2, A2, . . ., A3, A3, . .
., B1, B1, . . ., B2, B2, . . ., B3, B3, . . .

If different docs have different sheet collations specified, then only
one value of

MultipleDocumentHandling

is
permitted, and the printer reports an error when the job is submitted if
any other value is specified:

- MultipleDocumentHandling

=
SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each input doc will remain a
separate output document. Multiple copies of each output document (call
them A, B, . . .) will be produced with each document's pages in collated
or uncollated order as the corresponding input doc's SheetCollate
attribute specifies, and with the documents themselves in uncollated
order. If document A had SheetCollate = UNCOLLATED and document B had
SheetCollate = COLLATED, the following pages would be produced: A1, A1, .
. ., A2, A2, . . ., A3, A3, . . ., B1, B2, B3, . . ., B1, B2, B3, . . .

IPP Compatibility:

SheetCollate is not an IPP attribute at present.

The

SheetCollate

attribute interacts with the

MultipleDocumentHandling

attribute. The

MultipleDocumentHandling

attribute describes
the collation of entire documents, and the

SheetCollate

attribute
describes the semantics of collating individual pages within a document.

The effect of a

SheetCollate

attribute on a multidoc print job (a job
with multiple documents) depends on whether all the docs have the same sheet
collation specified or whether different docs have different sheet collations
specified, and on the (perhaps defaulted) value of the

MultipleDocumentHandling

attribute.

- If all the docs have the same sheet collation specified, then the
following combinations of

SheetCollate

and

MultipleDocumentHandling

are permitted,
and the printer reports an error when the job is submitted if any other
combination is specified:

- SheetCollate = COLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT -- All the input docs will be
combined into one output document. Multiple copies of the output document
will be produced with pages in collated order, i.e. pages 1, 2, 3, . . .,
1, 2, 3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT_NEW_SHEET -- All the input
docs will be combined into one output document, and the first impression
of each input doc will always start on a new media sheet. Multiple copies
of the output document will be produced with pages in collated order,
i.e. pages 1, 2, 3, . . ., 1, 2, 3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in collated order, but the documents themselves in
uncollated order, i.e. pages A1, A2, A3, . . ., A1, A2, A3, . . ., B1,
B2, B3, . . ., B1, B2, B3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_COLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in collated order, with the documents themselves also in
collated order, i.e. pages A1, A2, A3, . . ., B1, B2, B3, . . ., A1, A2,
A3, . . ., B1, B2, B3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT -- All the input docs will be
combined into one output document. Multiple copies of the output document
will be produced with pages in uncollated order, i.e. pages 1, 1, . . .,
2, 2, . . ., 3, 3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT_NEW_SHEET -- All the input
docs will be combined into one output document, and the first impression
of each input doc will always start on a new media sheet. Multiple copies
of the output document will be produced with pages in uncollated order,
i.e. pages 1, 1, . . ., 2, 2, . . ., 3, 3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in uncollated order, with the documents themselves also
in uncollated order, i.e. pages A1, A1, . . ., A2, A2, . . ., A3, A3, . .
., B1, B1, . . ., B2, B2, . . ., B3, B3, . . .

If different docs have different sheet collations specified, then only
one value of

MultipleDocumentHandling

is
permitted, and the printer reports an error when the job is submitted if
any other value is specified:

- MultipleDocumentHandling

=
SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each input doc will remain a
separate output document. Multiple copies of each output document (call
them A, B, . . .) will be produced with each document's pages in collated
or uncollated order as the corresponding input doc's SheetCollate
attribute specifies, and with the documents themselves in uncollated
order. If document A had SheetCollate = UNCOLLATED and document B had
SheetCollate = COLLATED, the following pages would be produced: A1, A1, .
. ., A2, A2, . . ., A3, A3, . . ., B1, B2, B3, . . ., B1, B2, B3, . . .

IPP Compatibility:

SheetCollate is not an IPP attribute at present.

The effect of a

SheetCollate

attribute on a multidoc print job (a job
with multiple documents) depends on whether all the docs have the same sheet
collation specified or whether different docs have different sheet collations
specified, and on the (perhaps defaulted) value of the

MultipleDocumentHandling

attribute.

- If all the docs have the same sheet collation specified, then the
following combinations of

SheetCollate

and

MultipleDocumentHandling

are permitted,
and the printer reports an error when the job is submitted if any other
combination is specified:

- SheetCollate = COLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT -- All the input docs will be
combined into one output document. Multiple copies of the output document
will be produced with pages in collated order, i.e. pages 1, 2, 3, . . .,
1, 2, 3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT_NEW_SHEET -- All the input
docs will be combined into one output document, and the first impression
of each input doc will always start on a new media sheet. Multiple copies
of the output document will be produced with pages in collated order,
i.e. pages 1, 2, 3, . . ., 1, 2, 3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in collated order, but the documents themselves in
uncollated order, i.e. pages A1, A2, A3, . . ., A1, A2, A3, . . ., B1,
B2, B3, . . ., B1, B2, B3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_COLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in collated order, with the documents themselves also in
collated order, i.e. pages A1, A2, A3, . . ., B1, B2, B3, . . ., A1, A2,
A3, . . ., B1, B2, B3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT -- All the input docs will be
combined into one output document. Multiple copies of the output document
will be produced with pages in uncollated order, i.e. pages 1, 1, . . .,
2, 2, . . ., 3, 3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT_NEW_SHEET -- All the input
docs will be combined into one output document, and the first impression
of each input doc will always start on a new media sheet. Multiple copies
of the output document will be produced with pages in uncollated order,
i.e. pages 1, 1, . . ., 2, 2, . . ., 3, 3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in uncollated order, with the documents themselves also
in uncollated order, i.e. pages A1, A1, . . ., A2, A2, . . ., A3, A3, . .
., B1, B1, . . ., B2, B2, . . ., B3, B3, . . .

If different docs have different sheet collations specified, then only
one value of

MultipleDocumentHandling

is
permitted, and the printer reports an error when the job is submitted if
any other value is specified:

- MultipleDocumentHandling

=
SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each input doc will remain a
separate output document. Multiple copies of each output document (call
them A, B, . . .) will be produced with each document's pages in collated
or uncollated order as the corresponding input doc's SheetCollate
attribute specifies, and with the documents themselves in uncollated
order. If document A had SheetCollate = UNCOLLATED and document B had
SheetCollate = COLLATED, the following pages would be produced: A1, A1, .
. ., A2, A2, . . ., A3, A3, . . ., B1, B2, B3, . . ., B1, B2, B3, . . .

IPP Compatibility:

SheetCollate is not an IPP attribute at present.

If all the docs have the same sheet collation specified, then the
following combinations of

SheetCollate

and

MultipleDocumentHandling

are permitted,
and the printer reports an error when the job is submitted if any other
combination is specified:

- SheetCollate = COLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT -- All the input docs will be
combined into one output document. Multiple copies of the output document
will be produced with pages in collated order, i.e. pages 1, 2, 3, . . .,
1, 2, 3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT_NEW_SHEET -- All the input
docs will be combined into one output document, and the first impression
of each input doc will always start on a new media sheet. Multiple copies
of the output document will be produced with pages in collated order,
i.e. pages 1, 2, 3, . . ., 1, 2, 3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in collated order, but the documents themselves in
uncollated order, i.e. pages A1, A2, A3, . . ., A1, A2, A3, . . ., B1,
B2, B3, . . ., B1, B2, B3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_COLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in collated order, with the documents themselves also in
collated order, i.e. pages A1, A2, A3, . . ., B1, B2, B3, . . ., A1, A2,
A3, . . ., B1, B2, B3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT -- All the input docs will be
combined into one output document. Multiple copies of the output document
will be produced with pages in uncollated order, i.e. pages 1, 1, . . .,
2, 2, . . ., 3, 3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT_NEW_SHEET -- All the input
docs will be combined into one output document, and the first impression
of each input doc will always start on a new media sheet. Multiple copies
of the output document will be produced with pages in uncollated order,
i.e. pages 1, 1, . . ., 2, 2, . . ., 3, 3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in uncollated order, with the documents themselves also
in uncollated order, i.e. pages A1, A1, . . ., A2, A2, . . ., A3, A3, . .
., B1, B1, . . ., B2, B2, . . ., B3, B3, . . .

If different docs have different sheet collations specified, then only
one value of

MultipleDocumentHandling

is
permitted, and the printer reports an error when the job is submitted if
any other value is specified:

- MultipleDocumentHandling

=
SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each input doc will remain a
separate output document. Multiple copies of each output document (call
them A, B, . . .) will be produced with each document's pages in collated
or uncollated order as the corresponding input doc's SheetCollate
attribute specifies, and with the documents themselves in uncollated
order. If document A had SheetCollate = UNCOLLATED and document B had
SheetCollate = COLLATED, the following pages would be produced: A1, A1, .
. ., A2, A2, . . ., A3, A3, . . ., B1, B2, B3, . . ., B1, B2, B3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT -- All the input docs will be
combined into one output document. Multiple copies of the output document
will be produced with pages in collated order, i.e. pages 1, 2, 3, . . .,
1, 2, 3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT_NEW_SHEET -- All the input
docs will be combined into one output document, and the first impression
of each input doc will always start on a new media sheet. Multiple copies
of the output document will be produced with pages in collated order,
i.e. pages 1, 2, 3, . . ., 1, 2, 3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in collated order, but the documents themselves in
uncollated order, i.e. pages A1, A2, A3, . . ., A1, A2, A3, . . ., B1,
B2, B3, . . ., B1, B2, B3, . . .

SheetCollate = COLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_COLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in collated order, with the documents themselves also in
collated order, i.e. pages A1, A2, A3, . . ., B1, B2, B3, . . ., A1, A2,
A3, . . ., B1, B2, B3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT -- All the input docs will be
combined into one output document. Multiple copies of the output document
will be produced with pages in uncollated order, i.e. pages 1, 1, . . .,
2, 2, . . ., 3, 3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SINGLE_DOCUMENT_NEW_SHEET -- All the input
docs will be combined into one output document, and the first impression
of each input doc will always start on a new media sheet. Multiple copies
of the output document will be produced with pages in uncollated order,
i.e. pages 1, 1, . . ., 2, 2, . . ., 3, 3, . . .

SheetCollate = UNCOLLATED,

MultipleDocumentHandling

= SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each
input doc will remain a separate output document. Multiple copies of each
output document (call them A, B, . . .) will be produced with each
document's pages in uncollated order, with the documents themselves also
in uncollated order, i.e. pages A1, A1, . . ., A2, A2, . . ., A3, A3, . .
., B1, B1, . . ., B2, B2, . . ., B3, B3, . . .

MultipleDocumentHandling

=
SEPARATE_DOCUMENTS_UNCOLLATED_COPIES -- Each input doc will remain a
separate output document. Multiple copies of each output document (call
them A, B, . . .) will be produced with each document's pages in collated
or uncollated order as the corresponding input doc's SheetCollate
attribute specifies, and with the documents themselves in uncollated
order. If document A had SheetCollate = UNCOLLATED and document B had
SheetCollate = COLLATED, the following pages would be produced: A1, A1, .
. ., A2, A2, . . ., A3, A3, . . ., B1, B2, B3, . . ., B1, B2, B3, . . .

IPP Compatibility:

SheetCollate is not an IPP attribute at present.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

SheetCollate

COLLATED

Sheets within a document appear in collated order when multiple copies
are printed.

static

SheetCollate

UNCOLLATED

Sheets within a document appear in uncollated order when multiple copies
are printed.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SheetCollate

​(int value)

Construct a new sheet collate enumeration value with the given integer
value.

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

SheetCollate

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

SheetCollate

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

SheetCollate

COLLATED

Sheets within a document appear in collated order when multiple copies
are printed.

static

SheetCollate

UNCOLLATED

Sheets within a document appear in uncollated order when multiple copies
are printed.

---

#### Field Summary

Sheets within a document appear in collated order when multiple copies
are printed.

Sheets within a document appear in uncollated order when multiple copies
are printed.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SheetCollate

​(int value)

Construct a new sheet collate enumeration value with the given integer
value.

---

#### Constructor Summary

Construct a new sheet collate enumeration value with the given integer
value.

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

SheetCollate

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

SheetCollate

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

SheetCollate

.

Get the name of the category of which this attribute value is an
instance.

Returns the string table for class

SheetCollate

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

- UNCOLLATED

```java
public static final
SheetCollate
UNCOLLATED
```

Sheets within a document appear in uncollated order when multiple copies
are printed.

- COLLATED

```java
public static final
SheetCollate
COLLATED
```

Sheets within a document appear in collated order when multiple copies
are printed.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SheetCollate

```java
protected SheetCollate​(int value)
```

Construct a new sheet collate enumeration value with the given integer
value.

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

SheetCollate

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

SheetCollate

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

SheetCollate

, the category is class

SheetCollate

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

SheetCollate

, the category name is

"sheet-collate"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Field Detail

- UNCOLLATED

```java
public static final
SheetCollate
UNCOLLATED
```

Sheets within a document appear in uncollated order when multiple copies
are printed.

- COLLATED

```java
public static final
SheetCollate
COLLATED
```

Sheets within a document appear in collated order when multiple copies
are printed.

---

#### Field Detail

UNCOLLATED

```java
public static final
SheetCollate
UNCOLLATED
```

Sheets within a document appear in uncollated order when multiple copies
are printed.

---

#### UNCOLLATED

public static final

SheetCollate

UNCOLLATED

Sheets within a document appear in uncollated order when multiple copies
are printed.

COLLATED

```java
public static final
SheetCollate
COLLATED
```

Sheets within a document appear in collated order when multiple copies
are printed.

---

#### COLLATED

public static final

SheetCollate

COLLATED

Sheets within a document appear in collated order when multiple copies
are printed.

Constructor Detail

- SheetCollate

```java
protected SheetCollate​(int value)
```

Construct a new sheet collate enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

SheetCollate

```java
protected SheetCollate​(int value)
```

Construct a new sheet collate enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### SheetCollate

protected SheetCollate​(int value)

Construct a new sheet collate enumeration value with the given integer
value.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

SheetCollate

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

SheetCollate

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

SheetCollate

, the category is class

SheetCollate

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

SheetCollate

, the category name is

"sheet-collate"

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

SheetCollate

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

SheetCollate

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

SheetCollate

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

SheetCollate

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

SheetCollate

, the category is class

SheetCollate

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

SheetCollate

, the category is class

SheetCollate

itself.

For class

SheetCollate

, the category is class

SheetCollate

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

SheetCollate

, the category name is

"sheet-collate"

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

SheetCollate

, the category name is

"sheet-collate"

.

For class

SheetCollate

, the category name is

"sheet-collate"

.

---

