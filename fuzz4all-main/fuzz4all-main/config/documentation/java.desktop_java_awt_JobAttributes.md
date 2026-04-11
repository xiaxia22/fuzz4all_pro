# Class JobAttributes

**Source:** `java.desktop\java\awt\JobAttributes.html`

### Class Description

```java
public final class
JobAttributes

extends
Object

implements
Cloneable
```

A set of attributes which control a print job.

Instances of this class control the number of copies, default selection,
destination, print dialog, file and printer names, page ranges, multiple
document handling (including collation), and multi-page imposition (such
as duplex) of every print job which uses the instance. Attribute names are
compliant with the Internet Printing Protocol (IPP) 1.1 where possible.
Attribute values are partially compliant where possible.

To use a method which takes an inner class type, pass a reference to
one of the constant fields of the inner class. Client code cannot create
new instances of the inner class types because none of those classes
has a public constructor. For example, to set the print dialog type to
the cross-platform, pure Java print dialog, use the following code:

```java
import java.awt.JobAttributes;

public class PureJavaPrintDialogExample {
public void setPureJavaPrintDialog(JobAttributes jobAttributes) {
jobAttributes.setDialog(JobAttributes.DialogType.COMMON);
}
}
```

Every IPP attribute which supports an

attributeName

-default value
has a corresponding

set

attributeName

ToDefault

method.
Default value fields are not provided.

**All Implemented Interfaces:** Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public JobAttributes()

Constructs a

JobAttributes

instance with default
values for every attribute. The dialog defaults to

DialogType.NATIVE

. Min page defaults to

1

. Max page defaults to

Integer.MAX_VALUE

.
Destination defaults to

DestinationType.PRINTER

.
Selection defaults to

DefaultSelectionType.ALL

.
Number of copies defaults to

1

. Multiple document handling defaults
to

MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

.
Sides defaults to

SidesType.ONE_SIDED

. File name defaults
to

null

.

---

#### public JobAttributes​(
JobAttributes
obj)

Constructs a

JobAttributes

instance which is a copy
of the supplied

JobAttributes

.

**Parameters:**
- obj

- the

JobAttributes

to copy

---

#### public JobAttributes​(int copies,

JobAttributes.DefaultSelectionType
defaultSelection,

JobAttributes.DestinationType
destination,

JobAttributes.DialogType
dialog,

String
fileName,
int maxPage,
int minPage,

JobAttributes.MultipleDocumentHandlingType
multipleDocumentHandling,
int[][] pageRanges,

String
printer,

JobAttributes.SidesType
sides)

Constructs a

JobAttributes

instance with the
specified values for every attribute.

**Parameters:**
- copies

- an integer greater than 0
- defaultSelection

-

DefaultSelectionType.ALL

,

DefaultSelectionType.RANGE

, or

DefaultSelectionType.SELECTION
- destination

-

DestinationType.FILE

or

DestinationType.PRINTER
- dialog

-

DialogType.COMMON

,

DialogType.NATIVE

, or

DialogType.NONE
- fileName

- the possibly

null

file name
- maxPage

- an integer greater than zero and greater than or equal
to

minPage
- minPage

- an integer greater than zero and less than or equal
to

maxPage
- multipleDocumentHandling

-

MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_COLLATED_COPIES

or

MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES
- pageRanges

- an array of integer arrays of two elements; an array
is interpreted as a range spanning all pages including and
between the specified pages; ranges must be in ascending
order and must not overlap; specified page numbers cannot be
less than

minPage

nor greater than

maxPage

;
for example:

```java
(new int[][] { new int[] { 1, 3 }, new int[] { 5, 5 },
new int[] { 15, 19 } }),
```

specifies pages 1, 2, 3, 5, 15, 16, 17, 18, and 19. Note that
(

new int[][] { new int[] { 1, 1 }, new int[] { 1, 2 } }

),
is an invalid set of page ranges because the two ranges
overlap
- printer

- the possibly

null

printer name
- sides

-

SidesType.ONE_SIDED

,

SidesType.TWO_SIDED_LONG_EDGE

, or

SidesType.TWO_SIDED_SHORT_EDGE

**Throws:**
- IllegalArgumentException

- if one or more of the above
conditions is violated

---

### Method Details

#### public
Object
clone()

Creates and returns a copy of this

JobAttributes

.

**Overrides:**
- clone

in class

Object

**Returns:**
- the newly created copy; it is safe to cast this Object into
a

JobAttributes

**See Also:**
- Cloneable

---

#### public void set​(
JobAttributes
obj)

Sets all of the attributes of this

JobAttributes

to
the same values as the attributes of obj.

**Parameters:**
- obj

- the

JobAttributes

to copy

---

#### public int getCopies()

Returns the number of copies the application should render for jobs
using these attributes. This attribute is updated to the value chosen
by the user.

**Returns:**
- an integer greater than 0.

---

#### public void setCopies​(int copies)

Specifies the number of copies the application should render for jobs
using these attributes. Not specifying this attribute is equivalent to
specifying

1

.

**Parameters:**
- copies

- an integer greater than 0

**Throws:**
- IllegalArgumentException

- if

copies

is less than
or equal to 0

---

#### public void setCopiesToDefault()

Sets the number of copies the application should render for jobs using
these attributes to the default. The default number of copies is 1.

---

#### public
JobAttributes.DefaultSelectionType
getDefaultSelection()

Specifies whether, for jobs using these attributes, the application
should print all pages, the range specified by the return value of

getPageRanges

, or the current selection. This attribute
is updated to the value chosen by the user.

**Returns:**
- DefaultSelectionType.ALL, DefaultSelectionType.RANGE, or
DefaultSelectionType.SELECTION

---

#### public void setDefaultSelection​(
JobAttributes.DefaultSelectionType
defaultSelection)

Specifies whether, for jobs using these attributes, the application
should print all pages, the range specified by the return value of

getPageRanges

, or the current selection. Not specifying
this attribute is equivalent to specifying DefaultSelectionType.ALL.

**Parameters:**
- defaultSelection

- DefaultSelectionType.ALL,
DefaultSelectionType.RANGE, or DefaultSelectionType.SELECTION.

**Throws:**
- IllegalArgumentException

- if defaultSelection is

null

---

#### public
JobAttributes.DestinationType
getDestination()

Specifies whether output will be to a printer or a file for jobs using
these attributes. This attribute is updated to the value chosen by the
user.

**Returns:**
- DestinationType.FILE or DestinationType.PRINTER

---

#### public void setDestination​(
JobAttributes.DestinationType
destination)

Specifies whether output will be to a printer or a file for jobs using
these attributes. Not specifying this attribute is equivalent to
specifying DestinationType.PRINTER.

**Parameters:**
- destination

- DestinationType.FILE or DestinationType.PRINTER.

**Throws:**
- IllegalArgumentException

- if destination is null.

---

#### public
JobAttributes.DialogType
getDialog()

Returns whether, for jobs using these attributes, the user should see
a print dialog in which to modify the print settings, and which type of
print dialog should be displayed. DialogType.COMMON denotes a cross-
platform, pure Java print dialog. DialogType.NATIVE denotes the
platform's native print dialog. If a platform does not support a native
print dialog, the pure Java print dialog is displayed instead.
DialogType.NONE specifies no print dialog (i.e., background printing).
This attribute cannot be modified by, and is not subject to any
limitations of, the implementation or the target printer.

**Returns:**
- DialogType.COMMON

,

DialogType.NATIVE

, or

DialogType.NONE

---

#### public void setDialog​(
JobAttributes.DialogType
dialog)

Specifies whether, for jobs using these attributes, the user should see
a print dialog in which to modify the print settings, and which type of
print dialog should be displayed. DialogType.COMMON denotes a cross-
platform, pure Java print dialog. DialogType.NATIVE denotes the
platform's native print dialog. If a platform does not support a native
print dialog, the pure Java print dialog is displayed instead.
DialogType.NONE specifies no print dialog (i.e., background printing).
Not specifying this attribute is equivalent to specifying
DialogType.NATIVE.

**Parameters:**
- dialog

- DialogType.COMMON, DialogType.NATIVE, or
DialogType.NONE.

**Throws:**
- IllegalArgumentException

- if dialog is null.

---

#### public
String
getFileName()

Specifies the file name for the output file for jobs using these
attributes. This attribute is updated to the value chosen by the user.

**Returns:**
- the possibly

null

file name

---

#### public void setFileName​(
String
fileName)

Specifies the file name for the output file for jobs using these
attributes. Default is platform-dependent and implementation-defined.

**Parameters:**
- fileName

- the possibly null file name.

---

#### public int getFromPage()

Returns, for jobs using these attributes, the first page to be
printed, if a range of pages is to be printed. This attribute is
updated to the value chosen by the user. An application should ignore
this attribute on output, unless the return value of the

getDefaultSelection

method is DefaultSelectionType.RANGE. An
application should honor the return value of

getPageRanges

over the return value of this method, if possible.

**Returns:**
- an integer greater than zero and less than or equal to

toPage

and greater than or equal to

minPage

and
less than or equal to

maxPage

.

---

#### public void setFromPage​(int fromPage)

Specifies, for jobs using these attributes, the first page to be
printed, if a range of pages is to be printed. If this attribute is not
specified, then the values from the pageRanges attribute are used. If
pageRanges and either or both of fromPage and toPage are specified,
pageRanges takes precedence. Specifying none of pageRanges, fromPage,
or toPage is equivalent to calling
setPageRanges(new int[][] { new int[] {

minPage

} });

**Parameters:**
- fromPage

- an integer greater than zero and less than or equal to

toPage

and greater than or equal to

minPage

and
less than or equal to

maxPage

.

**Throws:**
- IllegalArgumentException

- if one or more of the above
conditions is violated.

---

#### public int getMaxPage()

Specifies the maximum value the user can specify as the last page to
be printed for jobs using these attributes. This attribute cannot be
modified by, and is not subject to any limitations of, the
implementation or the target printer.

**Returns:**
- an integer greater than zero and greater than or equal
to

minPage

.

---

#### public void setMaxPage​(int maxPage)

Specifies the maximum value the user can specify as the last page to
be printed for jobs using these attributes. Not specifying this
attribute is equivalent to specifying

Integer.MAX_VALUE

.

**Parameters:**
- maxPage

- an integer greater than zero and greater than or equal
to

minPage

**Throws:**
- IllegalArgumentException

- if one or more of the above
conditions is violated

---

#### public int getMinPage()

Specifies the minimum value the user can specify as the first page to
be printed for jobs using these attributes. This attribute cannot be
modified by, and is not subject to any limitations of, the
implementation or the target printer.

**Returns:**
- an integer greater than zero and less than or equal
to

maxPage

.

---

#### public void setMinPage​(int minPage)

Specifies the minimum value the user can specify as the first page to
be printed for jobs using these attributes. Not specifying this
attribute is equivalent to specifying

1

.

**Parameters:**
- minPage

- an integer greater than zero and less than or equal
to

maxPage

.

**Throws:**
- IllegalArgumentException

- if one or more of the above
conditions is violated.

---

#### public
JobAttributes.MultipleDocumentHandlingType
getMultipleDocumentHandling()

Specifies the handling of multiple copies, including collation, for
jobs using these attributes. This attribute is updated to the value
chosen by the user.

**Returns:**
- MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_COLLATED_COPIES or
MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES.

---

#### public void setMultipleDocumentHandling​(
JobAttributes.MultipleDocumentHandlingType
multipleDocumentHandling)

Specifies the handling of multiple copies, including collation, for
jobs using these attributes. Not specifying this attribute is equivalent
to specifying
MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES.

**Parameters:**
- multipleDocumentHandling

- MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_COLLATED_COPIES or
MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES.

**Throws:**
- IllegalArgumentException

- if multipleDocumentHandling is null.

---

#### public void setMultipleDocumentHandlingToDefault()

Sets the handling of multiple copies, including collation, for jobs
using these attributes to the default. The default handling is
MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES.

---

#### public int[][] getPageRanges()

Specifies, for jobs using these attributes, the ranges of pages to be
printed, if a range of pages is to be printed. All range numbers are
inclusive. This attribute is updated to the value chosen by the user.
An application should ignore this attribute on output, unless the
return value of the

getDefaultSelection

method is
DefaultSelectionType.RANGE.

**Returns:**
- an array of integer arrays of 2 elements. An array
is interpreted as a range spanning all pages including and
between the specified pages. Ranges must be in ascending
order and must not overlap. Specified page numbers cannot be
less than

minPage

nor greater than

maxPage

.
For example:
(new int[][] { new int[] { 1, 3 }, new int[] { 5, 5 },
new int[] { 15, 19 } }),
specifies pages 1, 2, 3, 5, 15, 16, 17, 18, and 19.

---

#### public void setPageRanges​(int[][] pageRanges)

Specifies, for jobs using these attributes, the ranges of pages to be
printed, if a range of pages is to be printed. All range numbers are
inclusive. If this attribute is not specified, then the values from the
fromPage and toPages attributes are used. If pageRanges and either or
both of fromPage and toPage are specified, pageRanges takes precedence.
Specifying none of pageRanges, fromPage, or toPage is equivalent to
calling setPageRanges(new int[][] { new int[] {

minPage

,

minPage

} });

**Parameters:**
- pageRanges

- an array of integer arrays of 2 elements. An array
is interpreted as a range spanning all pages including and
between the specified pages. Ranges must be in ascending
order and must not overlap. Specified page numbers cannot be
less than

minPage

nor greater than

maxPage

.
For example:
(new int[][] { new int[] { 1, 3 }, new int[] { 5, 5 },
new int[] { 15, 19 } }),
specifies pages 1, 2, 3, 5, 15, 16, 17, 18, and 19. Note that
(new int[][] { new int[] { 1, 1 }, new int[] { 1, 2 } }),
is an invalid set of page ranges because the two ranges
overlap.

**Throws:**
- IllegalArgumentException

- if one or more of the above
conditions is violated.

---

#### public
String
getPrinter()

Returns the destination printer for jobs using these attributes. This
attribute is updated to the value chosen by the user.

**Returns:**
- the possibly null printer name.

---

#### public void setPrinter​(
String
printer)

Specifies the destination printer for jobs using these attributes.
Default is platform-dependent and implementation-defined.

**Parameters:**
- printer

- the possibly null printer name.

---

#### public
JobAttributes.SidesType
getSides()

Returns how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes. SidesType.ONE_SIDED
imposes each consecutive page upon the same side of consecutive media
sheets. This imposition is sometimes called

simplex

.
SidesType.TWO_SIDED_LONG_EDGE imposes each consecutive pair of pages
upon front and back sides of consecutive media sheets, such that the
orientation of each pair of pages on the medium would be correct for
the reader as if for binding on the long edge. This imposition is
sometimes called

duplex

. SidesType.TWO_SIDED_SHORT_EDGE imposes
each consecutive pair of pages upon front and back sides of consecutive
media sheets, such that the orientation of each pair of pages on the
medium would be correct for the reader as if for binding on the short
edge. This imposition is sometimes called

tumble

. This attribute
is updated to the value chosen by the user.

**Returns:**
- SidesType.ONE_SIDED, SidesType.TWO_SIDED_LONG_EDGE, or
SidesType.TWO_SIDED_SHORT_EDGE.

---

#### public void setSides​(
JobAttributes.SidesType
sides)

Specifies how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes. SidesType.ONE_SIDED
imposes each consecutive page upon the same side of consecutive media
sheets. This imposition is sometimes called

simplex

.
SidesType.TWO_SIDED_LONG_EDGE imposes each consecutive pair of pages
upon front and back sides of consecutive media sheets, such that the
orientation of each pair of pages on the medium would be correct for
the reader as if for binding on the long edge. This imposition is
sometimes called

duplex

. SidesType.TWO_SIDED_SHORT_EDGE imposes
each consecutive pair of pages upon front and back sides of consecutive
media sheets, such that the orientation of each pair of pages on the
medium would be correct for the reader as if for binding on the short
edge. This imposition is sometimes called

tumble

. Not specifying
this attribute is equivalent to specifying SidesType.ONE_SIDED.

**Parameters:**
- sides

- SidesType.ONE_SIDED, SidesType.TWO_SIDED_LONG_EDGE, or
SidesType.TWO_SIDED_SHORT_EDGE.

**Throws:**
- IllegalArgumentException

- if sides is null.

---

#### public void setSidesToDefault()

Sets how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes to the default. The
default imposition is SidesType.ONE_SIDED.

---

#### public int getToPage()

Returns, for jobs using these attributes, the last page (inclusive)
to be printed, if a range of pages is to be printed. This attribute is
updated to the value chosen by the user. An application should ignore
this attribute on output, unless the return value of the

getDefaultSelection

method is DefaultSelectionType.RANGE. An
application should honor the return value of

getPageRanges

over the return value of this method, if possible.

**Returns:**
- an integer greater than zero and greater than or equal
to

toPage

and greater than or equal to

minPage

and less than or equal to

maxPage

.

---

#### public void setToPage​(int toPage)

Specifies, for jobs using these attributes, the last page (inclusive)
to be printed, if a range of pages is to be printed.
If this attribute is not specified, then the values from the pageRanges
attribute are used. If pageRanges and either or both of fromPage and
toPage are specified, pageRanges takes precedence. Specifying none of
pageRanges, fromPage, or toPage is equivalent to calling
setPageRanges(new int[][] { new int[] {

minPage

} });

**Parameters:**
- toPage

- an integer greater than zero and greater than or equal
to

fromPage

and greater than or equal to

minPage

and less than or equal to

maxPage

.

**Throws:**
- IllegalArgumentException

- if one or more of the above
conditions is violated.

---

#### public boolean equals​(
Object
obj)

Determines whether two JobAttributes are equal to each other.

Two JobAttributes are equal if and only if each of their attributes are
equal. Attributes of enumeration type are equal if and only if the
fields refer to the same unique enumeration object. A set of page
ranges is equal if and only if the sets are of equal length, each range
enumerates the same pages, and the ranges are in the same order.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object whose equality will be checked.

**Returns:**
- whether obj is equal to this JobAttribute according to the
above criteria.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code value for this JobAttributes.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a string representation of this JobAttributes.

**Overrides:**
- toString

in class

Object

**Returns:**
- the string representation.

---

### Additional Sections

#### Class JobAttributes

java.lang.Object

- java.awt.JobAttributes

java.awt.JobAttributes

**All Implemented Interfaces:** Cloneable

```java
public final class
JobAttributes

extends
Object

implements
Cloneable
```

A set of attributes which control a print job.

Instances of this class control the number of copies, default selection,
destination, print dialog, file and printer names, page ranges, multiple
document handling (including collation), and multi-page imposition (such
as duplex) of every print job which uses the instance. Attribute names are
compliant with the Internet Printing Protocol (IPP) 1.1 where possible.
Attribute values are partially compliant where possible.

To use a method which takes an inner class type, pass a reference to
one of the constant fields of the inner class. Client code cannot create
new instances of the inner class types because none of those classes
has a public constructor. For example, to set the print dialog type to
the cross-platform, pure Java print dialog, use the following code:

```java
import java.awt.JobAttributes;

public class PureJavaPrintDialogExample {
public void setPureJavaPrintDialog(JobAttributes jobAttributes) {
jobAttributes.setDialog(JobAttributes.DialogType.COMMON);
}
}
```

Every IPP attribute which supports an

attributeName

-default value
has a corresponding

set

attributeName

ToDefault

method.
Default value fields are not provided.

**Since:** 1.3

public final class

JobAttributes

extends

Object

implements

Cloneable

A set of attributes which control a print job.

Instances of this class control the number of copies, default selection,
destination, print dialog, file and printer names, page ranges, multiple
document handling (including collation), and multi-page imposition (such
as duplex) of every print job which uses the instance. Attribute names are
compliant with the Internet Printing Protocol (IPP) 1.1 where possible.
Attribute values are partially compliant where possible.

To use a method which takes an inner class type, pass a reference to
one of the constant fields of the inner class. Client code cannot create
new instances of the inner class types because none of those classes
has a public constructor. For example, to set the print dialog type to
the cross-platform, pure Java print dialog, use the following code:

```java
import java.awt.JobAttributes;

public class PureJavaPrintDialogExample {
public void setPureJavaPrintDialog(JobAttributes jobAttributes) {
jobAttributes.setDialog(JobAttributes.DialogType.COMMON);
}
}
```

Every IPP attribute which supports an

attributeName

-default value
has a corresponding

set

attributeName

ToDefault

method.
Default value fields are not provided.

Instances of this class control the number of copies, default selection,
destination, print dialog, file and printer names, page ranges, multiple
document handling (including collation), and multi-page imposition (such
as duplex) of every print job which uses the instance. Attribute names are
compliant with the Internet Printing Protocol (IPP) 1.1 where possible.
Attribute values are partially compliant where possible.

To use a method which takes an inner class type, pass a reference to
one of the constant fields of the inner class. Client code cannot create
new instances of the inner class types because none of those classes
has a public constructor. For example, to set the print dialog type to
the cross-platform, pure Java print dialog, use the following code:

```java
import java.awt.JobAttributes;

public class PureJavaPrintDialogExample {
public void setPureJavaPrintDialog(JobAttributes jobAttributes) {
jobAttributes.setDialog(JobAttributes.DialogType.COMMON);
}
}
```

Every IPP attribute which supports an

attributeName

-default value
has a corresponding

set

attributeName

ToDefault

method.
Default value fields are not provided.

To use a method which takes an inner class type, pass a reference to
one of the constant fields of the inner class. Client code cannot create
new instances of the inner class types because none of those classes
has a public constructor. For example, to set the print dialog type to
the cross-platform, pure Java print dialog, use the following code:

```java
import java.awt.JobAttributes;

public class PureJavaPrintDialogExample {
public void setPureJavaPrintDialog(JobAttributes jobAttributes) {
jobAttributes.setDialog(JobAttributes.DialogType.COMMON);
}
}
```

Every IPP attribute which supports an

attributeName

-default value
has a corresponding

set

attributeName

ToDefault

method.
Default value fields are not provided.

import java.awt.JobAttributes;

public class PureJavaPrintDialogExample {
public void setPureJavaPrintDialog(JobAttributes jobAttributes) {
jobAttributes.setDialog(JobAttributes.DialogType.COMMON);
}
}

Every IPP attribute which supports an

attributeName

-default value
has a corresponding

set

attributeName

ToDefault

method.
Default value fields are not provided.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

JobAttributes.DefaultSelectionType

A type-safe enumeration of possible default selection states.

static class

JobAttributes.DestinationType

A type-safe enumeration of possible job destinations.

static class

JobAttributes.DialogType

A type-safe enumeration of possible dialogs to display to the user.

static class

JobAttributes.MultipleDocumentHandlingType

A type-safe enumeration of possible multiple copy handling states.

static class

JobAttributes.SidesType

A type-safe enumeration of possible multi-page impositions.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JobAttributes

()

Constructs a

JobAttributes

instance with default
values for every attribute.

JobAttributes

​(int copies,

JobAttributes.DefaultSelectionType

defaultSelection,

JobAttributes.DestinationType

destination,

JobAttributes.DialogType

dialog,

String

fileName,
int maxPage,
int minPage,

JobAttributes.MultipleDocumentHandlingType

multipleDocumentHandling,
int[][] pageRanges,

String

printer,

JobAttributes.SidesType

sides)

Constructs a

JobAttributes

instance with the
specified values for every attribute.

JobAttributes

​(

JobAttributes

obj)

Constructs a

JobAttributes

instance which is a copy
of the supplied

JobAttributes

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates and returns a copy of this

JobAttributes

.

boolean

equals

​(

Object

obj)

Determines whether two JobAttributes are equal to each other.

int

getCopies

()

Returns the number of copies the application should render for jobs
using these attributes.

JobAttributes.DefaultSelectionType

getDefaultSelection

()

Specifies whether, for jobs using these attributes, the application
should print all pages, the range specified by the return value of

getPageRanges

, or the current selection.

JobAttributes.DestinationType

getDestination

()

Specifies whether output will be to a printer or a file for jobs using
these attributes.

JobAttributes.DialogType

getDialog

()

Returns whether, for jobs using these attributes, the user should see
a print dialog in which to modify the print settings, and which type of
print dialog should be displayed.

String

getFileName

()

Specifies the file name for the output file for jobs using these
attributes.

int

getFromPage

()

Returns, for jobs using these attributes, the first page to be
printed, if a range of pages is to be printed.

int

getMaxPage

()

Specifies the maximum value the user can specify as the last page to
be printed for jobs using these attributes.

int

getMinPage

()

Specifies the minimum value the user can specify as the first page to
be printed for jobs using these attributes.

JobAttributes.MultipleDocumentHandlingType

getMultipleDocumentHandling

()

Specifies the handling of multiple copies, including collation, for
jobs using these attributes.

int[][]

getPageRanges

()

Specifies, for jobs using these attributes, the ranges of pages to be
printed, if a range of pages is to be printed.

String

getPrinter

()

Returns the destination printer for jobs using these attributes.

JobAttributes.SidesType

getSides

()

Returns how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes.

int

getToPage

()

Returns, for jobs using these attributes, the last page (inclusive)
to be printed, if a range of pages is to be printed.

int

hashCode

()

Returns a hash code value for this JobAttributes.

void

set

​(

JobAttributes

obj)

Sets all of the attributes of this

JobAttributes

to
the same values as the attributes of obj.

void

setCopies

​(int copies)

Specifies the number of copies the application should render for jobs
using these attributes.

void

setCopiesToDefault

()

Sets the number of copies the application should render for jobs using
these attributes to the default.

void

setDefaultSelection

​(

JobAttributes.DefaultSelectionType

defaultSelection)

Specifies whether, for jobs using these attributes, the application
should print all pages, the range specified by the return value of

getPageRanges

, or the current selection.

void

setDestination

​(

JobAttributes.DestinationType

destination)

Specifies whether output will be to a printer or a file for jobs using
these attributes.

void

setDialog

​(

JobAttributes.DialogType

dialog)

Specifies whether, for jobs using these attributes, the user should see
a print dialog in which to modify the print settings, and which type of
print dialog should be displayed.

void

setFileName

​(

String

fileName)

Specifies the file name for the output file for jobs using these
attributes.

void

setFromPage

​(int fromPage)

Specifies, for jobs using these attributes, the first page to be
printed, if a range of pages is to be printed.

void

setMaxPage

​(int maxPage)

Specifies the maximum value the user can specify as the last page to
be printed for jobs using these attributes.

void

setMinPage

​(int minPage)

Specifies the minimum value the user can specify as the first page to
be printed for jobs using these attributes.

void

setMultipleDocumentHandling

​(

JobAttributes.MultipleDocumentHandlingType

multipleDocumentHandling)

Specifies the handling of multiple copies, including collation, for
jobs using these attributes.

void

setMultipleDocumentHandlingToDefault

()

Sets the handling of multiple copies, including collation, for jobs
using these attributes to the default.

void

setPageRanges

​(int[][] pageRanges)

Specifies, for jobs using these attributes, the ranges of pages to be
printed, if a range of pages is to be printed.

void

setPrinter

​(

String

printer)

Specifies the destination printer for jobs using these attributes.

void

setSides

​(

JobAttributes.SidesType

sides)

Specifies how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes.

void

setSidesToDefault

()

Sets how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes to the default.

void

setToPage

​(int toPage)

Specifies, for jobs using these attributes, the last page (inclusive)
to be printed, if a range of pages is to be printed.

String

toString

()

Returns a string representation of this JobAttributes.

- Methods declared in class java.lang.

Object

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

JobAttributes.DefaultSelectionType

A type-safe enumeration of possible default selection states.

static class

JobAttributes.DestinationType

A type-safe enumeration of possible job destinations.

static class

JobAttributes.DialogType

A type-safe enumeration of possible dialogs to display to the user.

static class

JobAttributes.MultipleDocumentHandlingType

A type-safe enumeration of possible multiple copy handling states.

static class

JobAttributes.SidesType

A type-safe enumeration of possible multi-page impositions.

---

#### Nested Class Summary

A type-safe enumeration of possible default selection states.

A type-safe enumeration of possible job destinations.

A type-safe enumeration of possible dialogs to display to the user.

A type-safe enumeration of possible multiple copy handling states.

A type-safe enumeration of possible multi-page impositions.

Constructor Summary

Constructors

Constructor

Description

JobAttributes

()

Constructs a

JobAttributes

instance with default
values for every attribute.

JobAttributes

​(int copies,

JobAttributes.DefaultSelectionType

defaultSelection,

JobAttributes.DestinationType

destination,

JobAttributes.DialogType

dialog,

String

fileName,
int maxPage,
int minPage,

JobAttributes.MultipleDocumentHandlingType

multipleDocumentHandling,
int[][] pageRanges,

String

printer,

JobAttributes.SidesType

sides)

Constructs a

JobAttributes

instance with the
specified values for every attribute.

JobAttributes

​(

JobAttributes

obj)

Constructs a

JobAttributes

instance which is a copy
of the supplied

JobAttributes

.

---

#### Constructor Summary

Constructs a

JobAttributes

instance with default
values for every attribute.

Constructs a

JobAttributes

instance with the
specified values for every attribute.

Constructs a

JobAttributes

instance which is a copy
of the supplied

JobAttributes

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates and returns a copy of this

JobAttributes

.

boolean

equals

​(

Object

obj)

Determines whether two JobAttributes are equal to each other.

int

getCopies

()

Returns the number of copies the application should render for jobs
using these attributes.

JobAttributes.DefaultSelectionType

getDefaultSelection

()

Specifies whether, for jobs using these attributes, the application
should print all pages, the range specified by the return value of

getPageRanges

, or the current selection.

JobAttributes.DestinationType

getDestination

()

Specifies whether output will be to a printer or a file for jobs using
these attributes.

JobAttributes.DialogType

getDialog

()

Returns whether, for jobs using these attributes, the user should see
a print dialog in which to modify the print settings, and which type of
print dialog should be displayed.

String

getFileName

()

Specifies the file name for the output file for jobs using these
attributes.

int

getFromPage

()

Returns, for jobs using these attributes, the first page to be
printed, if a range of pages is to be printed.

int

getMaxPage

()

Specifies the maximum value the user can specify as the last page to
be printed for jobs using these attributes.

int

getMinPage

()

Specifies the minimum value the user can specify as the first page to
be printed for jobs using these attributes.

JobAttributes.MultipleDocumentHandlingType

getMultipleDocumentHandling

()

Specifies the handling of multiple copies, including collation, for
jobs using these attributes.

int[][]

getPageRanges

()

Specifies, for jobs using these attributes, the ranges of pages to be
printed, if a range of pages is to be printed.

String

getPrinter

()

Returns the destination printer for jobs using these attributes.

JobAttributes.SidesType

getSides

()

Returns how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes.

int

getToPage

()

Returns, for jobs using these attributes, the last page (inclusive)
to be printed, if a range of pages is to be printed.

int

hashCode

()

Returns a hash code value for this JobAttributes.

void

set

​(

JobAttributes

obj)

Sets all of the attributes of this

JobAttributes

to
the same values as the attributes of obj.

void

setCopies

​(int copies)

Specifies the number of copies the application should render for jobs
using these attributes.

void

setCopiesToDefault

()

Sets the number of copies the application should render for jobs using
these attributes to the default.

void

setDefaultSelection

​(

JobAttributes.DefaultSelectionType

defaultSelection)

Specifies whether, for jobs using these attributes, the application
should print all pages, the range specified by the return value of

getPageRanges

, or the current selection.

void

setDestination

​(

JobAttributes.DestinationType

destination)

Specifies whether output will be to a printer or a file for jobs using
these attributes.

void

setDialog

​(

JobAttributes.DialogType

dialog)

Specifies whether, for jobs using these attributes, the user should see
a print dialog in which to modify the print settings, and which type of
print dialog should be displayed.

void

setFileName

​(

String

fileName)

Specifies the file name for the output file for jobs using these
attributes.

void

setFromPage

​(int fromPage)

Specifies, for jobs using these attributes, the first page to be
printed, if a range of pages is to be printed.

void

setMaxPage

​(int maxPage)

Specifies the maximum value the user can specify as the last page to
be printed for jobs using these attributes.

void

setMinPage

​(int minPage)

Specifies the minimum value the user can specify as the first page to
be printed for jobs using these attributes.

void

setMultipleDocumentHandling

​(

JobAttributes.MultipleDocumentHandlingType

multipleDocumentHandling)

Specifies the handling of multiple copies, including collation, for
jobs using these attributes.

void

setMultipleDocumentHandlingToDefault

()

Sets the handling of multiple copies, including collation, for jobs
using these attributes to the default.

void

setPageRanges

​(int[][] pageRanges)

Specifies, for jobs using these attributes, the ranges of pages to be
printed, if a range of pages is to be printed.

void

setPrinter

​(

String

printer)

Specifies the destination printer for jobs using these attributes.

void

setSides

​(

JobAttributes.SidesType

sides)

Specifies how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes.

void

setSidesToDefault

()

Sets how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes to the default.

void

setToPage

​(int toPage)

Specifies, for jobs using these attributes, the last page (inclusive)
to be printed, if a range of pages is to be printed.

String

toString

()

Returns a string representation of this JobAttributes.

- Methods declared in class java.lang.

Object

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

Creates and returns a copy of this

JobAttributes

.

Determines whether two JobAttributes are equal to each other.

Returns the number of copies the application should render for jobs
using these attributes.

Specifies whether, for jobs using these attributes, the application
should print all pages, the range specified by the return value of

getPageRanges

, or the current selection.

Specifies whether output will be to a printer or a file for jobs using
these attributes.

Returns whether, for jobs using these attributes, the user should see
a print dialog in which to modify the print settings, and which type of
print dialog should be displayed.

Specifies the file name for the output file for jobs using these
attributes.

Returns, for jobs using these attributes, the first page to be
printed, if a range of pages is to be printed.

Specifies the maximum value the user can specify as the last page to
be printed for jobs using these attributes.

Specifies the minimum value the user can specify as the first page to
be printed for jobs using these attributes.

Specifies the handling of multiple copies, including collation, for
jobs using these attributes.

Specifies, for jobs using these attributes, the ranges of pages to be
printed, if a range of pages is to be printed.

Returns the destination printer for jobs using these attributes.

Returns how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes.

Returns, for jobs using these attributes, the last page (inclusive)
to be printed, if a range of pages is to be printed.

Returns a hash code value for this JobAttributes.

Sets all of the attributes of this

JobAttributes

to
the same values as the attributes of obj.

Specifies the number of copies the application should render for jobs
using these attributes.

Sets the number of copies the application should render for jobs using
these attributes to the default.

Specifies whether, for jobs using these attributes, the user should see
a print dialog in which to modify the print settings, and which type of
print dialog should be displayed.

Specifies, for jobs using these attributes, the first page to be
printed, if a range of pages is to be printed.

Sets the handling of multiple copies, including collation, for jobs
using these attributes to the default.

Specifies the destination printer for jobs using these attributes.

Specifies how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes.

Sets how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes to the default.

Specifies, for jobs using these attributes, the last page (inclusive)
to be printed, if a range of pages is to be printed.

Returns a string representation of this JobAttributes.

Methods declared in class java.lang.

Object

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JobAttributes

```java
public JobAttributes()
```

Constructs a

JobAttributes

instance with default
values for every attribute. The dialog defaults to

DialogType.NATIVE

. Min page defaults to

1

. Max page defaults to

Integer.MAX_VALUE

.
Destination defaults to

DestinationType.PRINTER

.
Selection defaults to

DefaultSelectionType.ALL

.
Number of copies defaults to

1

. Multiple document handling defaults
to

MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

.
Sides defaults to

SidesType.ONE_SIDED

. File name defaults
to

null

.

- JobAttributes

```java
public JobAttributes​(
JobAttributes
obj)
```

Constructs a

JobAttributes

instance which is a copy
of the supplied

JobAttributes

.

**Parameters:** obj

- the

JobAttributes

to copy

- JobAttributes

```java
public JobAttributes​(int copies,

JobAttributes.DefaultSelectionType
defaultSelection,

JobAttributes.DestinationType
destination,

JobAttributes.DialogType
dialog,

String
fileName,
int maxPage,
int minPage,

JobAttributes.MultipleDocumentHandlingType
multipleDocumentHandling,
int[][] pageRanges,

String
printer,

JobAttributes.SidesType
sides)
```

Constructs a

JobAttributes

instance with the
specified values for every attribute.

**Parameters:** copies

- an integer greater than 0
**Parameters:** defaultSelection

-

DefaultSelectionType.ALL

,

DefaultSelectionType.RANGE

, or

DefaultSelectionType.SELECTION
**Parameters:** destination

-

DestinationType.FILE

or

DestinationType.PRINTER
**Parameters:** dialog

-

DialogType.COMMON

,

DialogType.NATIVE

, or

DialogType.NONE
**Parameters:** fileName

- the possibly

null

file name
**Parameters:** maxPage

- an integer greater than zero and greater than or equal
to

minPage
**Parameters:** minPage

- an integer greater than zero and less than or equal
to

maxPage
**Parameters:** multipleDocumentHandling

-

MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_COLLATED_COPIES

or

MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES
**Parameters:** pageRanges

- an array of integer arrays of two elements; an array
is interpreted as a range spanning all pages including and
between the specified pages; ranges must be in ascending
order and must not overlap; specified page numbers cannot be
less than

minPage

nor greater than

maxPage

;
for example:

```java
(new int[][] { new int[] { 1, 3 }, new int[] { 5, 5 },
new int[] { 15, 19 } }),
```

specifies pages 1, 2, 3, 5, 15, 16, 17, 18, and 19. Note that
(

new int[][] { new int[] { 1, 1 }, new int[] { 1, 2 } }

),
is an invalid set of page ranges because the two ranges
overlap
**Parameters:** printer

- the possibly

null

printer name
**Parameters:** sides

-

SidesType.ONE_SIDED

,

SidesType.TWO_SIDED_LONG_EDGE

, or

SidesType.TWO_SIDED_SHORT_EDGE
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated

============ METHOD DETAIL ==========

- Method Detail

- clone

```java
public
Object
clone()
```

Creates and returns a copy of this

JobAttributes

.

**Overrides:** clone

in class

Object
**Returns:** the newly created copy; it is safe to cast this Object into
a

JobAttributes
**See Also:** Cloneable

- set

```java
public void set​(
JobAttributes
obj)
```

Sets all of the attributes of this

JobAttributes

to
the same values as the attributes of obj.

**Parameters:** obj

- the

JobAttributes

to copy

- getCopies

```java
public int getCopies()
```

Returns the number of copies the application should render for jobs
using these attributes. This attribute is updated to the value chosen
by the user.

**Returns:** an integer greater than 0.

- setCopies

```java
public void setCopies​(int copies)
```

Specifies the number of copies the application should render for jobs
using these attributes. Not specifying this attribute is equivalent to
specifying

1

.

**Parameters:** copies

- an integer greater than 0
**Throws:** IllegalArgumentException

- if

copies

is less than
or equal to 0

- setCopiesToDefault

```java
public void setCopiesToDefault()
```

Sets the number of copies the application should render for jobs using
these attributes to the default. The default number of copies is 1.

- getDefaultSelection

```java
public
JobAttributes.DefaultSelectionType
getDefaultSelection()
```

Specifies whether, for jobs using these attributes, the application
should print all pages, the range specified by the return value of

getPageRanges

, or the current selection. This attribute
is updated to the value chosen by the user.

**Returns:** DefaultSelectionType.ALL, DefaultSelectionType.RANGE, or
DefaultSelectionType.SELECTION

- setDefaultSelection

```java
public void setDefaultSelection​(
JobAttributes.DefaultSelectionType
defaultSelection)
```

Specifies whether, for jobs using these attributes, the application
should print all pages, the range specified by the return value of

getPageRanges

, or the current selection. Not specifying
this attribute is equivalent to specifying DefaultSelectionType.ALL.

**Parameters:** defaultSelection

- DefaultSelectionType.ALL,
DefaultSelectionType.RANGE, or DefaultSelectionType.SELECTION.
**Throws:** IllegalArgumentException

- if defaultSelection is

null

- getDestination

```java
public
JobAttributes.DestinationType
getDestination()
```

Specifies whether output will be to a printer or a file for jobs using
these attributes. This attribute is updated to the value chosen by the
user.

**Returns:** DestinationType.FILE or DestinationType.PRINTER

- setDestination

```java
public void setDestination​(
JobAttributes.DestinationType
destination)
```

Specifies whether output will be to a printer or a file for jobs using
these attributes. Not specifying this attribute is equivalent to
specifying DestinationType.PRINTER.

**Parameters:** destination

- DestinationType.FILE or DestinationType.PRINTER.
**Throws:** IllegalArgumentException

- if destination is null.

- getDialog

```java
public
JobAttributes.DialogType
getDialog()
```

Returns whether, for jobs using these attributes, the user should see
a print dialog in which to modify the print settings, and which type of
print dialog should be displayed. DialogType.COMMON denotes a cross-
platform, pure Java print dialog. DialogType.NATIVE denotes the
platform's native print dialog. If a platform does not support a native
print dialog, the pure Java print dialog is displayed instead.
DialogType.NONE specifies no print dialog (i.e., background printing).
This attribute cannot be modified by, and is not subject to any
limitations of, the implementation or the target printer.

**Returns:** DialogType.COMMON

,

DialogType.NATIVE

, or

DialogType.NONE

- setDialog

```java
public void setDialog​(
JobAttributes.DialogType
dialog)
```

Specifies whether, for jobs using these attributes, the user should see
a print dialog in which to modify the print settings, and which type of
print dialog should be displayed. DialogType.COMMON denotes a cross-
platform, pure Java print dialog. DialogType.NATIVE denotes the
platform's native print dialog. If a platform does not support a native
print dialog, the pure Java print dialog is displayed instead.
DialogType.NONE specifies no print dialog (i.e., background printing).
Not specifying this attribute is equivalent to specifying
DialogType.NATIVE.

**Parameters:** dialog

- DialogType.COMMON, DialogType.NATIVE, or
DialogType.NONE.
**Throws:** IllegalArgumentException

- if dialog is null.

- getFileName

```java
public
String
getFileName()
```

Specifies the file name for the output file for jobs using these
attributes. This attribute is updated to the value chosen by the user.

**Returns:** the possibly

null

file name

- setFileName

```java
public void setFileName​(
String
fileName)
```

Specifies the file name for the output file for jobs using these
attributes. Default is platform-dependent and implementation-defined.

**Parameters:** fileName

- the possibly null file name.

- getFromPage

```java
public int getFromPage()
```

Returns, for jobs using these attributes, the first page to be
printed, if a range of pages is to be printed. This attribute is
updated to the value chosen by the user. An application should ignore
this attribute on output, unless the return value of the

getDefaultSelection

method is DefaultSelectionType.RANGE. An
application should honor the return value of

getPageRanges

over the return value of this method, if possible.

**Returns:** an integer greater than zero and less than or equal to

toPage

and greater than or equal to

minPage

and
less than or equal to

maxPage

.

- setFromPage

```java
public void setFromPage​(int fromPage)
```

Specifies, for jobs using these attributes, the first page to be
printed, if a range of pages is to be printed. If this attribute is not
specified, then the values from the pageRanges attribute are used. If
pageRanges and either or both of fromPage and toPage are specified,
pageRanges takes precedence. Specifying none of pageRanges, fromPage,
or toPage is equivalent to calling
setPageRanges(new int[][] { new int[] {

minPage

} });

**Parameters:** fromPage

- an integer greater than zero and less than or equal to

toPage

and greater than or equal to

minPage

and
less than or equal to

maxPage

.
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated.

- getMaxPage

```java
public int getMaxPage()
```

Specifies the maximum value the user can specify as the last page to
be printed for jobs using these attributes. This attribute cannot be
modified by, and is not subject to any limitations of, the
implementation or the target printer.

**Returns:** an integer greater than zero and greater than or equal
to

minPage

.

- setMaxPage

```java
public void setMaxPage​(int maxPage)
```

Specifies the maximum value the user can specify as the last page to
be printed for jobs using these attributes. Not specifying this
attribute is equivalent to specifying

Integer.MAX_VALUE

.

**Parameters:** maxPage

- an integer greater than zero and greater than or equal
to

minPage
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated

- getMinPage

```java
public int getMinPage()
```

Specifies the minimum value the user can specify as the first page to
be printed for jobs using these attributes. This attribute cannot be
modified by, and is not subject to any limitations of, the
implementation or the target printer.

**Returns:** an integer greater than zero and less than or equal
to

maxPage

.

- setMinPage

```java
public void setMinPage​(int minPage)
```

Specifies the minimum value the user can specify as the first page to
be printed for jobs using these attributes. Not specifying this
attribute is equivalent to specifying

1

.

**Parameters:** minPage

- an integer greater than zero and less than or equal
to

maxPage

.
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated.

- getMultipleDocumentHandling

```java
public
JobAttributes.MultipleDocumentHandlingType
getMultipleDocumentHandling()
```

Specifies the handling of multiple copies, including collation, for
jobs using these attributes. This attribute is updated to the value
chosen by the user.

**Returns:** MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_COLLATED_COPIES or
MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES.

- setMultipleDocumentHandling

```java
public void setMultipleDocumentHandling​(
JobAttributes.MultipleDocumentHandlingType
multipleDocumentHandling)
```

Specifies the handling of multiple copies, including collation, for
jobs using these attributes. Not specifying this attribute is equivalent
to specifying
MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES.

**Parameters:** multipleDocumentHandling

- MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_COLLATED_COPIES or
MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES.
**Throws:** IllegalArgumentException

- if multipleDocumentHandling is null.

- setMultipleDocumentHandlingToDefault

```java
public void setMultipleDocumentHandlingToDefault()
```

Sets the handling of multiple copies, including collation, for jobs
using these attributes to the default. The default handling is
MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES.

- getPageRanges

```java
public int[][] getPageRanges()
```

Specifies, for jobs using these attributes, the ranges of pages to be
printed, if a range of pages is to be printed. All range numbers are
inclusive. This attribute is updated to the value chosen by the user.
An application should ignore this attribute on output, unless the
return value of the

getDefaultSelection

method is
DefaultSelectionType.RANGE.

**Returns:** an array of integer arrays of 2 elements. An array
is interpreted as a range spanning all pages including and
between the specified pages. Ranges must be in ascending
order and must not overlap. Specified page numbers cannot be
less than

minPage

nor greater than

maxPage

.
For example:
(new int[][] { new int[] { 1, 3 }, new int[] { 5, 5 },
new int[] { 15, 19 } }),
specifies pages 1, 2, 3, 5, 15, 16, 17, 18, and 19.

- setPageRanges

```java
public void setPageRanges​(int[][] pageRanges)
```

Specifies, for jobs using these attributes, the ranges of pages to be
printed, if a range of pages is to be printed. All range numbers are
inclusive. If this attribute is not specified, then the values from the
fromPage and toPages attributes are used. If pageRanges and either or
both of fromPage and toPage are specified, pageRanges takes precedence.
Specifying none of pageRanges, fromPage, or toPage is equivalent to
calling setPageRanges(new int[][] { new int[] {

minPage

,

minPage

} });

**Parameters:** pageRanges

- an array of integer arrays of 2 elements. An array
is interpreted as a range spanning all pages including and
between the specified pages. Ranges must be in ascending
order and must not overlap. Specified page numbers cannot be
less than

minPage

nor greater than

maxPage

.
For example:
(new int[][] { new int[] { 1, 3 }, new int[] { 5, 5 },
new int[] { 15, 19 } }),
specifies pages 1, 2, 3, 5, 15, 16, 17, 18, and 19. Note that
(new int[][] { new int[] { 1, 1 }, new int[] { 1, 2 } }),
is an invalid set of page ranges because the two ranges
overlap.
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated.

- getPrinter

```java
public
String
getPrinter()
```

Returns the destination printer for jobs using these attributes. This
attribute is updated to the value chosen by the user.

**Returns:** the possibly null printer name.

- setPrinter

```java
public void setPrinter​(
String
printer)
```

Specifies the destination printer for jobs using these attributes.
Default is platform-dependent and implementation-defined.

**Parameters:** printer

- the possibly null printer name.

- getSides

```java
public
JobAttributes.SidesType
getSides()
```

Returns how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes. SidesType.ONE_SIDED
imposes each consecutive page upon the same side of consecutive media
sheets. This imposition is sometimes called

simplex

.
SidesType.TWO_SIDED_LONG_EDGE imposes each consecutive pair of pages
upon front and back sides of consecutive media sheets, such that the
orientation of each pair of pages on the medium would be correct for
the reader as if for binding on the long edge. This imposition is
sometimes called

duplex

. SidesType.TWO_SIDED_SHORT_EDGE imposes
each consecutive pair of pages upon front and back sides of consecutive
media sheets, such that the orientation of each pair of pages on the
medium would be correct for the reader as if for binding on the short
edge. This imposition is sometimes called

tumble

. This attribute
is updated to the value chosen by the user.

**Returns:** SidesType.ONE_SIDED, SidesType.TWO_SIDED_LONG_EDGE, or
SidesType.TWO_SIDED_SHORT_EDGE.

- setSides

```java
public void setSides​(
JobAttributes.SidesType
sides)
```

Specifies how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes. SidesType.ONE_SIDED
imposes each consecutive page upon the same side of consecutive media
sheets. This imposition is sometimes called

simplex

.
SidesType.TWO_SIDED_LONG_EDGE imposes each consecutive pair of pages
upon front and back sides of consecutive media sheets, such that the
orientation of each pair of pages on the medium would be correct for
the reader as if for binding on the long edge. This imposition is
sometimes called

duplex

. SidesType.TWO_SIDED_SHORT_EDGE imposes
each consecutive pair of pages upon front and back sides of consecutive
media sheets, such that the orientation of each pair of pages on the
medium would be correct for the reader as if for binding on the short
edge. This imposition is sometimes called

tumble

. Not specifying
this attribute is equivalent to specifying SidesType.ONE_SIDED.

**Parameters:** sides

- SidesType.ONE_SIDED, SidesType.TWO_SIDED_LONG_EDGE, or
SidesType.TWO_SIDED_SHORT_EDGE.
**Throws:** IllegalArgumentException

- if sides is null.

- setSidesToDefault

```java
public void setSidesToDefault()
```

Sets how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes to the default. The
default imposition is SidesType.ONE_SIDED.

- getToPage

```java
public int getToPage()
```

Returns, for jobs using these attributes, the last page (inclusive)
to be printed, if a range of pages is to be printed. This attribute is
updated to the value chosen by the user. An application should ignore
this attribute on output, unless the return value of the

getDefaultSelection

method is DefaultSelectionType.RANGE. An
application should honor the return value of

getPageRanges

over the return value of this method, if possible.

**Returns:** an integer greater than zero and greater than or equal
to

toPage

and greater than or equal to

minPage

and less than or equal to

maxPage

.

- setToPage

```java
public void setToPage​(int toPage)
```

Specifies, for jobs using these attributes, the last page (inclusive)
to be printed, if a range of pages is to be printed.
If this attribute is not specified, then the values from the pageRanges
attribute are used. If pageRanges and either or both of fromPage and
toPage are specified, pageRanges takes precedence. Specifying none of
pageRanges, fromPage, or toPage is equivalent to calling
setPageRanges(new int[][] { new int[] {

minPage

} });

**Parameters:** toPage

- an integer greater than zero and greater than or equal
to

fromPage

and greater than or equal to

minPage

and less than or equal to

maxPage

.
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated.

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether two JobAttributes are equal to each other.

Two JobAttributes are equal if and only if each of their attributes are
equal. Attributes of enumeration type are equal if and only if the
fields refer to the same unique enumeration object. A set of page
ranges is equal if and only if the sets are of equal length, each range
enumerates the same pages, and the ranges are in the same order.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object whose equality will be checked.
**Returns:** whether obj is equal to this JobAttribute according to the
above criteria.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this JobAttributes.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of this JobAttributes.

**Overrides:** toString

in class

Object
**Returns:** the string representation.

Constructor Detail

- JobAttributes

```java
public JobAttributes()
```

Constructs a

JobAttributes

instance with default
values for every attribute. The dialog defaults to

DialogType.NATIVE

. Min page defaults to

1

. Max page defaults to

Integer.MAX_VALUE

.
Destination defaults to

DestinationType.PRINTER

.
Selection defaults to

DefaultSelectionType.ALL

.
Number of copies defaults to

1

. Multiple document handling defaults
to

MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

.
Sides defaults to

SidesType.ONE_SIDED

. File name defaults
to

null

.

- JobAttributes

```java
public JobAttributes​(
JobAttributes
obj)
```

Constructs a

JobAttributes

instance which is a copy
of the supplied

JobAttributes

.

**Parameters:** obj

- the

JobAttributes

to copy

- JobAttributes

```java
public JobAttributes​(int copies,

JobAttributes.DefaultSelectionType
defaultSelection,

JobAttributes.DestinationType
destination,

JobAttributes.DialogType
dialog,

String
fileName,
int maxPage,
int minPage,

JobAttributes.MultipleDocumentHandlingType
multipleDocumentHandling,
int[][] pageRanges,

String
printer,

JobAttributes.SidesType
sides)
```

Constructs a

JobAttributes

instance with the
specified values for every attribute.

**Parameters:** copies

- an integer greater than 0
**Parameters:** defaultSelection

-

DefaultSelectionType.ALL

,

DefaultSelectionType.RANGE

, or

DefaultSelectionType.SELECTION
**Parameters:** destination

-

DestinationType.FILE

or

DestinationType.PRINTER
**Parameters:** dialog

-

DialogType.COMMON

,

DialogType.NATIVE

, or

DialogType.NONE
**Parameters:** fileName

- the possibly

null

file name
**Parameters:** maxPage

- an integer greater than zero and greater than or equal
to

minPage
**Parameters:** minPage

- an integer greater than zero and less than or equal
to

maxPage
**Parameters:** multipleDocumentHandling

-

MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_COLLATED_COPIES

or

MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES
**Parameters:** pageRanges

- an array of integer arrays of two elements; an array
is interpreted as a range spanning all pages including and
between the specified pages; ranges must be in ascending
order and must not overlap; specified page numbers cannot be
less than

minPage

nor greater than

maxPage

;
for example:

```java
(new int[][] { new int[] { 1, 3 }, new int[] { 5, 5 },
new int[] { 15, 19 } }),
```

specifies pages 1, 2, 3, 5, 15, 16, 17, 18, and 19. Note that
(

new int[][] { new int[] { 1, 1 }, new int[] { 1, 2 } }

),
is an invalid set of page ranges because the two ranges
overlap
**Parameters:** printer

- the possibly

null

printer name
**Parameters:** sides

-

SidesType.ONE_SIDED

,

SidesType.TWO_SIDED_LONG_EDGE

, or

SidesType.TWO_SIDED_SHORT_EDGE
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated

---

#### Constructor Detail

JobAttributes

```java
public JobAttributes()
```

Constructs a

JobAttributes

instance with default
values for every attribute. The dialog defaults to

DialogType.NATIVE

. Min page defaults to

1

. Max page defaults to

Integer.MAX_VALUE

.
Destination defaults to

DestinationType.PRINTER

.
Selection defaults to

DefaultSelectionType.ALL

.
Number of copies defaults to

1

. Multiple document handling defaults
to

MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

.
Sides defaults to

SidesType.ONE_SIDED

. File name defaults
to

null

.

---

#### JobAttributes

public JobAttributes()

Constructs a

JobAttributes

instance with default
values for every attribute. The dialog defaults to

DialogType.NATIVE

. Min page defaults to

1

. Max page defaults to

Integer.MAX_VALUE

.
Destination defaults to

DestinationType.PRINTER

.
Selection defaults to

DefaultSelectionType.ALL

.
Number of copies defaults to

1

. Multiple document handling defaults
to

MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

.
Sides defaults to

SidesType.ONE_SIDED

. File name defaults
to

null

.

JobAttributes

```java
public JobAttributes​(
JobAttributes
obj)
```

Constructs a

JobAttributes

instance which is a copy
of the supplied

JobAttributes

.

**Parameters:** obj

- the

JobAttributes

to copy

---

#### JobAttributes

public JobAttributes​(

JobAttributes

obj)

Constructs a

JobAttributes

instance which is a copy
of the supplied

JobAttributes

.

JobAttributes

```java
public JobAttributes​(int copies,

JobAttributes.DefaultSelectionType
defaultSelection,

JobAttributes.DestinationType
destination,

JobAttributes.DialogType
dialog,

String
fileName,
int maxPage,
int minPage,

JobAttributes.MultipleDocumentHandlingType
multipleDocumentHandling,
int[][] pageRanges,

String
printer,

JobAttributes.SidesType
sides)
```

Constructs a

JobAttributes

instance with the
specified values for every attribute.

**Parameters:** copies

- an integer greater than 0
**Parameters:** defaultSelection

-

DefaultSelectionType.ALL

,

DefaultSelectionType.RANGE

, or

DefaultSelectionType.SELECTION
**Parameters:** destination

-

DestinationType.FILE

or

DestinationType.PRINTER
**Parameters:** dialog

-

DialogType.COMMON

,

DialogType.NATIVE

, or

DialogType.NONE
**Parameters:** fileName

- the possibly

null

file name
**Parameters:** maxPage

- an integer greater than zero and greater than or equal
to

minPage
**Parameters:** minPage

- an integer greater than zero and less than or equal
to

maxPage
**Parameters:** multipleDocumentHandling

-

MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_COLLATED_COPIES

or

MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES
**Parameters:** pageRanges

- an array of integer arrays of two elements; an array
is interpreted as a range spanning all pages including and
between the specified pages; ranges must be in ascending
order and must not overlap; specified page numbers cannot be
less than

minPage

nor greater than

maxPage

;
for example:

```java
(new int[][] { new int[] { 1, 3 }, new int[] { 5, 5 },
new int[] { 15, 19 } }),
```

specifies pages 1, 2, 3, 5, 15, 16, 17, 18, and 19. Note that
(

new int[][] { new int[] { 1, 1 }, new int[] { 1, 2 } }

),
is an invalid set of page ranges because the two ranges
overlap
**Parameters:** printer

- the possibly

null

printer name
**Parameters:** sides

-

SidesType.ONE_SIDED

,

SidesType.TWO_SIDED_LONG_EDGE

, or

SidesType.TWO_SIDED_SHORT_EDGE
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated

---

#### JobAttributes

public JobAttributes​(int copies,

JobAttributes.DefaultSelectionType

defaultSelection,

JobAttributes.DestinationType

destination,

JobAttributes.DialogType

dialog,

String

fileName,
int maxPage,
int minPage,

JobAttributes.MultipleDocumentHandlingType

multipleDocumentHandling,
int[][] pageRanges,

String

printer,

JobAttributes.SidesType

sides)

Constructs a

JobAttributes

instance with the
specified values for every attribute.

(new int[][] { new int[] { 1, 3 }, new int[] { 5, 5 },
new int[] { 15, 19 } }),

Method Detail

- clone

```java
public
Object
clone()
```

Creates and returns a copy of this

JobAttributes

.

**Overrides:** clone

in class

Object
**Returns:** the newly created copy; it is safe to cast this Object into
a

JobAttributes
**See Also:** Cloneable

- set

```java
public void set​(
JobAttributes
obj)
```

Sets all of the attributes of this

JobAttributes

to
the same values as the attributes of obj.

**Parameters:** obj

- the

JobAttributes

to copy

- getCopies

```java
public int getCopies()
```

Returns the number of copies the application should render for jobs
using these attributes. This attribute is updated to the value chosen
by the user.

**Returns:** an integer greater than 0.

- setCopies

```java
public void setCopies​(int copies)
```

Specifies the number of copies the application should render for jobs
using these attributes. Not specifying this attribute is equivalent to
specifying

1

.

**Parameters:** copies

- an integer greater than 0
**Throws:** IllegalArgumentException

- if

copies

is less than
or equal to 0

- setCopiesToDefault

```java
public void setCopiesToDefault()
```

Sets the number of copies the application should render for jobs using
these attributes to the default. The default number of copies is 1.

- getDefaultSelection

```java
public
JobAttributes.DefaultSelectionType
getDefaultSelection()
```

Specifies whether, for jobs using these attributes, the application
should print all pages, the range specified by the return value of

getPageRanges

, or the current selection. This attribute
is updated to the value chosen by the user.

**Returns:** DefaultSelectionType.ALL, DefaultSelectionType.RANGE, or
DefaultSelectionType.SELECTION

- setDefaultSelection

```java
public void setDefaultSelection​(
JobAttributes.DefaultSelectionType
defaultSelection)
```

Specifies whether, for jobs using these attributes, the application
should print all pages, the range specified by the return value of

getPageRanges

, or the current selection. Not specifying
this attribute is equivalent to specifying DefaultSelectionType.ALL.

**Parameters:** defaultSelection

- DefaultSelectionType.ALL,
DefaultSelectionType.RANGE, or DefaultSelectionType.SELECTION.
**Throws:** IllegalArgumentException

- if defaultSelection is

null

- getDestination

```java
public
JobAttributes.DestinationType
getDestination()
```

Specifies whether output will be to a printer or a file for jobs using
these attributes. This attribute is updated to the value chosen by the
user.

**Returns:** DestinationType.FILE or DestinationType.PRINTER

- setDestination

```java
public void setDestination​(
JobAttributes.DestinationType
destination)
```

Specifies whether output will be to a printer or a file for jobs using
these attributes. Not specifying this attribute is equivalent to
specifying DestinationType.PRINTER.

**Parameters:** destination

- DestinationType.FILE or DestinationType.PRINTER.
**Throws:** IllegalArgumentException

- if destination is null.

- getDialog

```java
public
JobAttributes.DialogType
getDialog()
```

Returns whether, for jobs using these attributes, the user should see
a print dialog in which to modify the print settings, and which type of
print dialog should be displayed. DialogType.COMMON denotes a cross-
platform, pure Java print dialog. DialogType.NATIVE denotes the
platform's native print dialog. If a platform does not support a native
print dialog, the pure Java print dialog is displayed instead.
DialogType.NONE specifies no print dialog (i.e., background printing).
This attribute cannot be modified by, and is not subject to any
limitations of, the implementation or the target printer.

**Returns:** DialogType.COMMON

,

DialogType.NATIVE

, or

DialogType.NONE

- setDialog

```java
public void setDialog​(
JobAttributes.DialogType
dialog)
```

Specifies whether, for jobs using these attributes, the user should see
a print dialog in which to modify the print settings, and which type of
print dialog should be displayed. DialogType.COMMON denotes a cross-
platform, pure Java print dialog. DialogType.NATIVE denotes the
platform's native print dialog. If a platform does not support a native
print dialog, the pure Java print dialog is displayed instead.
DialogType.NONE specifies no print dialog (i.e., background printing).
Not specifying this attribute is equivalent to specifying
DialogType.NATIVE.

**Parameters:** dialog

- DialogType.COMMON, DialogType.NATIVE, or
DialogType.NONE.
**Throws:** IllegalArgumentException

- if dialog is null.

- getFileName

```java
public
String
getFileName()
```

Specifies the file name for the output file for jobs using these
attributes. This attribute is updated to the value chosen by the user.

**Returns:** the possibly

null

file name

- setFileName

```java
public void setFileName​(
String
fileName)
```

Specifies the file name for the output file for jobs using these
attributes. Default is platform-dependent and implementation-defined.

**Parameters:** fileName

- the possibly null file name.

- getFromPage

```java
public int getFromPage()
```

Returns, for jobs using these attributes, the first page to be
printed, if a range of pages is to be printed. This attribute is
updated to the value chosen by the user. An application should ignore
this attribute on output, unless the return value of the

getDefaultSelection

method is DefaultSelectionType.RANGE. An
application should honor the return value of

getPageRanges

over the return value of this method, if possible.

**Returns:** an integer greater than zero and less than or equal to

toPage

and greater than or equal to

minPage

and
less than or equal to

maxPage

.

- setFromPage

```java
public void setFromPage​(int fromPage)
```

Specifies, for jobs using these attributes, the first page to be
printed, if a range of pages is to be printed. If this attribute is not
specified, then the values from the pageRanges attribute are used. If
pageRanges and either or both of fromPage and toPage are specified,
pageRanges takes precedence. Specifying none of pageRanges, fromPage,
or toPage is equivalent to calling
setPageRanges(new int[][] { new int[] {

minPage

} });

**Parameters:** fromPage

- an integer greater than zero and less than or equal to

toPage

and greater than or equal to

minPage

and
less than or equal to

maxPage

.
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated.

- getMaxPage

```java
public int getMaxPage()
```

Specifies the maximum value the user can specify as the last page to
be printed for jobs using these attributes. This attribute cannot be
modified by, and is not subject to any limitations of, the
implementation or the target printer.

**Returns:** an integer greater than zero and greater than or equal
to

minPage

.

- setMaxPage

```java
public void setMaxPage​(int maxPage)
```

Specifies the maximum value the user can specify as the last page to
be printed for jobs using these attributes. Not specifying this
attribute is equivalent to specifying

Integer.MAX_VALUE

.

**Parameters:** maxPage

- an integer greater than zero and greater than or equal
to

minPage
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated

- getMinPage

```java
public int getMinPage()
```

Specifies the minimum value the user can specify as the first page to
be printed for jobs using these attributes. This attribute cannot be
modified by, and is not subject to any limitations of, the
implementation or the target printer.

**Returns:** an integer greater than zero and less than or equal
to

maxPage

.

- setMinPage

```java
public void setMinPage​(int minPage)
```

Specifies the minimum value the user can specify as the first page to
be printed for jobs using these attributes. Not specifying this
attribute is equivalent to specifying

1

.

**Parameters:** minPage

- an integer greater than zero and less than or equal
to

maxPage

.
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated.

- getMultipleDocumentHandling

```java
public
JobAttributes.MultipleDocumentHandlingType
getMultipleDocumentHandling()
```

Specifies the handling of multiple copies, including collation, for
jobs using these attributes. This attribute is updated to the value
chosen by the user.

**Returns:** MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_COLLATED_COPIES or
MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES.

- setMultipleDocumentHandling

```java
public void setMultipleDocumentHandling​(
JobAttributes.MultipleDocumentHandlingType
multipleDocumentHandling)
```

Specifies the handling of multiple copies, including collation, for
jobs using these attributes. Not specifying this attribute is equivalent
to specifying
MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES.

**Parameters:** multipleDocumentHandling

- MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_COLLATED_COPIES or
MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES.
**Throws:** IllegalArgumentException

- if multipleDocumentHandling is null.

- setMultipleDocumentHandlingToDefault

```java
public void setMultipleDocumentHandlingToDefault()
```

Sets the handling of multiple copies, including collation, for jobs
using these attributes to the default. The default handling is
MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES.

- getPageRanges

```java
public int[][] getPageRanges()
```

Specifies, for jobs using these attributes, the ranges of pages to be
printed, if a range of pages is to be printed. All range numbers are
inclusive. This attribute is updated to the value chosen by the user.
An application should ignore this attribute on output, unless the
return value of the

getDefaultSelection

method is
DefaultSelectionType.RANGE.

**Returns:** an array of integer arrays of 2 elements. An array
is interpreted as a range spanning all pages including and
between the specified pages. Ranges must be in ascending
order and must not overlap. Specified page numbers cannot be
less than

minPage

nor greater than

maxPage

.
For example:
(new int[][] { new int[] { 1, 3 }, new int[] { 5, 5 },
new int[] { 15, 19 } }),
specifies pages 1, 2, 3, 5, 15, 16, 17, 18, and 19.

- setPageRanges

```java
public void setPageRanges​(int[][] pageRanges)
```

Specifies, for jobs using these attributes, the ranges of pages to be
printed, if a range of pages is to be printed. All range numbers are
inclusive. If this attribute is not specified, then the values from the
fromPage and toPages attributes are used. If pageRanges and either or
both of fromPage and toPage are specified, pageRanges takes precedence.
Specifying none of pageRanges, fromPage, or toPage is equivalent to
calling setPageRanges(new int[][] { new int[] {

minPage

,

minPage

} });

**Parameters:** pageRanges

- an array of integer arrays of 2 elements. An array
is interpreted as a range spanning all pages including and
between the specified pages. Ranges must be in ascending
order and must not overlap. Specified page numbers cannot be
less than

minPage

nor greater than

maxPage

.
For example:
(new int[][] { new int[] { 1, 3 }, new int[] { 5, 5 },
new int[] { 15, 19 } }),
specifies pages 1, 2, 3, 5, 15, 16, 17, 18, and 19. Note that
(new int[][] { new int[] { 1, 1 }, new int[] { 1, 2 } }),
is an invalid set of page ranges because the two ranges
overlap.
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated.

- getPrinter

```java
public
String
getPrinter()
```

Returns the destination printer for jobs using these attributes. This
attribute is updated to the value chosen by the user.

**Returns:** the possibly null printer name.

- setPrinter

```java
public void setPrinter​(
String
printer)
```

Specifies the destination printer for jobs using these attributes.
Default is platform-dependent and implementation-defined.

**Parameters:** printer

- the possibly null printer name.

- getSides

```java
public
JobAttributes.SidesType
getSides()
```

Returns how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes. SidesType.ONE_SIDED
imposes each consecutive page upon the same side of consecutive media
sheets. This imposition is sometimes called

simplex

.
SidesType.TWO_SIDED_LONG_EDGE imposes each consecutive pair of pages
upon front and back sides of consecutive media sheets, such that the
orientation of each pair of pages on the medium would be correct for
the reader as if for binding on the long edge. This imposition is
sometimes called

duplex

. SidesType.TWO_SIDED_SHORT_EDGE imposes
each consecutive pair of pages upon front and back sides of consecutive
media sheets, such that the orientation of each pair of pages on the
medium would be correct for the reader as if for binding on the short
edge. This imposition is sometimes called

tumble

. This attribute
is updated to the value chosen by the user.

**Returns:** SidesType.ONE_SIDED, SidesType.TWO_SIDED_LONG_EDGE, or
SidesType.TWO_SIDED_SHORT_EDGE.

- setSides

```java
public void setSides​(
JobAttributes.SidesType
sides)
```

Specifies how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes. SidesType.ONE_SIDED
imposes each consecutive page upon the same side of consecutive media
sheets. This imposition is sometimes called

simplex

.
SidesType.TWO_SIDED_LONG_EDGE imposes each consecutive pair of pages
upon front and back sides of consecutive media sheets, such that the
orientation of each pair of pages on the medium would be correct for
the reader as if for binding on the long edge. This imposition is
sometimes called

duplex

. SidesType.TWO_SIDED_SHORT_EDGE imposes
each consecutive pair of pages upon front and back sides of consecutive
media sheets, such that the orientation of each pair of pages on the
medium would be correct for the reader as if for binding on the short
edge. This imposition is sometimes called

tumble

. Not specifying
this attribute is equivalent to specifying SidesType.ONE_SIDED.

**Parameters:** sides

- SidesType.ONE_SIDED, SidesType.TWO_SIDED_LONG_EDGE, or
SidesType.TWO_SIDED_SHORT_EDGE.
**Throws:** IllegalArgumentException

- if sides is null.

- setSidesToDefault

```java
public void setSidesToDefault()
```

Sets how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes to the default. The
default imposition is SidesType.ONE_SIDED.

- getToPage

```java
public int getToPage()
```

Returns, for jobs using these attributes, the last page (inclusive)
to be printed, if a range of pages is to be printed. This attribute is
updated to the value chosen by the user. An application should ignore
this attribute on output, unless the return value of the

getDefaultSelection

method is DefaultSelectionType.RANGE. An
application should honor the return value of

getPageRanges

over the return value of this method, if possible.

**Returns:** an integer greater than zero and greater than or equal
to

toPage

and greater than or equal to

minPage

and less than or equal to

maxPage

.

- setToPage

```java
public void setToPage​(int toPage)
```

Specifies, for jobs using these attributes, the last page (inclusive)
to be printed, if a range of pages is to be printed.
If this attribute is not specified, then the values from the pageRanges
attribute are used. If pageRanges and either or both of fromPage and
toPage are specified, pageRanges takes precedence. Specifying none of
pageRanges, fromPage, or toPage is equivalent to calling
setPageRanges(new int[][] { new int[] {

minPage

} });

**Parameters:** toPage

- an integer greater than zero and greater than or equal
to

fromPage

and greater than or equal to

minPage

and less than or equal to

maxPage

.
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated.

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether two JobAttributes are equal to each other.

Two JobAttributes are equal if and only if each of their attributes are
equal. Attributes of enumeration type are equal if and only if the
fields refer to the same unique enumeration object. A set of page
ranges is equal if and only if the sets are of equal length, each range
enumerates the same pages, and the ranges are in the same order.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object whose equality will be checked.
**Returns:** whether obj is equal to this JobAttribute according to the
above criteria.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this JobAttributes.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of this JobAttributes.

**Overrides:** toString

in class

Object
**Returns:** the string representation.

---

#### Method Detail

clone

```java
public
Object
clone()
```

Creates and returns a copy of this

JobAttributes

.

**Overrides:** clone

in class

Object
**Returns:** the newly created copy; it is safe to cast this Object into
a

JobAttributes
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Creates and returns a copy of this

JobAttributes

.

set

```java
public void set​(
JobAttributes
obj)
```

Sets all of the attributes of this

JobAttributes

to
the same values as the attributes of obj.

**Parameters:** obj

- the

JobAttributes

to copy

---

#### set

public void set​(

JobAttributes

obj)

Sets all of the attributes of this

JobAttributes

to
the same values as the attributes of obj.

getCopies

```java
public int getCopies()
```

Returns the number of copies the application should render for jobs
using these attributes. This attribute is updated to the value chosen
by the user.

**Returns:** an integer greater than 0.

---

#### getCopies

public int getCopies()

Returns the number of copies the application should render for jobs
using these attributes. This attribute is updated to the value chosen
by the user.

setCopies

```java
public void setCopies​(int copies)
```

Specifies the number of copies the application should render for jobs
using these attributes. Not specifying this attribute is equivalent to
specifying

1

.

**Parameters:** copies

- an integer greater than 0
**Throws:** IllegalArgumentException

- if

copies

is less than
or equal to 0

---

#### setCopies

public void setCopies​(int copies)

Specifies the number of copies the application should render for jobs
using these attributes. Not specifying this attribute is equivalent to
specifying

1

.

setCopiesToDefault

```java
public void setCopiesToDefault()
```

Sets the number of copies the application should render for jobs using
these attributes to the default. The default number of copies is 1.

---

#### setCopiesToDefault

public void setCopiesToDefault()

Sets the number of copies the application should render for jobs using
these attributes to the default. The default number of copies is 1.

getDefaultSelection

```java
public
JobAttributes.DefaultSelectionType
getDefaultSelection()
```

Specifies whether, for jobs using these attributes, the application
should print all pages, the range specified by the return value of

getPageRanges

, or the current selection. This attribute
is updated to the value chosen by the user.

**Returns:** DefaultSelectionType.ALL, DefaultSelectionType.RANGE, or
DefaultSelectionType.SELECTION

---

#### getDefaultSelection

public

JobAttributes.DefaultSelectionType

getDefaultSelection()

Specifies whether, for jobs using these attributes, the application
should print all pages, the range specified by the return value of

getPageRanges

, or the current selection. This attribute
is updated to the value chosen by the user.

setDefaultSelection

```java
public void setDefaultSelection​(
JobAttributes.DefaultSelectionType
defaultSelection)
```

Specifies whether, for jobs using these attributes, the application
should print all pages, the range specified by the return value of

getPageRanges

, or the current selection. Not specifying
this attribute is equivalent to specifying DefaultSelectionType.ALL.

**Parameters:** defaultSelection

- DefaultSelectionType.ALL,
DefaultSelectionType.RANGE, or DefaultSelectionType.SELECTION.
**Throws:** IllegalArgumentException

- if defaultSelection is

null

---

#### setDefaultSelection

public void setDefaultSelection​(

JobAttributes.DefaultSelectionType

defaultSelection)

Specifies whether, for jobs using these attributes, the application
should print all pages, the range specified by the return value of

getPageRanges

, or the current selection. Not specifying
this attribute is equivalent to specifying DefaultSelectionType.ALL.

getDestination

```java
public
JobAttributes.DestinationType
getDestination()
```

Specifies whether output will be to a printer or a file for jobs using
these attributes. This attribute is updated to the value chosen by the
user.

**Returns:** DestinationType.FILE or DestinationType.PRINTER

---

#### getDestination

public

JobAttributes.DestinationType

getDestination()

Specifies whether output will be to a printer or a file for jobs using
these attributes. This attribute is updated to the value chosen by the
user.

setDestination

```java
public void setDestination​(
JobAttributes.DestinationType
destination)
```

Specifies whether output will be to a printer or a file for jobs using
these attributes. Not specifying this attribute is equivalent to
specifying DestinationType.PRINTER.

**Parameters:** destination

- DestinationType.FILE or DestinationType.PRINTER.
**Throws:** IllegalArgumentException

- if destination is null.

---

#### setDestination

public void setDestination​(

JobAttributes.DestinationType

destination)

Specifies whether output will be to a printer or a file for jobs using
these attributes. Not specifying this attribute is equivalent to
specifying DestinationType.PRINTER.

getDialog

```java
public
JobAttributes.DialogType
getDialog()
```

Returns whether, for jobs using these attributes, the user should see
a print dialog in which to modify the print settings, and which type of
print dialog should be displayed. DialogType.COMMON denotes a cross-
platform, pure Java print dialog. DialogType.NATIVE denotes the
platform's native print dialog. If a platform does not support a native
print dialog, the pure Java print dialog is displayed instead.
DialogType.NONE specifies no print dialog (i.e., background printing).
This attribute cannot be modified by, and is not subject to any
limitations of, the implementation or the target printer.

**Returns:** DialogType.COMMON

,

DialogType.NATIVE

, or

DialogType.NONE

---

#### getDialog

public

JobAttributes.DialogType

getDialog()

Returns whether, for jobs using these attributes, the user should see
a print dialog in which to modify the print settings, and which type of
print dialog should be displayed. DialogType.COMMON denotes a cross-
platform, pure Java print dialog. DialogType.NATIVE denotes the
platform's native print dialog. If a platform does not support a native
print dialog, the pure Java print dialog is displayed instead.
DialogType.NONE specifies no print dialog (i.e., background printing).
This attribute cannot be modified by, and is not subject to any
limitations of, the implementation or the target printer.

setDialog

```java
public void setDialog​(
JobAttributes.DialogType
dialog)
```

Specifies whether, for jobs using these attributes, the user should see
a print dialog in which to modify the print settings, and which type of
print dialog should be displayed. DialogType.COMMON denotes a cross-
platform, pure Java print dialog. DialogType.NATIVE denotes the
platform's native print dialog. If a platform does not support a native
print dialog, the pure Java print dialog is displayed instead.
DialogType.NONE specifies no print dialog (i.e., background printing).
Not specifying this attribute is equivalent to specifying
DialogType.NATIVE.

**Parameters:** dialog

- DialogType.COMMON, DialogType.NATIVE, or
DialogType.NONE.
**Throws:** IllegalArgumentException

- if dialog is null.

---

#### setDialog

public void setDialog​(

JobAttributes.DialogType

dialog)

Specifies whether, for jobs using these attributes, the user should see
a print dialog in which to modify the print settings, and which type of
print dialog should be displayed. DialogType.COMMON denotes a cross-
platform, pure Java print dialog. DialogType.NATIVE denotes the
platform's native print dialog. If a platform does not support a native
print dialog, the pure Java print dialog is displayed instead.
DialogType.NONE specifies no print dialog (i.e., background printing).
Not specifying this attribute is equivalent to specifying
DialogType.NATIVE.

getFileName

```java
public
String
getFileName()
```

Specifies the file name for the output file for jobs using these
attributes. This attribute is updated to the value chosen by the user.

**Returns:** the possibly

null

file name

---

#### getFileName

public

String

getFileName()

Specifies the file name for the output file for jobs using these
attributes. This attribute is updated to the value chosen by the user.

setFileName

```java
public void setFileName​(
String
fileName)
```

Specifies the file name for the output file for jobs using these
attributes. Default is platform-dependent and implementation-defined.

**Parameters:** fileName

- the possibly null file name.

---

#### setFileName

public void setFileName​(

String

fileName)

Specifies the file name for the output file for jobs using these
attributes. Default is platform-dependent and implementation-defined.

getFromPage

```java
public int getFromPage()
```

Returns, for jobs using these attributes, the first page to be
printed, if a range of pages is to be printed. This attribute is
updated to the value chosen by the user. An application should ignore
this attribute on output, unless the return value of the

getDefaultSelection

method is DefaultSelectionType.RANGE. An
application should honor the return value of

getPageRanges

over the return value of this method, if possible.

**Returns:** an integer greater than zero and less than or equal to

toPage

and greater than or equal to

minPage

and
less than or equal to

maxPage

.

---

#### getFromPage

public int getFromPage()

Returns, for jobs using these attributes, the first page to be
printed, if a range of pages is to be printed. This attribute is
updated to the value chosen by the user. An application should ignore
this attribute on output, unless the return value of the

getDefaultSelection

method is DefaultSelectionType.RANGE. An
application should honor the return value of

getPageRanges

over the return value of this method, if possible.

setFromPage

```java
public void setFromPage​(int fromPage)
```

Specifies, for jobs using these attributes, the first page to be
printed, if a range of pages is to be printed. If this attribute is not
specified, then the values from the pageRanges attribute are used. If
pageRanges and either or both of fromPage and toPage are specified,
pageRanges takes precedence. Specifying none of pageRanges, fromPage,
or toPage is equivalent to calling
setPageRanges(new int[][] { new int[] {

minPage

} });

**Parameters:** fromPage

- an integer greater than zero and less than or equal to

toPage

and greater than or equal to

minPage

and
less than or equal to

maxPage

.
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated.

---

#### setFromPage

public void setFromPage​(int fromPage)

Specifies, for jobs using these attributes, the first page to be
printed, if a range of pages is to be printed. If this attribute is not
specified, then the values from the pageRanges attribute are used. If
pageRanges and either or both of fromPage and toPage are specified,
pageRanges takes precedence. Specifying none of pageRanges, fromPage,
or toPage is equivalent to calling
setPageRanges(new int[][] { new int[] {

minPage

} });

getMaxPage

```java
public int getMaxPage()
```

Specifies the maximum value the user can specify as the last page to
be printed for jobs using these attributes. This attribute cannot be
modified by, and is not subject to any limitations of, the
implementation or the target printer.

**Returns:** an integer greater than zero and greater than or equal
to

minPage

.

---

#### getMaxPage

public int getMaxPage()

Specifies the maximum value the user can specify as the last page to
be printed for jobs using these attributes. This attribute cannot be
modified by, and is not subject to any limitations of, the
implementation or the target printer.

setMaxPage

```java
public void setMaxPage​(int maxPage)
```

Specifies the maximum value the user can specify as the last page to
be printed for jobs using these attributes. Not specifying this
attribute is equivalent to specifying

Integer.MAX_VALUE

.

**Parameters:** maxPage

- an integer greater than zero and greater than or equal
to

minPage
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated

---

#### setMaxPage

public void setMaxPage​(int maxPage)

Specifies the maximum value the user can specify as the last page to
be printed for jobs using these attributes. Not specifying this
attribute is equivalent to specifying

Integer.MAX_VALUE

.

getMinPage

```java
public int getMinPage()
```

Specifies the minimum value the user can specify as the first page to
be printed for jobs using these attributes. This attribute cannot be
modified by, and is not subject to any limitations of, the
implementation or the target printer.

**Returns:** an integer greater than zero and less than or equal
to

maxPage

.

---

#### getMinPage

public int getMinPage()

Specifies the minimum value the user can specify as the first page to
be printed for jobs using these attributes. This attribute cannot be
modified by, and is not subject to any limitations of, the
implementation or the target printer.

setMinPage

```java
public void setMinPage​(int minPage)
```

Specifies the minimum value the user can specify as the first page to
be printed for jobs using these attributes. Not specifying this
attribute is equivalent to specifying

1

.

**Parameters:** minPage

- an integer greater than zero and less than or equal
to

maxPage

.
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated.

---

#### setMinPage

public void setMinPage​(int minPage)

Specifies the minimum value the user can specify as the first page to
be printed for jobs using these attributes. Not specifying this
attribute is equivalent to specifying

1

.

getMultipleDocumentHandling

```java
public
JobAttributes.MultipleDocumentHandlingType
getMultipleDocumentHandling()
```

Specifies the handling of multiple copies, including collation, for
jobs using these attributes. This attribute is updated to the value
chosen by the user.

**Returns:** MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_COLLATED_COPIES or
MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES.

---

#### getMultipleDocumentHandling

public

JobAttributes.MultipleDocumentHandlingType

getMultipleDocumentHandling()

Specifies the handling of multiple copies, including collation, for
jobs using these attributes. This attribute is updated to the value
chosen by the user.

setMultipleDocumentHandling

```java
public void setMultipleDocumentHandling​(
JobAttributes.MultipleDocumentHandlingType
multipleDocumentHandling)
```

Specifies the handling of multiple copies, including collation, for
jobs using these attributes. Not specifying this attribute is equivalent
to specifying
MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES.

**Parameters:** multipleDocumentHandling

- MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_COLLATED_COPIES or
MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES.
**Throws:** IllegalArgumentException

- if multipleDocumentHandling is null.

---

#### setMultipleDocumentHandling

public void setMultipleDocumentHandling​(

JobAttributes.MultipleDocumentHandlingType

multipleDocumentHandling)

Specifies the handling of multiple copies, including collation, for
jobs using these attributes. Not specifying this attribute is equivalent
to specifying
MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES.

setMultipleDocumentHandlingToDefault

```java
public void setMultipleDocumentHandlingToDefault()
```

Sets the handling of multiple copies, including collation, for jobs
using these attributes to the default. The default handling is
MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES.

---

#### setMultipleDocumentHandlingToDefault

public void setMultipleDocumentHandlingToDefault()

Sets the handling of multiple copies, including collation, for jobs
using these attributes to the default. The default handling is
MultipleDocumentHandlingType.SEPARATE_DOCUMENTS_UNCOLLATED_COPIES.

getPageRanges

```java
public int[][] getPageRanges()
```

Specifies, for jobs using these attributes, the ranges of pages to be
printed, if a range of pages is to be printed. All range numbers are
inclusive. This attribute is updated to the value chosen by the user.
An application should ignore this attribute on output, unless the
return value of the

getDefaultSelection

method is
DefaultSelectionType.RANGE.

**Returns:** an array of integer arrays of 2 elements. An array
is interpreted as a range spanning all pages including and
between the specified pages. Ranges must be in ascending
order and must not overlap. Specified page numbers cannot be
less than

minPage

nor greater than

maxPage

.
For example:
(new int[][] { new int[] { 1, 3 }, new int[] { 5, 5 },
new int[] { 15, 19 } }),
specifies pages 1, 2, 3, 5, 15, 16, 17, 18, and 19.

---

#### getPageRanges

public int[][] getPageRanges()

Specifies, for jobs using these attributes, the ranges of pages to be
printed, if a range of pages is to be printed. All range numbers are
inclusive. This attribute is updated to the value chosen by the user.
An application should ignore this attribute on output, unless the
return value of the

getDefaultSelection

method is
DefaultSelectionType.RANGE.

setPageRanges

```java
public void setPageRanges​(int[][] pageRanges)
```

Specifies, for jobs using these attributes, the ranges of pages to be
printed, if a range of pages is to be printed. All range numbers are
inclusive. If this attribute is not specified, then the values from the
fromPage and toPages attributes are used. If pageRanges and either or
both of fromPage and toPage are specified, pageRanges takes precedence.
Specifying none of pageRanges, fromPage, or toPage is equivalent to
calling setPageRanges(new int[][] { new int[] {

minPage

,

minPage

} });

**Parameters:** pageRanges

- an array of integer arrays of 2 elements. An array
is interpreted as a range spanning all pages including and
between the specified pages. Ranges must be in ascending
order and must not overlap. Specified page numbers cannot be
less than

minPage

nor greater than

maxPage

.
For example:
(new int[][] { new int[] { 1, 3 }, new int[] { 5, 5 },
new int[] { 15, 19 } }),
specifies pages 1, 2, 3, 5, 15, 16, 17, 18, and 19. Note that
(new int[][] { new int[] { 1, 1 }, new int[] { 1, 2 } }),
is an invalid set of page ranges because the two ranges
overlap.
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated.

---

#### setPageRanges

public void setPageRanges​(int[][] pageRanges)

Specifies, for jobs using these attributes, the ranges of pages to be
printed, if a range of pages is to be printed. All range numbers are
inclusive. If this attribute is not specified, then the values from the
fromPage and toPages attributes are used. If pageRanges and either or
both of fromPage and toPage are specified, pageRanges takes precedence.
Specifying none of pageRanges, fromPage, or toPage is equivalent to
calling setPageRanges(new int[][] { new int[] {

minPage

,

minPage

} });

getPrinter

```java
public
String
getPrinter()
```

Returns the destination printer for jobs using these attributes. This
attribute is updated to the value chosen by the user.

**Returns:** the possibly null printer name.

---

#### getPrinter

public

String

getPrinter()

Returns the destination printer for jobs using these attributes. This
attribute is updated to the value chosen by the user.

setPrinter

```java
public void setPrinter​(
String
printer)
```

Specifies the destination printer for jobs using these attributes.
Default is platform-dependent and implementation-defined.

**Parameters:** printer

- the possibly null printer name.

---

#### setPrinter

public void setPrinter​(

String

printer)

Specifies the destination printer for jobs using these attributes.
Default is platform-dependent and implementation-defined.

getSides

```java
public
JobAttributes.SidesType
getSides()
```

Returns how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes. SidesType.ONE_SIDED
imposes each consecutive page upon the same side of consecutive media
sheets. This imposition is sometimes called

simplex

.
SidesType.TWO_SIDED_LONG_EDGE imposes each consecutive pair of pages
upon front and back sides of consecutive media sheets, such that the
orientation of each pair of pages on the medium would be correct for
the reader as if for binding on the long edge. This imposition is
sometimes called

duplex

. SidesType.TWO_SIDED_SHORT_EDGE imposes
each consecutive pair of pages upon front and back sides of consecutive
media sheets, such that the orientation of each pair of pages on the
medium would be correct for the reader as if for binding on the short
edge. This imposition is sometimes called

tumble

. This attribute
is updated to the value chosen by the user.

**Returns:** SidesType.ONE_SIDED, SidesType.TWO_SIDED_LONG_EDGE, or
SidesType.TWO_SIDED_SHORT_EDGE.

---

#### getSides

public

JobAttributes.SidesType

getSides()

Returns how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes. SidesType.ONE_SIDED
imposes each consecutive page upon the same side of consecutive media
sheets. This imposition is sometimes called

simplex

.
SidesType.TWO_SIDED_LONG_EDGE imposes each consecutive pair of pages
upon front and back sides of consecutive media sheets, such that the
orientation of each pair of pages on the medium would be correct for
the reader as if for binding on the long edge. This imposition is
sometimes called

duplex

. SidesType.TWO_SIDED_SHORT_EDGE imposes
each consecutive pair of pages upon front and back sides of consecutive
media sheets, such that the orientation of each pair of pages on the
medium would be correct for the reader as if for binding on the short
edge. This imposition is sometimes called

tumble

. This attribute
is updated to the value chosen by the user.

setSides

```java
public void setSides​(
JobAttributes.SidesType
sides)
```

Specifies how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes. SidesType.ONE_SIDED
imposes each consecutive page upon the same side of consecutive media
sheets. This imposition is sometimes called

simplex

.
SidesType.TWO_SIDED_LONG_EDGE imposes each consecutive pair of pages
upon front and back sides of consecutive media sheets, such that the
orientation of each pair of pages on the medium would be correct for
the reader as if for binding on the long edge. This imposition is
sometimes called

duplex

. SidesType.TWO_SIDED_SHORT_EDGE imposes
each consecutive pair of pages upon front and back sides of consecutive
media sheets, such that the orientation of each pair of pages on the
medium would be correct for the reader as if for binding on the short
edge. This imposition is sometimes called

tumble

. Not specifying
this attribute is equivalent to specifying SidesType.ONE_SIDED.

**Parameters:** sides

- SidesType.ONE_SIDED, SidesType.TWO_SIDED_LONG_EDGE, or
SidesType.TWO_SIDED_SHORT_EDGE.
**Throws:** IllegalArgumentException

- if sides is null.

---

#### setSides

public void setSides​(

JobAttributes.SidesType

sides)

Specifies how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes. SidesType.ONE_SIDED
imposes each consecutive page upon the same side of consecutive media
sheets. This imposition is sometimes called

simplex

.
SidesType.TWO_SIDED_LONG_EDGE imposes each consecutive pair of pages
upon front and back sides of consecutive media sheets, such that the
orientation of each pair of pages on the medium would be correct for
the reader as if for binding on the long edge. This imposition is
sometimes called

duplex

. SidesType.TWO_SIDED_SHORT_EDGE imposes
each consecutive pair of pages upon front and back sides of consecutive
media sheets, such that the orientation of each pair of pages on the
medium would be correct for the reader as if for binding on the short
edge. This imposition is sometimes called

tumble

. Not specifying
this attribute is equivalent to specifying SidesType.ONE_SIDED.

setSidesToDefault

```java
public void setSidesToDefault()
```

Sets how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes to the default. The
default imposition is SidesType.ONE_SIDED.

---

#### setSidesToDefault

public void setSidesToDefault()

Sets how consecutive pages should be imposed upon the sides of the
print medium for jobs using these attributes to the default. The
default imposition is SidesType.ONE_SIDED.

getToPage

```java
public int getToPage()
```

Returns, for jobs using these attributes, the last page (inclusive)
to be printed, if a range of pages is to be printed. This attribute is
updated to the value chosen by the user. An application should ignore
this attribute on output, unless the return value of the

getDefaultSelection

method is DefaultSelectionType.RANGE. An
application should honor the return value of

getPageRanges

over the return value of this method, if possible.

**Returns:** an integer greater than zero and greater than or equal
to

toPage

and greater than or equal to

minPage

and less than or equal to

maxPage

.

---

#### getToPage

public int getToPage()

Returns, for jobs using these attributes, the last page (inclusive)
to be printed, if a range of pages is to be printed. This attribute is
updated to the value chosen by the user. An application should ignore
this attribute on output, unless the return value of the

getDefaultSelection

method is DefaultSelectionType.RANGE. An
application should honor the return value of

getPageRanges

over the return value of this method, if possible.

setToPage

```java
public void setToPage​(int toPage)
```

Specifies, for jobs using these attributes, the last page (inclusive)
to be printed, if a range of pages is to be printed.
If this attribute is not specified, then the values from the pageRanges
attribute are used. If pageRanges and either or both of fromPage and
toPage are specified, pageRanges takes precedence. Specifying none of
pageRanges, fromPage, or toPage is equivalent to calling
setPageRanges(new int[][] { new int[] {

minPage

} });

**Parameters:** toPage

- an integer greater than zero and greater than or equal
to

fromPage

and greater than or equal to

minPage

and less than or equal to

maxPage

.
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated.

---

#### setToPage

public void setToPage​(int toPage)

Specifies, for jobs using these attributes, the last page (inclusive)
to be printed, if a range of pages is to be printed.
If this attribute is not specified, then the values from the pageRanges
attribute are used. If pageRanges and either or both of fromPage and
toPage are specified, pageRanges takes precedence. Specifying none of
pageRanges, fromPage, or toPage is equivalent to calling
setPageRanges(new int[][] { new int[] {

minPage

} });

equals

```java
public boolean equals​(
Object
obj)
```

Determines whether two JobAttributes are equal to each other.

Two JobAttributes are equal if and only if each of their attributes are
equal. Attributes of enumeration type are equal if and only if the
fields refer to the same unique enumeration object. A set of page
ranges is equal if and only if the sets are of equal length, each range
enumerates the same pages, and the ranges are in the same order.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object whose equality will be checked.
**Returns:** whether obj is equal to this JobAttribute according to the
above criteria.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Determines whether two JobAttributes are equal to each other.

Two JobAttributes are equal if and only if each of their attributes are
equal. Attributes of enumeration type are equal if and only if the
fields refer to the same unique enumeration object. A set of page
ranges is equal if and only if the sets are of equal length, each range
enumerates the same pages, and the ranges are in the same order.

Two JobAttributes are equal if and only if each of their attributes are
equal. Attributes of enumeration type are equal if and only if the
fields refer to the same unique enumeration object. A set of page
ranges is equal if and only if the sets are of equal length, each range
enumerates the same pages, and the ranges are in the same order.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this JobAttributes.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code value for this JobAttributes.

toString

```java
public
String
toString()
```

Returns a string representation of this JobAttributes.

**Overrides:** toString

in class

Object
**Returns:** the string representation.

---

#### toString

public

String

toString()

Returns a string representation of this JobAttributes.

---

