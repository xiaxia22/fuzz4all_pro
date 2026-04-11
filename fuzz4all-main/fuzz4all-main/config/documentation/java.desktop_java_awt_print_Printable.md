# Interface Printable

**Source:** `java.desktop\java\awt\print\Printable.html`

### Class Description

```java
public interface
Printable
```

The

Printable

interface is implemented
by the

print

methods of the current
page painter, which is called by the printing
system to render a page. When building a

Pageable

, pairs of

PageFormat

instances and instances that implement
this interface are used to describe each page. The
instance implementing

Printable

is called to
print the page's graphics.

A

Printable(..)

may be set on a

PrinterJob

.
When the client subsequently initiates printing by calling

PrinterJob.print(..)

control

is handed to the printing system until all pages have been printed.
It does this by calling

Printable.print(..)

until
all pages in the document have been printed.
In using the

Printable

interface the printing
commits to image the contents of a page whenever
requested by the printing system.

The parameters to

Printable.print(..)

include a

PageFormat

which describes the printable area of
the page, needed for calculating the contents that will fit the
page, and the page index, which specifies the zero-based print
stream index of the requested page.

For correct printing behaviour, the following points should be
observed:

- The printing system may request a page index more than once.
On each occasion equal PageFormat parameters will be supplied.

The printing system will call

Printable.print(..)

with page indexes which increase monotonically, although as noted above,
the

Printable

should expect multiple calls for a page index
and that page indexes may be skipped, when page ranges are specified
by the client, or by a user through a print dialog.

If multiple collated copies of a document are requested, and the
printer cannot natively support this, then the document may be imaged
multiple times. Printing will start each copy from the lowest print
stream page index page.

With the exception of re-imaging an entire document for multiple
collated copies, the increasing page index order means that when
page N is requested if a client needs to calculate page break position,
it may safely discard any state related to pages < N, and make current
that for page N. "State" usually is just the calculated position in the
document that corresponds to the start of the page.

When called by the printing system the

Printable

must
inspect and honour the supplied PageFormat parameter as well as the
page index. The format of the page to be drawn is specified by the
supplied PageFormat. The size, orientation and imageable area of the page
is therefore already determined and rendering must be within this
imageable area.
This is key to correct printing behaviour, and it has the
implication that the client has the responsibility of tracking
what content belongs on the specified page.

When the

Printable

is obtained from a client-supplied

Pageable

then the client may provide different PageFormats
for each page index. Calculations of page breaks must account for this.

**See Also:** Pageable

,

PageFormat

,

PrinterJob

---

### Field Details

#### static final int PAGE_EXISTS

Returned from

print(Graphics, PageFormat, int)

to signify that the requested page was rendered.

**See Also:**
- Constant Field Values

---

#### static final int NO_SUCH_PAGE

Returned from

print

to signify that the

pageIndex

is too large and that the requested page
does not exist.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### int print​(
Graphics
graphics,

PageFormat
pageFormat,
int pageIndex)
throws
PrinterException

Prints the page at the specified index into the specified

Graphics

context in the specified
format. A

PrinterJob

calls the

Printable

interface to request that a page be
rendered into the context specified by

graphics

. The format of the page to be drawn is
specified by

pageFormat

. The zero based index
of the requested page is specified by

pageIndex

.
If the requested page does not exist then this method returns
NO_SUCH_PAGE; otherwise PAGE_EXISTS is returned.
The

Graphics

class or subclass implements the

PrinterGraphics

interface to provide additional
information. If the

Printable

object
aborts the print job then it throws a

PrinterException

.

**Parameters:**
- graphics

- the context into which the page is drawn
- pageFormat

- the size and orientation of the page being drawn
- pageIndex

- the zero based index of the page to be drawn

**Returns:**
- PAGE_EXISTS if the page is rendered successfully
or NO_SUCH_PAGE if

pageIndex

specifies a
non-existent page.

**Throws:**
- PrinterException

- thrown when the print job is terminated.

---

### Additional Sections

#### Interface Printable

```java
public interface
Printable
```

The

Printable

interface is implemented
by the

print

methods of the current
page painter, which is called by the printing
system to render a page. When building a

Pageable

, pairs of

PageFormat

instances and instances that implement
this interface are used to describe each page. The
instance implementing

Printable

is called to
print the page's graphics.

A

Printable(..)

may be set on a

PrinterJob

.
When the client subsequently initiates printing by calling

PrinterJob.print(..)

control

is handed to the printing system until all pages have been printed.
It does this by calling

Printable.print(..)

until
all pages in the document have been printed.
In using the

Printable

interface the printing
commits to image the contents of a page whenever
requested by the printing system.

The parameters to

Printable.print(..)

include a

PageFormat

which describes the printable area of
the page, needed for calculating the contents that will fit the
page, and the page index, which specifies the zero-based print
stream index of the requested page.

For correct printing behaviour, the following points should be
observed:

- The printing system may request a page index more than once.
On each occasion equal PageFormat parameters will be supplied.

The printing system will call

Printable.print(..)

with page indexes which increase monotonically, although as noted above,
the

Printable

should expect multiple calls for a page index
and that page indexes may be skipped, when page ranges are specified
by the client, or by a user through a print dialog.

If multiple collated copies of a document are requested, and the
printer cannot natively support this, then the document may be imaged
multiple times. Printing will start each copy from the lowest print
stream page index page.

With the exception of re-imaging an entire document for multiple
collated copies, the increasing page index order means that when
page N is requested if a client needs to calculate page break position,
it may safely discard any state related to pages < N, and make current
that for page N. "State" usually is just the calculated position in the
document that corresponds to the start of the page.

When called by the printing system the

Printable

must
inspect and honour the supplied PageFormat parameter as well as the
page index. The format of the page to be drawn is specified by the
supplied PageFormat. The size, orientation and imageable area of the page
is therefore already determined and rendering must be within this
imageable area.
This is key to correct printing behaviour, and it has the
implication that the client has the responsibility of tracking
what content belongs on the specified page.

When the

Printable

is obtained from a client-supplied

Pageable

then the client may provide different PageFormats
for each page index. Calculations of page breaks must account for this.

**See Also:** Pageable

,

PageFormat

,

PrinterJob

public interface

Printable

The

Printable

interface is implemented
by the

print

methods of the current
page painter, which is called by the printing
system to render a page. When building a

Pageable

, pairs of

PageFormat

instances and instances that implement
this interface are used to describe each page. The
instance implementing

Printable

is called to
print the page's graphics.

A

Printable(..)

may be set on a

PrinterJob

.
When the client subsequently initiates printing by calling

PrinterJob.print(..)

control

is handed to the printing system until all pages have been printed.
It does this by calling

Printable.print(..)

until
all pages in the document have been printed.
In using the

Printable

interface the printing
commits to image the contents of a page whenever
requested by the printing system.

The parameters to

Printable.print(..)

include a

PageFormat

which describes the printable area of
the page, needed for calculating the contents that will fit the
page, and the page index, which specifies the zero-based print
stream index of the requested page.

For correct printing behaviour, the following points should be
observed:

- The printing system may request a page index more than once.
On each occasion equal PageFormat parameters will be supplied.

The printing system will call

Printable.print(..)

with page indexes which increase monotonically, although as noted above,
the

Printable

should expect multiple calls for a page index
and that page indexes may be skipped, when page ranges are specified
by the client, or by a user through a print dialog.

If multiple collated copies of a document are requested, and the
printer cannot natively support this, then the document may be imaged
multiple times. Printing will start each copy from the lowest print
stream page index page.

With the exception of re-imaging an entire document for multiple
collated copies, the increasing page index order means that when
page N is requested if a client needs to calculate page break position,
it may safely discard any state related to pages < N, and make current
that for page N. "State" usually is just the calculated position in the
document that corresponds to the start of the page.

When called by the printing system the

Printable

must
inspect and honour the supplied PageFormat parameter as well as the
page index. The format of the page to be drawn is specified by the
supplied PageFormat. The size, orientation and imageable area of the page
is therefore already determined and rendering must be within this
imageable area.
This is key to correct printing behaviour, and it has the
implication that the client has the responsibility of tracking
what content belongs on the specified page.

When the

Printable

is obtained from a client-supplied

Pageable

then the client may provide different PageFormats
for each page index. Calculations of page breaks must account for this.

A

Printable(..)

may be set on a

PrinterJob

.
When the client subsequently initiates printing by calling

PrinterJob.print(..)

control

is handed to the printing system until all pages have been printed.
It does this by calling

Printable.print(..)

until
all pages in the document have been printed.
In using the

Printable

interface the printing
commits to image the contents of a page whenever
requested by the printing system.

The parameters to

Printable.print(..)

include a

PageFormat

which describes the printable area of
the page, needed for calculating the contents that will fit the
page, and the page index, which specifies the zero-based print
stream index of the requested page.

For correct printing behaviour, the following points should be
observed:

- The printing system may request a page index more than once.
On each occasion equal PageFormat parameters will be supplied.

The printing system will call

Printable.print(..)

with page indexes which increase monotonically, although as noted above,
the

Printable

should expect multiple calls for a page index
and that page indexes may be skipped, when page ranges are specified
by the client, or by a user through a print dialog.

If multiple collated copies of a document are requested, and the
printer cannot natively support this, then the document may be imaged
multiple times. Printing will start each copy from the lowest print
stream page index page.

With the exception of re-imaging an entire document for multiple
collated copies, the increasing page index order means that when
page N is requested if a client needs to calculate page break position,
it may safely discard any state related to pages < N, and make current
that for page N. "State" usually is just the calculated position in the
document that corresponds to the start of the page.

When called by the printing system the

Printable

must
inspect and honour the supplied PageFormat parameter as well as the
page index. The format of the page to be drawn is specified by the
supplied PageFormat. The size, orientation and imageable area of the page
is therefore already determined and rendering must be within this
imageable area.
This is key to correct printing behaviour, and it has the
implication that the client has the responsibility of tracking
what content belongs on the specified page.

When the

Printable

is obtained from a client-supplied

Pageable

then the client may provide different PageFormats
for each page index. Calculations of page breaks must account for this.

is handed to the printing system until all pages have been printed.
It does this by calling

Printable.print(..)

until
all pages in the document have been printed.
In using the

Printable

interface the printing
commits to image the contents of a page whenever
requested by the printing system.

The parameters to

Printable.print(..)

include a

PageFormat

which describes the printable area of
the page, needed for calculating the contents that will fit the
page, and the page index, which specifies the zero-based print
stream index of the requested page.

For correct printing behaviour, the following points should be
observed:

- The printing system may request a page index more than once.
On each occasion equal PageFormat parameters will be supplied.

The printing system will call

Printable.print(..)

with page indexes which increase monotonically, although as noted above,
the

Printable

should expect multiple calls for a page index
and that page indexes may be skipped, when page ranges are specified
by the client, or by a user through a print dialog.

If multiple collated copies of a document are requested, and the
printer cannot natively support this, then the document may be imaged
multiple times. Printing will start each copy from the lowest print
stream page index page.

With the exception of re-imaging an entire document for multiple
collated copies, the increasing page index order means that when
page N is requested if a client needs to calculate page break position,
it may safely discard any state related to pages < N, and make current
that for page N. "State" usually is just the calculated position in the
document that corresponds to the start of the page.

When called by the printing system the

Printable

must
inspect and honour the supplied PageFormat parameter as well as the
page index. The format of the page to be drawn is specified by the
supplied PageFormat. The size, orientation and imageable area of the page
is therefore already determined and rendering must be within this
imageable area.
This is key to correct printing behaviour, and it has the
implication that the client has the responsibility of tracking
what content belongs on the specified page.

When the

Printable

is obtained from a client-supplied

Pageable

then the client may provide different PageFormats
for each page index. Calculations of page breaks must account for this.

The parameters to

Printable.print(..)

include a

PageFormat

which describes the printable area of
the page, needed for calculating the contents that will fit the
page, and the page index, which specifies the zero-based print
stream index of the requested page.

For correct printing behaviour, the following points should be
observed:

- The printing system may request a page index more than once.
On each occasion equal PageFormat parameters will be supplied.

The printing system will call

Printable.print(..)

with page indexes which increase monotonically, although as noted above,
the

Printable

should expect multiple calls for a page index
and that page indexes may be skipped, when page ranges are specified
by the client, or by a user through a print dialog.

If multiple collated copies of a document are requested, and the
printer cannot natively support this, then the document may be imaged
multiple times. Printing will start each copy from the lowest print
stream page index page.

With the exception of re-imaging an entire document for multiple
collated copies, the increasing page index order means that when
page N is requested if a client needs to calculate page break position,
it may safely discard any state related to pages < N, and make current
that for page N. "State" usually is just the calculated position in the
document that corresponds to the start of the page.

When called by the printing system the

Printable

must
inspect and honour the supplied PageFormat parameter as well as the
page index. The format of the page to be drawn is specified by the
supplied PageFormat. The size, orientation and imageable area of the page
is therefore already determined and rendering must be within this
imageable area.
This is key to correct printing behaviour, and it has the
implication that the client has the responsibility of tracking
what content belongs on the specified page.

When the

Printable

is obtained from a client-supplied

Pageable

then the client may provide different PageFormats
for each page index. Calculations of page breaks must account for this.

For correct printing behaviour, the following points should be
observed:

- The printing system may request a page index more than once.
On each occasion equal PageFormat parameters will be supplied.

The printing system will call

Printable.print(..)

with page indexes which increase monotonically, although as noted above,
the

Printable

should expect multiple calls for a page index
and that page indexes may be skipped, when page ranges are specified
by the client, or by a user through a print dialog.

If multiple collated copies of a document are requested, and the
printer cannot natively support this, then the document may be imaged
multiple times. Printing will start each copy from the lowest print
stream page index page.

With the exception of re-imaging an entire document for multiple
collated copies, the increasing page index order means that when
page N is requested if a client needs to calculate page break position,
it may safely discard any state related to pages < N, and make current
that for page N. "State" usually is just the calculated position in the
document that corresponds to the start of the page.

When called by the printing system the

Printable

must
inspect and honour the supplied PageFormat parameter as well as the
page index. The format of the page to be drawn is specified by the
supplied PageFormat. The size, orientation and imageable area of the page
is therefore already determined and rendering must be within this
imageable area.
This is key to correct printing behaviour, and it has the
implication that the client has the responsibility of tracking
what content belongs on the specified page.

When the

Printable

is obtained from a client-supplied

Pageable

then the client may provide different PageFormats
for each page index. Calculations of page breaks must account for this.

The printing system may request a page index more than once.
On each occasion equal PageFormat parameters will be supplied.

The printing system will call

Printable.print(..)

with page indexes which increase monotonically, although as noted above,
the

Printable

should expect multiple calls for a page index
and that page indexes may be skipped, when page ranges are specified
by the client, or by a user through a print dialog.

If multiple collated copies of a document are requested, and the
printer cannot natively support this, then the document may be imaged
multiple times. Printing will start each copy from the lowest print
stream page index page.

With the exception of re-imaging an entire document for multiple
collated copies, the increasing page index order means that when
page N is requested if a client needs to calculate page break position,
it may safely discard any state related to pages < N, and make current
that for page N. "State" usually is just the calculated position in the
document that corresponds to the start of the page.

When called by the printing system the

Printable

must
inspect and honour the supplied PageFormat parameter as well as the
page index. The format of the page to be drawn is specified by the
supplied PageFormat. The size, orientation and imageable area of the page
is therefore already determined and rendering must be within this
imageable area.
This is key to correct printing behaviour, and it has the
implication that the client has the responsibility of tracking
what content belongs on the specified page.

When the

Printable

is obtained from a client-supplied

Pageable

then the client may provide different PageFormats
for each page index. Calculations of page breaks must account for this.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

NO_SUCH_PAGE

Returned from

print

to signify that the

pageIndex

is too large and that the requested page
does not exist.

static int

PAGE_EXISTS

Returned from

print(Graphics, PageFormat, int)

to signify that the requested page was rendered.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

print

​(

Graphics

graphics,

PageFormat

pageFormat,
int pageIndex)

Prints the page at the specified index into the specified

Graphics

context in the specified
format.

Field Summary

Fields

Modifier and Type

Field

Description

static int

NO_SUCH_PAGE

Returned from

print

to signify that the

pageIndex

is too large and that the requested page
does not exist.

static int

PAGE_EXISTS

Returned from

print(Graphics, PageFormat, int)

to signify that the requested page was rendered.

---

#### Field Summary

Returned from

print

to signify that the

pageIndex

is too large and that the requested page
does not exist.

Returned from

print(Graphics, PageFormat, int)

to signify that the requested page was rendered.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

print

​(

Graphics

graphics,

PageFormat

pageFormat,
int pageIndex)

Prints the page at the specified index into the specified

Graphics

context in the specified
format.

---

#### Method Summary

Prints the page at the specified index into the specified

Graphics

context in the specified
format.

============ FIELD DETAIL ===========

- Field Detail

- PAGE_EXISTS

```java
static final int PAGE_EXISTS
```

Returned from

print(Graphics, PageFormat, int)

to signify that the requested page was rendered.

**See Also:** Constant Field Values

- NO_SUCH_PAGE

```java
static final int NO_SUCH_PAGE
```

Returned from

print

to signify that the

pageIndex

is too large and that the requested page
does not exist.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- print

```java
int print​(
Graphics
graphics,

PageFormat
pageFormat,
int pageIndex)
throws
PrinterException
```

Prints the page at the specified index into the specified

Graphics

context in the specified
format. A

PrinterJob

calls the

Printable

interface to request that a page be
rendered into the context specified by

graphics

. The format of the page to be drawn is
specified by

pageFormat

. The zero based index
of the requested page is specified by

pageIndex

.
If the requested page does not exist then this method returns
NO_SUCH_PAGE; otherwise PAGE_EXISTS is returned.
The

Graphics

class or subclass implements the

PrinterGraphics

interface to provide additional
information. If the

Printable

object
aborts the print job then it throws a

PrinterException

.

**Parameters:** graphics

- the context into which the page is drawn
**Parameters:** pageFormat

- the size and orientation of the page being drawn
**Parameters:** pageIndex

- the zero based index of the page to be drawn
**Returns:** PAGE_EXISTS if the page is rendered successfully
or NO_SUCH_PAGE if

pageIndex

specifies a
non-existent page.
**Throws:** PrinterException

- thrown when the print job is terminated.

Field Detail

- PAGE_EXISTS

```java
static final int PAGE_EXISTS
```

Returned from

print(Graphics, PageFormat, int)

to signify that the requested page was rendered.

**See Also:** Constant Field Values

- NO_SUCH_PAGE

```java
static final int NO_SUCH_PAGE
```

Returned from

print

to signify that the

pageIndex

is too large and that the requested page
does not exist.

**See Also:** Constant Field Values

---

#### Field Detail

PAGE_EXISTS

```java
static final int PAGE_EXISTS
```

Returned from

print(Graphics, PageFormat, int)

to signify that the requested page was rendered.

**See Also:** Constant Field Values

---

#### PAGE_EXISTS

static final int PAGE_EXISTS

Returned from

print(Graphics, PageFormat, int)

to signify that the requested page was rendered.

NO_SUCH_PAGE

```java
static final int NO_SUCH_PAGE
```

Returned from

print

to signify that the

pageIndex

is too large and that the requested page
does not exist.

**See Also:** Constant Field Values

---

#### NO_SUCH_PAGE

static final int NO_SUCH_PAGE

Returned from

print

to signify that the

pageIndex

is too large and that the requested page
does not exist.

Method Detail

- print

```java
int print​(
Graphics
graphics,

PageFormat
pageFormat,
int pageIndex)
throws
PrinterException
```

Prints the page at the specified index into the specified

Graphics

context in the specified
format. A

PrinterJob

calls the

Printable

interface to request that a page be
rendered into the context specified by

graphics

. The format of the page to be drawn is
specified by

pageFormat

. The zero based index
of the requested page is specified by

pageIndex

.
If the requested page does not exist then this method returns
NO_SUCH_PAGE; otherwise PAGE_EXISTS is returned.
The

Graphics

class or subclass implements the

PrinterGraphics

interface to provide additional
information. If the

Printable

object
aborts the print job then it throws a

PrinterException

.

**Parameters:** graphics

- the context into which the page is drawn
**Parameters:** pageFormat

- the size and orientation of the page being drawn
**Parameters:** pageIndex

- the zero based index of the page to be drawn
**Returns:** PAGE_EXISTS if the page is rendered successfully
or NO_SUCH_PAGE if

pageIndex

specifies a
non-existent page.
**Throws:** PrinterException

- thrown when the print job is terminated.

---

#### Method Detail

print

```java
int print​(
Graphics
graphics,

PageFormat
pageFormat,
int pageIndex)
throws
PrinterException
```

Prints the page at the specified index into the specified

Graphics

context in the specified
format. A

PrinterJob

calls the

Printable

interface to request that a page be
rendered into the context specified by

graphics

. The format of the page to be drawn is
specified by

pageFormat

. The zero based index
of the requested page is specified by

pageIndex

.
If the requested page does not exist then this method returns
NO_SUCH_PAGE; otherwise PAGE_EXISTS is returned.
The

Graphics

class or subclass implements the

PrinterGraphics

interface to provide additional
information. If the

Printable

object
aborts the print job then it throws a

PrinterException

.

**Parameters:** graphics

- the context into which the page is drawn
**Parameters:** pageFormat

- the size and orientation of the page being drawn
**Parameters:** pageIndex

- the zero based index of the page to be drawn
**Returns:** PAGE_EXISTS if the page is rendered successfully
or NO_SUCH_PAGE if

pageIndex

specifies a
non-existent page.
**Throws:** PrinterException

- thrown when the print job is terminated.

---

#### print

int print​(

Graphics

graphics,

PageFormat

pageFormat,
int pageIndex)
throws

PrinterException

Prints the page at the specified index into the specified

Graphics

context in the specified
format. A

PrinterJob

calls the

Printable

interface to request that a page be
rendered into the context specified by

graphics

. The format of the page to be drawn is
specified by

pageFormat

. The zero based index
of the requested page is specified by

pageIndex

.
If the requested page does not exist then this method returns
NO_SUCH_PAGE; otherwise PAGE_EXISTS is returned.
The

Graphics

class or subclass implements the

PrinterGraphics

interface to provide additional
information. If the

Printable

object
aborts the print job then it throws a

PrinterException

.

---

