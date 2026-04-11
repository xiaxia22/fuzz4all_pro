# Class MultipleDocumentHandling

**Source:** `java.desktop\javax\print\attribute\standard\MultipleDocumentHandling.html`

### Class Description

```java
public class
MultipleDocumentHandling

extends
EnumSyntax

implements
PrintRequestAttribute
,
PrintJobAttribute
```

Class

MultipleDocumentHandling

is a printing attribute class, an
enumeration, that controls finishing operations and the placement of one or
more print-stream pages into impressions and onto media sheets. When the
value of the

Copies

attribute exceeds 1,

MultipleDocumentHandling

also controls the order in which the copies
that result from processing the documents are produced. This attribute is
relevant only for a multidoc print job consisting of two or more individual
docs.

Briefly,

MultipleDocumentHandling

determines the relationship between
the multiple input (electronic) documents fed into a multidoc print job and
the output (physical) document or documents produced by the multidoc print
job.
There are two possibilities:

- The multiple input documents are combined into a single output
document. Finishing operations (

Finishings

), are
performed on this single output document. The

Copies

attribute tells how many copies of this single output document to produce.
The

MultipleDocumentHandling

values

SINGLE_DOCUMENT

and

SINGLE_DOCUMENT_NEW_SHEET

specify two variations of this
possibility.

The multiple input documents remain separate output documents.
Finishing operations (

Finishings

), are performed on each
output document separately. The

Copies

attribute tells how
many copies of each separate output document to produce. The

MultipleDocumentHandling

values

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

and

SEPARATE_DOCUMENTS_COLLATED_COPIES

specify two variations of this
possibility.

In the detailed explanations below, if "

a

" represents an instance of
document data, then the result of processing the data in document "

a

"
is a sequence of media sheets represented by "

a(*)

".

The standard

MultipleDocumentHandling

values are:

- SINGLE_DOCUMENT

. If a
print job has multiple documents -- say, the document data is called

a

and

b

-- then the result of processing all the document
data (

a

and then

b

) must be treated as a single sequence of
media sheets for finishing operations; that is, finishing would be
performed on the concatenation of the sequences

a(*),b(*)

. The
printer must not force the data in each document instance to be formatted
onto a new print-stream page, nor to start a new impression on a new media
sheet. If more than one copy is made, the ordering of the sets of media
sheets resulting from processing the document data must be

a(*),b(*),a(*),b(*),...

, and the printer object must force each
copy (

a(*),b(*)

) to start on a new media sheet.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

. If a print job has multiple
documents -- say, the document data is called

a

and

b

--
then the result of processing the data in each document instance must be
treated as a single sequence of media sheets for finishing operations; that
is, the sets

a(*)

and

b(*)

would each be finished
separately. The printer must force each copy of the result of processing
the data in a single document to start on a new media sheet. If more than
one copy is made, the ordering of the sets of media sheets resulting from
processing the document data must be

a(*),a(*),...,b(*),b(*)...

.

SEPARATE_DOCUMENTS_COLLATED_COPIES

. If a print job has multiple
documents -- say, the document data is called

a

and

b

--
then the result of processing the data in each document instance must be
treated as a single sequence of media sheets for finishing operations; that
is, the sets

a(*)

and

b(*)

would each be finished
separately. The printer must force each copy of the result of processing
the data in a single document to start on a new media sheet. If more than
one copy is made, the ordering of the sets of media sheets resulting from
processing the document data must be

a(*),b(*),a(*),b(*),...

.

SINGLE_DOCUMENT_NEW_SHEET

. Same as SINGLE_DOCUMENT, except that the
printer must ensure that the first impression of each document instance in
the job is placed on a new media sheet. This value allows multiple
documents to be stapled together with a single staple where each document
starts on a new sheet.

SINGLE_DOCUMENT

is the same as

SEPARATE_DOCUMENTS_COLLATED_COPIES

with respect to ordering of
print-stream pages, but not media sheet generation, since

SINGLE_DOCUMENT

will put the first page of the next document on the
back side of a sheet if an odd number of pages have been produced so far for
the job, while

SEPARATE_DOCUMENTS_COLLATED_COPIES

always forces the
next document or document copy on to a new sheet.

In addition, if a

Finishings

attribute of

STAPLE

is specified, then:

- With

SINGLE_DOCUMENT

, documents

a

and

b

are
stapled together as a single document with no regard to new sheets.

With

SINGLE_DOCUMENT_NEW_SHEET

, documents

a

and

b

are stapled together as a single document, but document

b

starts on a new sheet.

With

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

and

SEPARATE_DOCUMENTS_COLLATED_COPIES

, documents

a

and

b

are stapled separately.

Note:

None of these values provide means to produce uncollated sheets
within a document, i.e., where multiple copies of sheet

n

are produced
before sheet

n

+1 of the same document. To specify that, see the

SheetCollate

attribute.

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

PrintJobAttribute

,

PrintRequestAttribute

---

### Field Details

#### public static final
MultipleDocumentHandling
SINGLE_DOCUMENT

Single document -- see above for

further information

.

---

#### public static final
MultipleDocumentHandling
SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

Separate documents uncollated copies -- see above for

further information

.

---

#### public static final
MultipleDocumentHandling
SEPARATE_DOCUMENTS_COLLATED_COPIES

Separate documents collated copies -- see above for

further information

.

---

#### public static final
MultipleDocumentHandling
SINGLE_DOCUMENT_NEW_SHEET

Single document new sheet -- see above for

further
information

.

---

### Constructor Details

#### protected MultipleDocumentHandling​(int value)

Construct a new multiple document handling enumeration value with the
given integer value.

**Parameters:**
- value

- Integer value

---

### Method Details

#### protected
String
[] getStringTable()

Returns the string table for class

MultipleDocumentHandling

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

MultipleDocumentHandling

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

MultipleDocumentHandling

and any vendor-defined
subclasses, the category is class

MultipleDocumentHandling

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

MultipleDocumentHandling

and any vendor-defined
subclasses, the category name is

"multiple-document-handling"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class MultipleDocumentHandling

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.MultipleDocumentHandling

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.MultipleDocumentHandling

javax.print.attribute.standard.MultipleDocumentHandling

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

,

PrintRequestAttribute

```java
public class
MultipleDocumentHandling

extends
EnumSyntax

implements
PrintRequestAttribute
,
PrintJobAttribute
```

Class

MultipleDocumentHandling

is a printing attribute class, an
enumeration, that controls finishing operations and the placement of one or
more print-stream pages into impressions and onto media sheets. When the
value of the

Copies

attribute exceeds 1,

MultipleDocumentHandling

also controls the order in which the copies
that result from processing the documents are produced. This attribute is
relevant only for a multidoc print job consisting of two or more individual
docs.

Briefly,

MultipleDocumentHandling

determines the relationship between
the multiple input (electronic) documents fed into a multidoc print job and
the output (physical) document or documents produced by the multidoc print
job.
There are two possibilities:

- The multiple input documents are combined into a single output
document. Finishing operations (

Finishings

), are
performed on this single output document. The

Copies

attribute tells how many copies of this single output document to produce.
The

MultipleDocumentHandling

values

SINGLE_DOCUMENT

and

SINGLE_DOCUMENT_NEW_SHEET

specify two variations of this
possibility.

The multiple input documents remain separate output documents.
Finishing operations (

Finishings

), are performed on each
output document separately. The

Copies

attribute tells how
many copies of each separate output document to produce. The

MultipleDocumentHandling

values

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

and

SEPARATE_DOCUMENTS_COLLATED_COPIES

specify two variations of this
possibility.

In the detailed explanations below, if "

a

" represents an instance of
document data, then the result of processing the data in document "

a

"
is a sequence of media sheets represented by "

a(*)

".

The standard

MultipleDocumentHandling

values are:

- SINGLE_DOCUMENT

. If a
print job has multiple documents -- say, the document data is called

a

and

b

-- then the result of processing all the document
data (

a

and then

b

) must be treated as a single sequence of
media sheets for finishing operations; that is, finishing would be
performed on the concatenation of the sequences

a(*),b(*)

. The
printer must not force the data in each document instance to be formatted
onto a new print-stream page, nor to start a new impression on a new media
sheet. If more than one copy is made, the ordering of the sets of media
sheets resulting from processing the document data must be

a(*),b(*),a(*),b(*),...

, and the printer object must force each
copy (

a(*),b(*)

) to start on a new media sheet.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

. If a print job has multiple
documents -- say, the document data is called

a

and

b

--
then the result of processing the data in each document instance must be
treated as a single sequence of media sheets for finishing operations; that
is, the sets

a(*)

and

b(*)

would each be finished
separately. The printer must force each copy of the result of processing
the data in a single document to start on a new media sheet. If more than
one copy is made, the ordering of the sets of media sheets resulting from
processing the document data must be

a(*),a(*),...,b(*),b(*)...

.

SEPARATE_DOCUMENTS_COLLATED_COPIES

. If a print job has multiple
documents -- say, the document data is called

a

and

b

--
then the result of processing the data in each document instance must be
treated as a single sequence of media sheets for finishing operations; that
is, the sets

a(*)

and

b(*)

would each be finished
separately. The printer must force each copy of the result of processing
the data in a single document to start on a new media sheet. If more than
one copy is made, the ordering of the sets of media sheets resulting from
processing the document data must be

a(*),b(*),a(*),b(*),...

.

SINGLE_DOCUMENT_NEW_SHEET

. Same as SINGLE_DOCUMENT, except that the
printer must ensure that the first impression of each document instance in
the job is placed on a new media sheet. This value allows multiple
documents to be stapled together with a single staple where each document
starts on a new sheet.

SINGLE_DOCUMENT

is the same as

SEPARATE_DOCUMENTS_COLLATED_COPIES

with respect to ordering of
print-stream pages, but not media sheet generation, since

SINGLE_DOCUMENT

will put the first page of the next document on the
back side of a sheet if an odd number of pages have been produced so far for
the job, while

SEPARATE_DOCUMENTS_COLLATED_COPIES

always forces the
next document or document copy on to a new sheet.

In addition, if a

Finishings

attribute of

STAPLE

is specified, then:

- With

SINGLE_DOCUMENT

, documents

a

and

b

are
stapled together as a single document with no regard to new sheets.

With

SINGLE_DOCUMENT_NEW_SHEET

, documents

a

and

b

are stapled together as a single document, but document

b

starts on a new sheet.

With

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

and

SEPARATE_DOCUMENTS_COLLATED_COPIES

, documents

a

and

b

are stapled separately.

Note:

None of these values provide means to produce uncollated sheets
within a document, i.e., where multiple copies of sheet

n

are produced
before sheet

n

+1 of the same document. To specify that, see the

SheetCollate

attribute.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

**See Also:** Copies

,

Finishings

,

NumberUp

,

PageRanges

,

SheetCollate

,

Sides

,

Serialized Form

public class

MultipleDocumentHandling

extends

EnumSyntax

implements

PrintRequestAttribute

,

PrintJobAttribute

Class

MultipleDocumentHandling

is a printing attribute class, an
enumeration, that controls finishing operations and the placement of one or
more print-stream pages into impressions and onto media sheets. When the
value of the

Copies

attribute exceeds 1,

MultipleDocumentHandling

also controls the order in which the copies
that result from processing the documents are produced. This attribute is
relevant only for a multidoc print job consisting of two or more individual
docs.

Briefly,

MultipleDocumentHandling

determines the relationship between
the multiple input (electronic) documents fed into a multidoc print job and
the output (physical) document or documents produced by the multidoc print
job.
There are two possibilities:

- The multiple input documents are combined into a single output
document. Finishing operations (

Finishings

), are
performed on this single output document. The

Copies

attribute tells how many copies of this single output document to produce.
The

MultipleDocumentHandling

values

SINGLE_DOCUMENT

and

SINGLE_DOCUMENT_NEW_SHEET

specify two variations of this
possibility.

The multiple input documents remain separate output documents.
Finishing operations (

Finishings

), are performed on each
output document separately. The

Copies

attribute tells how
many copies of each separate output document to produce. The

MultipleDocumentHandling

values

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

and

SEPARATE_DOCUMENTS_COLLATED_COPIES

specify two variations of this
possibility.

In the detailed explanations below, if "

a

" represents an instance of
document data, then the result of processing the data in document "

a

"
is a sequence of media sheets represented by "

a(*)

".

The standard

MultipleDocumentHandling

values are:

- SINGLE_DOCUMENT

. If a
print job has multiple documents -- say, the document data is called

a

and

b

-- then the result of processing all the document
data (

a

and then

b

) must be treated as a single sequence of
media sheets for finishing operations; that is, finishing would be
performed on the concatenation of the sequences

a(*),b(*)

. The
printer must not force the data in each document instance to be formatted
onto a new print-stream page, nor to start a new impression on a new media
sheet. If more than one copy is made, the ordering of the sets of media
sheets resulting from processing the document data must be

a(*),b(*),a(*),b(*),...

, and the printer object must force each
copy (

a(*),b(*)

) to start on a new media sheet.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

. If a print job has multiple
documents -- say, the document data is called

a

and

b

--
then the result of processing the data in each document instance must be
treated as a single sequence of media sheets for finishing operations; that
is, the sets

a(*)

and

b(*)

would each be finished
separately. The printer must force each copy of the result of processing
the data in a single document to start on a new media sheet. If more than
one copy is made, the ordering of the sets of media sheets resulting from
processing the document data must be

a(*),a(*),...,b(*),b(*)...

.

SEPARATE_DOCUMENTS_COLLATED_COPIES

. If a print job has multiple
documents -- say, the document data is called

a

and

b

--
then the result of processing the data in each document instance must be
treated as a single sequence of media sheets for finishing operations; that
is, the sets

a(*)

and

b(*)

would each be finished
separately. The printer must force each copy of the result of processing
the data in a single document to start on a new media sheet. If more than
one copy is made, the ordering of the sets of media sheets resulting from
processing the document data must be

a(*),b(*),a(*),b(*),...

.

SINGLE_DOCUMENT_NEW_SHEET

. Same as SINGLE_DOCUMENT, except that the
printer must ensure that the first impression of each document instance in
the job is placed on a new media sheet. This value allows multiple
documents to be stapled together with a single staple where each document
starts on a new sheet.

SINGLE_DOCUMENT

is the same as

SEPARATE_DOCUMENTS_COLLATED_COPIES

with respect to ordering of
print-stream pages, but not media sheet generation, since

SINGLE_DOCUMENT

will put the first page of the next document on the
back side of a sheet if an odd number of pages have been produced so far for
the job, while

SEPARATE_DOCUMENTS_COLLATED_COPIES

always forces the
next document or document copy on to a new sheet.

In addition, if a

Finishings

attribute of

STAPLE

is specified, then:

- With

SINGLE_DOCUMENT

, documents

a

and

b

are
stapled together as a single document with no regard to new sheets.

With

SINGLE_DOCUMENT_NEW_SHEET

, documents

a

and

b

are stapled together as a single document, but document

b

starts on a new sheet.

With

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

and

SEPARATE_DOCUMENTS_COLLATED_COPIES

, documents

a

and

b

are stapled separately.

Note:

None of these values provide means to produce uncollated sheets
within a document, i.e., where multiple copies of sheet

n

are produced
before sheet

n

+1 of the same document. To specify that, see the

SheetCollate

attribute.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

Briefly,

MultipleDocumentHandling

determines the relationship between
the multiple input (electronic) documents fed into a multidoc print job and
the output (physical) document or documents produced by the multidoc print
job.
There are two possibilities:

- The multiple input documents are combined into a single output
document. Finishing operations (

Finishings

), are
performed on this single output document. The

Copies

attribute tells how many copies of this single output document to produce.
The

MultipleDocumentHandling

values

SINGLE_DOCUMENT

and

SINGLE_DOCUMENT_NEW_SHEET

specify two variations of this
possibility.

The multiple input documents remain separate output documents.
Finishing operations (

Finishings

), are performed on each
output document separately. The

Copies

attribute tells how
many copies of each separate output document to produce. The

MultipleDocumentHandling

values

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

and

SEPARATE_DOCUMENTS_COLLATED_COPIES

specify two variations of this
possibility.

In the detailed explanations below, if "

a

" represents an instance of
document data, then the result of processing the data in document "

a

"
is a sequence of media sheets represented by "

a(*)

".

The standard

MultipleDocumentHandling

values are:

- SINGLE_DOCUMENT

. If a
print job has multiple documents -- say, the document data is called

a

and

b

-- then the result of processing all the document
data (

a

and then

b

) must be treated as a single sequence of
media sheets for finishing operations; that is, finishing would be
performed on the concatenation of the sequences

a(*),b(*)

. The
printer must not force the data in each document instance to be formatted
onto a new print-stream page, nor to start a new impression on a new media
sheet. If more than one copy is made, the ordering of the sets of media
sheets resulting from processing the document data must be

a(*),b(*),a(*),b(*),...

, and the printer object must force each
copy (

a(*),b(*)

) to start on a new media sheet.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

. If a print job has multiple
documents -- say, the document data is called

a

and

b

--
then the result of processing the data in each document instance must be
treated as a single sequence of media sheets for finishing operations; that
is, the sets

a(*)

and

b(*)

would each be finished
separately. The printer must force each copy of the result of processing
the data in a single document to start on a new media sheet. If more than
one copy is made, the ordering of the sets of media sheets resulting from
processing the document data must be

a(*),a(*),...,b(*),b(*)...

.

SEPARATE_DOCUMENTS_COLLATED_COPIES

. If a print job has multiple
documents -- say, the document data is called

a

and

b

--
then the result of processing the data in each document instance must be
treated as a single sequence of media sheets for finishing operations; that
is, the sets

a(*)

and

b(*)

would each be finished
separately. The printer must force each copy of the result of processing
the data in a single document to start on a new media sheet. If more than
one copy is made, the ordering of the sets of media sheets resulting from
processing the document data must be

a(*),b(*),a(*),b(*),...

.

SINGLE_DOCUMENT_NEW_SHEET

. Same as SINGLE_DOCUMENT, except that the
printer must ensure that the first impression of each document instance in
the job is placed on a new media sheet. This value allows multiple
documents to be stapled together with a single staple where each document
starts on a new sheet.

SINGLE_DOCUMENT

is the same as

SEPARATE_DOCUMENTS_COLLATED_COPIES

with respect to ordering of
print-stream pages, but not media sheet generation, since

SINGLE_DOCUMENT

will put the first page of the next document on the
back side of a sheet if an odd number of pages have been produced so far for
the job, while

SEPARATE_DOCUMENTS_COLLATED_COPIES

always forces the
next document or document copy on to a new sheet.

In addition, if a

Finishings

attribute of

STAPLE

is specified, then:

- With

SINGLE_DOCUMENT

, documents

a

and

b

are
stapled together as a single document with no regard to new sheets.

With

SINGLE_DOCUMENT_NEW_SHEET

, documents

a

and

b

are stapled together as a single document, but document

b

starts on a new sheet.

With

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

and

SEPARATE_DOCUMENTS_COLLATED_COPIES

, documents

a

and

b

are stapled separately.

Note:

None of these values provide means to produce uncollated sheets
within a document, i.e., where multiple copies of sheet

n

are produced
before sheet

n

+1 of the same document. To specify that, see the

SheetCollate

attribute.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

The multiple input documents are combined into a single output
document. Finishing operations (

Finishings

), are
performed on this single output document. The

Copies

attribute tells how many copies of this single output document to produce.
The

MultipleDocumentHandling

values

SINGLE_DOCUMENT

and

SINGLE_DOCUMENT_NEW_SHEET

specify two variations of this
possibility.

The multiple input documents remain separate output documents.
Finishing operations (

Finishings

), are performed on each
output document separately. The

Copies

attribute tells how
many copies of each separate output document to produce. The

MultipleDocumentHandling

values

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

and

SEPARATE_DOCUMENTS_COLLATED_COPIES

specify two variations of this
possibility.

The standard

MultipleDocumentHandling

values are:

- SINGLE_DOCUMENT

. If a
print job has multiple documents -- say, the document data is called

a

and

b

-- then the result of processing all the document
data (

a

and then

b

) must be treated as a single sequence of
media sheets for finishing operations; that is, finishing would be
performed on the concatenation of the sequences

a(*),b(*)

. The
printer must not force the data in each document instance to be formatted
onto a new print-stream page, nor to start a new impression on a new media
sheet. If more than one copy is made, the ordering of the sets of media
sheets resulting from processing the document data must be

a(*),b(*),a(*),b(*),...

, and the printer object must force each
copy (

a(*),b(*)

) to start on a new media sheet.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

. If a print job has multiple
documents -- say, the document data is called

a

and

b

--
then the result of processing the data in each document instance must be
treated as a single sequence of media sheets for finishing operations; that
is, the sets

a(*)

and

b(*)

would each be finished
separately. The printer must force each copy of the result of processing
the data in a single document to start on a new media sheet. If more than
one copy is made, the ordering of the sets of media sheets resulting from
processing the document data must be

a(*),a(*),...,b(*),b(*)...

.

SEPARATE_DOCUMENTS_COLLATED_COPIES

. If a print job has multiple
documents -- say, the document data is called

a

and

b

--
then the result of processing the data in each document instance must be
treated as a single sequence of media sheets for finishing operations; that
is, the sets

a(*)

and

b(*)

would each be finished
separately. The printer must force each copy of the result of processing
the data in a single document to start on a new media sheet. If more than
one copy is made, the ordering of the sets of media sheets resulting from
processing the document data must be

a(*),b(*),a(*),b(*),...

.

SINGLE_DOCUMENT_NEW_SHEET

. Same as SINGLE_DOCUMENT, except that the
printer must ensure that the first impression of each document instance in
the job is placed on a new media sheet. This value allows multiple
documents to be stapled together with a single staple where each document
starts on a new sheet.

SINGLE_DOCUMENT

is the same as

SEPARATE_DOCUMENTS_COLLATED_COPIES

with respect to ordering of
print-stream pages, but not media sheet generation, since

SINGLE_DOCUMENT

will put the first page of the next document on the
back side of a sheet if an odd number of pages have been produced so far for
the job, while

SEPARATE_DOCUMENTS_COLLATED_COPIES

always forces the
next document or document copy on to a new sheet.

In addition, if a

Finishings

attribute of

STAPLE

is specified, then:

- With

SINGLE_DOCUMENT

, documents

a

and

b

are
stapled together as a single document with no regard to new sheets.

With

SINGLE_DOCUMENT_NEW_SHEET

, documents

a

and

b

are stapled together as a single document, but document

b

starts on a new sheet.

With

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

and

SEPARATE_DOCUMENTS_COLLATED_COPIES

, documents

a

and

b

are stapled separately.

Note:

None of these values provide means to produce uncollated sheets
within a document, i.e., where multiple copies of sheet

n

are produced
before sheet

n

+1 of the same document. To specify that, see the

SheetCollate

attribute.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

SINGLE_DOCUMENT

. If a
print job has multiple documents -- say, the document data is called

a

and

b

-- then the result of processing all the document
data (

a

and then

b

) must be treated as a single sequence of
media sheets for finishing operations; that is, finishing would be
performed on the concatenation of the sequences

a(*),b(*)

. The
printer must not force the data in each document instance to be formatted
onto a new print-stream page, nor to start a new impression on a new media
sheet. If more than one copy is made, the ordering of the sets of media
sheets resulting from processing the document data must be

a(*),b(*),a(*),b(*),...

, and the printer object must force each
copy (

a(*),b(*)

) to start on a new media sheet.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

. If a print job has multiple
documents -- say, the document data is called

a

and

b

--
then the result of processing the data in each document instance must be
treated as a single sequence of media sheets for finishing operations; that
is, the sets

a(*)

and

b(*)

would each be finished
separately. The printer must force each copy of the result of processing
the data in a single document to start on a new media sheet. If more than
one copy is made, the ordering of the sets of media sheets resulting from
processing the document data must be

a(*),a(*),...,b(*),b(*)...

.

SEPARATE_DOCUMENTS_COLLATED_COPIES

. If a print job has multiple
documents -- say, the document data is called

a

and

b

--
then the result of processing the data in each document instance must be
treated as a single sequence of media sheets for finishing operations; that
is, the sets

a(*)

and

b(*)

would each be finished
separately. The printer must force each copy of the result of processing
the data in a single document to start on a new media sheet. If more than
one copy is made, the ordering of the sets of media sheets resulting from
processing the document data must be

a(*),b(*),a(*),b(*),...

.

SINGLE_DOCUMENT_NEW_SHEET

. Same as SINGLE_DOCUMENT, except that the
printer must ensure that the first impression of each document instance in
the job is placed on a new media sheet. This value allows multiple
documents to be stapled together with a single staple where each document
starts on a new sheet.

SINGLE_DOCUMENT

is the same as

SEPARATE_DOCUMENTS_COLLATED_COPIES

with respect to ordering of
print-stream pages, but not media sheet generation, since

SINGLE_DOCUMENT

will put the first page of the next document on the
back side of a sheet if an odd number of pages have been produced so far for
the job, while

SEPARATE_DOCUMENTS_COLLATED_COPIES

always forces the
next document or document copy on to a new sheet.

In addition, if a

Finishings

attribute of

STAPLE

is specified, then:

- With

SINGLE_DOCUMENT

, documents

a

and

b

are
stapled together as a single document with no regard to new sheets.

With

SINGLE_DOCUMENT_NEW_SHEET

, documents

a

and

b

are stapled together as a single document, but document

b

starts on a new sheet.

With

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

and

SEPARATE_DOCUMENTS_COLLATED_COPIES

, documents

a

and

b

are stapled separately.

Note:

None of these values provide means to produce uncollated sheets
within a document, i.e., where multiple copies of sheet

n

are produced
before sheet

n

+1 of the same document. To specify that, see the

SheetCollate

attribute.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

In addition, if a

Finishings

attribute of

STAPLE

is specified, then:

- With

SINGLE_DOCUMENT

, documents

a

and

b

are
stapled together as a single document with no regard to new sheets.

With

SINGLE_DOCUMENT_NEW_SHEET

, documents

a

and

b

are stapled together as a single document, but document

b

starts on a new sheet.

With

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

and

SEPARATE_DOCUMENTS_COLLATED_COPIES

, documents

a

and

b

are stapled separately.

Note:

None of these values provide means to produce uncollated sheets
within a document, i.e., where multiple copies of sheet

n

are produced
before sheet

n

+1 of the same document. To specify that, see the

SheetCollate

attribute.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

With

SINGLE_DOCUMENT

, documents

a

and

b

are
stapled together as a single document with no regard to new sheets.

With

SINGLE_DOCUMENT_NEW_SHEET

, documents

a

and

b

are stapled together as a single document, but document

b

starts on a new sheet.

With

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

and

SEPARATE_DOCUMENTS_COLLATED_COPIES

, documents

a

and

b

are stapled separately.

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

MultipleDocumentHandling

SEPARATE_DOCUMENTS_COLLATED_COPIES

Separate documents collated copies -- see above for

further information

.

static

MultipleDocumentHandling

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

Separate documents uncollated copies -- see above for

further information

.

static

MultipleDocumentHandling

SINGLE_DOCUMENT

Single document -- see above for

further information

.

static

MultipleDocumentHandling

SINGLE_DOCUMENT_NEW_SHEET

Single document new sheet -- see above for

further
information

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

MultipleDocumentHandling

​(int value)

Construct a new multiple document handling enumeration value with the
given integer value.

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

MultipleDocumentHandling

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

MultipleDocumentHandling

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

MultipleDocumentHandling

SEPARATE_DOCUMENTS_COLLATED_COPIES

Separate documents collated copies -- see above for

further information

.

static

MultipleDocumentHandling

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

Separate documents uncollated copies -- see above for

further information

.

static

MultipleDocumentHandling

SINGLE_DOCUMENT

Single document -- see above for

further information

.

static

MultipleDocumentHandling

SINGLE_DOCUMENT_NEW_SHEET

Single document new sheet -- see above for

further
information

.

---

#### Field Summary

Separate documents collated copies -- see above for

further information

.

Separate documents uncollated copies -- see above for

further information

.

Single document -- see above for

further information

.

Single document new sheet -- see above for

further
information

.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

MultipleDocumentHandling

​(int value)

Construct a new multiple document handling enumeration value with the
given integer value.

---

#### Constructor Summary

Construct a new multiple document handling enumeration value with the
given integer value.

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

MultipleDocumentHandling

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

MultipleDocumentHandling

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

MultipleDocumentHandling

.

Get the name of the category of which this attribute value is an
instance.

Returns the string table for class

MultipleDocumentHandling

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

- SINGLE_DOCUMENT

```java
public static final
MultipleDocumentHandling
SINGLE_DOCUMENT
```

Single document -- see above for

further information

.

- SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

```java
public static final
MultipleDocumentHandling
SEPARATE_DOCUMENTS_UNCOLLATED_COPIES
```

Separate documents uncollated copies -- see above for

further information

.

- SEPARATE_DOCUMENTS_COLLATED_COPIES

```java
public static final
MultipleDocumentHandling
SEPARATE_DOCUMENTS_COLLATED_COPIES
```

Separate documents collated copies -- see above for

further information

.

- SINGLE_DOCUMENT_NEW_SHEET

```java
public static final
MultipleDocumentHandling
SINGLE_DOCUMENT_NEW_SHEET
```

Single document new sheet -- see above for

further
information

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MultipleDocumentHandling

```java
protected MultipleDocumentHandling​(int value)
```

Construct a new multiple document handling enumeration value with the
given integer value.

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

MultipleDocumentHandling

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

MultipleDocumentHandling

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

MultipleDocumentHandling

and any vendor-defined
subclasses, the category is class

MultipleDocumentHandling

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

MultipleDocumentHandling

and any vendor-defined
subclasses, the category name is

"multiple-document-handling"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Field Detail

- SINGLE_DOCUMENT

```java
public static final
MultipleDocumentHandling
SINGLE_DOCUMENT
```

Single document -- see above for

further information

.

- SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

```java
public static final
MultipleDocumentHandling
SEPARATE_DOCUMENTS_UNCOLLATED_COPIES
```

Separate documents uncollated copies -- see above for

further information

.

- SEPARATE_DOCUMENTS_COLLATED_COPIES

```java
public static final
MultipleDocumentHandling
SEPARATE_DOCUMENTS_COLLATED_COPIES
```

Separate documents collated copies -- see above for

further information

.

- SINGLE_DOCUMENT_NEW_SHEET

```java
public static final
MultipleDocumentHandling
SINGLE_DOCUMENT_NEW_SHEET
```

Single document new sheet -- see above for

further
information

.

---

#### Field Detail

SINGLE_DOCUMENT

```java
public static final
MultipleDocumentHandling
SINGLE_DOCUMENT
```

Single document -- see above for

further information

.

---

#### SINGLE_DOCUMENT

public static final

MultipleDocumentHandling

SINGLE_DOCUMENT

Single document -- see above for

further information

.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

```java
public static final
MultipleDocumentHandling
SEPARATE_DOCUMENTS_UNCOLLATED_COPIES
```

Separate documents uncollated copies -- see above for

further information

.

---

#### SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

public static final

MultipleDocumentHandling

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

Separate documents uncollated copies -- see above for

further information

.

SEPARATE_DOCUMENTS_COLLATED_COPIES

```java
public static final
MultipleDocumentHandling
SEPARATE_DOCUMENTS_COLLATED_COPIES
```

Separate documents collated copies -- see above for

further information

.

---

#### SEPARATE_DOCUMENTS_COLLATED_COPIES

public static final

MultipleDocumentHandling

SEPARATE_DOCUMENTS_COLLATED_COPIES

Separate documents collated copies -- see above for

further information

.

SINGLE_DOCUMENT_NEW_SHEET

```java
public static final
MultipleDocumentHandling
SINGLE_DOCUMENT_NEW_SHEET
```

Single document new sheet -- see above for

further
information

.

---

#### SINGLE_DOCUMENT_NEW_SHEET

public static final

MultipleDocumentHandling

SINGLE_DOCUMENT_NEW_SHEET

Single document new sheet -- see above for

further
information

.

Constructor Detail

- MultipleDocumentHandling

```java
protected MultipleDocumentHandling​(int value)
```

Construct a new multiple document handling enumeration value with the
given integer value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

MultipleDocumentHandling

```java
protected MultipleDocumentHandling​(int value)
```

Construct a new multiple document handling enumeration value with the
given integer value.

**Parameters:** value

- Integer value

---

#### MultipleDocumentHandling

protected MultipleDocumentHandling​(int value)

Construct a new multiple document handling enumeration value with the
given integer value.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

MultipleDocumentHandling

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

MultipleDocumentHandling

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

MultipleDocumentHandling

and any vendor-defined
subclasses, the category is class

MultipleDocumentHandling

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

MultipleDocumentHandling

and any vendor-defined
subclasses, the category name is

"multiple-document-handling"

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

MultipleDocumentHandling

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

MultipleDocumentHandling

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

MultipleDocumentHandling

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

MultipleDocumentHandling

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

MultipleDocumentHandling

and any vendor-defined
subclasses, the category is class

MultipleDocumentHandling

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

MultipleDocumentHandling

and any vendor-defined
subclasses, the category is class

MultipleDocumentHandling

itself.

For class

MultipleDocumentHandling

and any vendor-defined
subclasses, the category is class

MultipleDocumentHandling

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

MultipleDocumentHandling

and any vendor-defined
subclasses, the category name is

"multiple-document-handling"

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

MultipleDocumentHandling

and any vendor-defined
subclasses, the category name is

"multiple-document-handling"

.

For class

MultipleDocumentHandling

and any vendor-defined
subclasses, the category name is

"multiple-document-handling"

.

---

