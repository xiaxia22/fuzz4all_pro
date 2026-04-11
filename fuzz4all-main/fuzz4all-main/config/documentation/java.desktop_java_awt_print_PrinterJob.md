# Class PrinterJob

**Source:** `java.desktop\java\awt\print\PrinterJob.html`

### Class Description

```java
public abstract class
PrinterJob

extends
Object
```

The

PrinterJob

class is the principal class that controls
printing. An application calls methods in this class to set up a job,
optionally to invoke a print dialog with the user, and then to print
the pages of the job.

---

### Field Details

*No entries found.*

### Constructor Details

#### public PrinterJob()

A

PrinterJob

object should be created using the
static

getPrinterJob

method.

---

### Method Details

#### public static
PrinterJob
getPrinterJob()

Creates and returns a

PrinterJob

which is initially
associated with the default printer.
If no printers are available on the system, a PrinterJob will still
be returned from this method, but

getPrintService()

will return

null

, and calling

print

with this

PrinterJob

might
generate an exception. Applications that need to determine if
there are suitable printers before creating a

PrinterJob

should ensure that the array returned from

lookupPrintServices

is not empty.

**Returns:**
- a new

PrinterJob

.

**Throws:**
- SecurityException

- if a security manager exists and its

SecurityManager.checkPrintJobAccess()

method disallows this thread from creating a print job request

---

#### public static
PrintService
[] lookupPrintServices()

A convenience method which looks up 2D print services.
Services returned from this method may be installed on

PrinterJob

s which support print services.
Calling this method is equivalent to calling

PrintServiceLookup.lookupPrintServices()

and specifying a Pageable DocFlavor.

**Returns:**
- a possibly empty array of 2D print services.

**Since:**
- 1.4

---

#### public static
StreamPrintServiceFactory
[] lookupStreamPrintServices​(
String
mimeType)

A convenience method which locates factories for stream print
services which can image 2D graphics.
Sample usage :

```java
FileOutputStream outstream;
StreamPrintService psPrinter;
String psMimeType = "application/postscript";
PrinterJob pj = PrinterJob.getPrinterJob();

StreamPrintServiceFactory[] factories =
PrinterJob.lookupStreamPrintServices(psMimeType);
if (factories.length > 0) {
try {
outstream = new File("out.ps");
psPrinter = factories[0].getPrintService(outstream);
// psPrinter can now be set as the service on a PrinterJob
pj.setPrintService(psPrinter)
} catch (Exception e) {
e.printStackTrace();
}
}
```

Services returned from this method may be installed on

PrinterJob

instances which support print services.
Calling this method is equivalent to calling

StreamPrintServiceFactory.lookupStreamPrintServiceFactories()

and specifying a Pageable DocFlavor.

**Parameters:**
- mimeType

- the required output format, or null to mean any format.

**Returns:**
- a possibly empty array of 2D stream print service factories.

**Since:**
- 1.4

---

#### public
PrintService
getPrintService()

Returns the service (printer) for this printer job.
Implementations of this class which do not support print services
may return null. null will also be returned if no printers are
available.

**Returns:**
- the service for this printer job.

**See Also:**
- setPrintService(PrintService)

,

getPrinterJob()

**Since:**
- 1.4

---

#### public void setPrintService​(
PrintService
service)
throws
PrinterException

Associate this PrinterJob with a new PrintService.
This method is overridden by subclasses which support
specifying a Print Service.

Throws

PrinterException

if the specified service
cannot support the

Pageable

and

Printable

interfaces necessary to support 2D printing.

**Parameters:**
- service

- a print service that supports 2D printing

**Throws:**
- PrinterException

- if the specified service does not support
2D printing, or this PrinterJob class does not support
setting a 2D print service, or the specified service is
otherwise not a valid print service.

**See Also:**
- getPrintService()

**Since:**
- 1.4

---

#### public abstract void setPrintable​(
Printable
painter)

Calls

painter

to render the pages. The pages in the
document to be printed by this

PrinterJob

are rendered by the

Printable

object,

painter

. The

PageFormat

for each page
is the default page format.

**Parameters:**
- painter

- the

Printable

that renders each page of
the document.

---

#### public abstract void setPrintable​(
Printable
painter,

PageFormat
format)

Calls

painter

to render the pages in the specified

format

. The pages in the document to be printed by
this

PrinterJob

are rendered by the

Printable

object,

painter

. The

PageFormat

of each page is

format

.

**Parameters:**
- painter

- the

Printable

called to render
each page of the document
- format

- the size and orientation of each page to
be printed

---

#### public abstract void setPageable​(
Pageable
document)
throws
NullPointerException

Queries

document

for the number of pages and
the

PageFormat

and

Printable

for each
page held in the

Pageable

instance,

document

.

**Parameters:**
- document

- the pages to be printed. It can not be

null

.

**Throws:**
- NullPointerException

- the

Pageable

passed in
was

null

.

**See Also:**
- PageFormat

,

Printable

---

#### public abstract boolean printDialog()
throws
HeadlessException

Presents a dialog to the user for changing the properties of
the print job.
This method will display a native dialog if a native print
service is selected, and user choice of printers will be restricted
to these native print services.
To present the cross platform print dialog for all services,
including native ones instead use

printDialog(PrintRequestAttributeSet)

.

PrinterJob implementations which can use PrintService's will update
the PrintService for this PrinterJob to reflect the new service
selected by the user.

**Returns:**
- true

if the user does not cancel the dialog;

false

otherwise.

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public boolean printDialog​(
PrintRequestAttributeSet
attributes)
throws
HeadlessException

A convenience method which displays a cross-platform print dialog
for all services which are capable of printing 2D graphics using the

Pageable

interface. The selected printer when the
dialog is initially displayed will reflect the print service currently
attached to this print job.
If the user changes the print service, the PrinterJob will be
updated to reflect this, unless the user cancels the dialog.
As well as allowing the user to select the destination printer,
the user can also select values of various print request attributes.

The attributes parameter on input will reflect the applications
required initial selections in the user dialog. Attributes not
specified display using the default for the service. On return it
will reflect the user's choices. Selections may be updated by
the implementation to be consistent with the supported values
for the currently selected print service.

As the user scrolls to a new print service selection, the values
copied are based on the settings for the previous service, together
with any user changes. The values are not based on the original
settings supplied by the client.

With the exception of selected printer, the PrinterJob state is
not updated to reflect the user's changes.
For the selections to affect a printer job, the attributes must
be specified in the call to the

print(PrintRequestAttributeSet)

method. If using
the Pageable interface, clients which intend to use media selected
by the user must create a PageFormat derived from the user's
selections.
If the user cancels the dialog, the attributes will not reflect
any changes made by the user.

**Parameters:**
- attributes

- on input is application supplied attributes,
on output the contents are updated to reflect user choices.
This parameter may not be null.

**Returns:**
- true

if the user does not cancel the dialog;

false

otherwise.

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
- NullPointerException

- if

attributes

parameter
is null.

**See Also:**
- GraphicsEnvironment.isHeadless()

**Since:**
- 1.4

---

#### public abstract
PageFormat
pageDialog​(
PageFormat
page)
throws
HeadlessException

Displays a dialog that allows modification of a

PageFormat

instance.
The

page

argument is used to initialize controls
in the page setup dialog.
If the user cancels the dialog then this method returns the
original

page

object unmodified.
If the user okays the dialog then this method returns a new

PageFormat

object with the indicated changes.
In either case, the original

page

object is
not modified.

**Parameters:**
- page

- the default

PageFormat

presented to the
user for modification

**Returns:**
- the original

page

object if the dialog
is cancelled; a new

PageFormat

object
containing the format indicated by the user if the
dialog is acknowledged.

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.

**See Also:**
- GraphicsEnvironment.isHeadless()

**Since:**
- 1.2

---

#### public
PageFormat
pageDialog​(
PrintRequestAttributeSet
attributes)
throws
HeadlessException

A convenience method which displays a cross-platform page setup dialog.
The choices available will reflect the print service currently
set on this PrinterJob.

The attributes parameter on input will reflect the client's
required initial selections in the user dialog. Attributes which are
not specified display using the default for the service. On return it
will reflect the user's choices. Selections may be updated by
the implementation to be consistent with the supported values
for the currently selected print service.

The return value will be a PageFormat equivalent to the
selections in the PrintRequestAttributeSet.
If the user cancels the dialog, the attributes will not reflect
any changes made by the user, and the return value will be null.

**Parameters:**
- attributes

- on input is application supplied attributes,
on output the contents are updated to reflect user choices.
This parameter may not be null.

**Returns:**
- a page format if the user does not cancel the dialog;

null

otherwise.

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
- NullPointerException

- if

attributes

parameter
is null.

**See Also:**
- GraphicsEnvironment.isHeadless()

**Since:**
- 1.4

---

#### public abstract
PageFormat
defaultPage​(
PageFormat
page)

Clones the

PageFormat

argument and alters the
clone to describe a default page size and orientation.

**Parameters:**
- page

- the

PageFormat

to be cloned and altered

**Returns:**
- clone of

page

, altered to describe a default

PageFormat

.

---

#### public
PageFormat
defaultPage()

Creates a new

PageFormat

instance and
sets it to a default size and orientation.

**Returns:**
- a

PageFormat

set to a default size and
orientation.

---

#### public
PageFormat
getPageFormat​(
PrintRequestAttributeSet
attributes)

Calculates a

PageFormat

with values consistent with those
supported by the current

PrintService

for this job
(ie the value returned by

getPrintService()

) and media,
printable area and orientation contained in

attributes

.

Calling this method does not update the job.
It is useful for clients that have a set of attributes obtained from

printDialog(PrintRequestAttributeSet attributes)

and need a PageFormat to print a Pageable object.

**Parameters:**
- attributes

- a set of printing attributes, for example obtained
from calling printDialog. If

attributes

is null a default
PageFormat is returned.

**Returns:**
- a

PageFormat

whose settings conform with
those of the current service and the specified attributes.

**Since:**
- 1.6

---

#### public abstract
PageFormat
validatePage​(
PageFormat
page)

Returns the clone of

page

with its settings
adjusted to be compatible with the current printer of this

PrinterJob

. For example, the returned

PageFormat

could have its imageable area
adjusted to fit within the physical area of the paper that
is used by the current printer.

**Parameters:**
- page

- the

PageFormat

that is cloned and
whose settings are changed to be compatible with
the current printer

**Returns:**
- a

PageFormat

that is cloned from

page

and whose settings are changed
to conform with this

PrinterJob

.

---

#### public abstract void print()
throws
PrinterException

Prints a set of pages.

**Throws:**
- PrinterException

- an error in the print system
caused the job to be aborted.

**See Also:**
- Book

,

Pageable

,

Printable

---

#### public void print​(
PrintRequestAttributeSet
attributes)
throws
PrinterException

Prints a set of pages using the settings in the attribute
set. The default implementation ignores the attribute set.

Note that some attributes may be set directly on the PrinterJob
by equivalent method calls, (for example), copies:

setCopies(int)

, job name:

setJobName(String)

and specifying media size and orientation though the

PageFormat

object.

If a supported attribute-value is specified in this attribute set,
it will take precedence over the API settings for this print()
operation only.
The following behaviour is specified for PageFormat:
If a client uses the Printable interface, then the

attributes

parameter to this method is examined
for attributes which specify media (by size), orientation, and
imageable area, and those are used to construct a new PageFormat
which is passed to the Printable object's print() method.
See

Printable

for an explanation of the required
behaviour of a Printable to ensure optimal printing via PrinterJob.
For clients of the Pageable interface, the PageFormat will always
be as supplied by that interface, on a per page basis.

These behaviours allow an application to directly pass the
user settings returned from

printDialog(PrintRequestAttributeSet attributes

to
this print() method.

**Parameters:**
- attributes

- a set of attributes for the job

**Throws:**
- PrinterException

- an error in the print system
caused the job to be aborted.

**See Also:**
- Book

,

Pageable

,

Printable

**Since:**
- 1.4

---

#### public abstract void setCopies​(int copies)

Sets the number of copies to be printed.

**Parameters:**
- copies

- the number of copies to be printed

**See Also:**
- getCopies()

---

#### public abstract int getCopies()

Gets the number of copies to be printed.

**Returns:**
- the number of copies to be printed.

**See Also:**
- setCopies(int)

---

#### public abstract
String
getUserName()

Gets the name of the printing user.

**Returns:**
- the name of the printing user

**Throws:**
- SecurityException

- if a security manager exists and
PropertyPermission - user.name is not given in the policy file

---

#### public abstract void setJobName​(
String
jobName)

Sets the name of the document to be printed.
The document name can not be

null

.

**Parameters:**
- jobName

- the name of the document to be printed

**See Also:**
- getJobName()

---

#### public abstract
String
getJobName()

Gets the name of the document to be printed.

**Returns:**
- the name of the document to be printed.

**See Also:**
- setJobName(java.lang.String)

---

#### public abstract void cancel()

Cancels a print job that is in progress. If

print

has been called but has not
returned then this method signals
that the job should be cancelled at the next
chance. If there is no print job in progress then
this call does nothing.

---

#### public abstract boolean isCancelled()

Returns

true

if a print job is
in progress, but is going to be cancelled
at the next opportunity; otherwise returns

false

.

**Returns:**
- true

if the job in progress
is going to be cancelled;

false

otherwise.

---

### Additional Sections

#### Class PrinterJob

java.lang.Object

- java.awt.print.PrinterJob

java.awt.print.PrinterJob

```java
public abstract class
PrinterJob

extends
Object
```

The

PrinterJob

class is the principal class that controls
printing. An application calls methods in this class to set up a job,
optionally to invoke a print dialog with the user, and then to print
the pages of the job.

public abstract class

PrinterJob

extends

Object

The

PrinterJob

class is the principal class that controls
printing. An application calls methods in this class to set up a job,
optionally to invoke a print dialog with the user, and then to print
the pages of the job.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PrinterJob

()

A

PrinterJob

object should be created using the
static

getPrinterJob

method.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

cancel

()

Cancels a print job that is in progress.

PageFormat

defaultPage

()

Creates a new

PageFormat

instance and
sets it to a default size and orientation.

abstract

PageFormat

defaultPage

​(

PageFormat

page)

Clones the

PageFormat

argument and alters the
clone to describe a default page size and orientation.

abstract int

getCopies

()

Gets the number of copies to be printed.

abstract

String

getJobName

()

Gets the name of the document to be printed.

PageFormat

getPageFormat

​(

PrintRequestAttributeSet

attributes)

Calculates a

PageFormat

with values consistent with those
supported by the current

PrintService

for this job
(ie the value returned by

getPrintService()

) and media,
printable area and orientation contained in

attributes

.

static

PrinterJob

getPrinterJob

()

Creates and returns a

PrinterJob

which is initially
associated with the default printer.

PrintService

getPrintService

()

Returns the service (printer) for this printer job.

abstract

String

getUserName

()

Gets the name of the printing user.

abstract boolean

isCancelled

()

Returns

true

if a print job is
in progress, but is going to be cancelled
at the next opportunity; otherwise returns

false

.

static

PrintService

[]

lookupPrintServices

()

A convenience method which looks up 2D print services.

static

StreamPrintServiceFactory

[]

lookupStreamPrintServices

​(

String

mimeType)

A convenience method which locates factories for stream print
services which can image 2D graphics.

abstract

PageFormat

pageDialog

​(

PageFormat

page)

Displays a dialog that allows modification of a

PageFormat

instance.

PageFormat

pageDialog

​(

PrintRequestAttributeSet

attributes)

A convenience method which displays a cross-platform page setup dialog.

abstract void

print

()

Prints a set of pages.

void

print

​(

PrintRequestAttributeSet

attributes)

Prints a set of pages using the settings in the attribute
set.

abstract boolean

printDialog

()

Presents a dialog to the user for changing the properties of
the print job.

boolean

printDialog

​(

PrintRequestAttributeSet

attributes)

A convenience method which displays a cross-platform print dialog
for all services which are capable of printing 2D graphics using the

Pageable

interface.

abstract void

setCopies

​(int copies)

Sets the number of copies to be printed.

abstract void

setJobName

​(

String

jobName)

Sets the name of the document to be printed.

abstract void

setPageable

​(

Pageable

document)

Queries

document

for the number of pages and
the

PageFormat

and

Printable

for each
page held in the

Pageable

instance,

document

.

abstract void

setPrintable

​(

Printable

painter)

Calls

painter

to render the pages.

abstract void

setPrintable

​(

Printable

painter,

PageFormat

format)

Calls

painter

to render the pages in the specified

format

.

void

setPrintService

​(

PrintService

service)

Associate this PrinterJob with a new PrintService.

abstract

PageFormat

validatePage

​(

PageFormat

page)

Returns the clone of

page

with its settings
adjusted to be compatible with the current printer of this

PrinterJob

.

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

Constructor Summary

Constructors

Constructor

Description

PrinterJob

()

A

PrinterJob

object should be created using the
static

getPrinterJob

method.

---

#### Constructor Summary

A

PrinterJob

object should be created using the
static

getPrinterJob

method.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

cancel

()

Cancels a print job that is in progress.

PageFormat

defaultPage

()

Creates a new

PageFormat

instance and
sets it to a default size and orientation.

abstract

PageFormat

defaultPage

​(

PageFormat

page)

Clones the

PageFormat

argument and alters the
clone to describe a default page size and orientation.

abstract int

getCopies

()

Gets the number of copies to be printed.

abstract

String

getJobName

()

Gets the name of the document to be printed.

PageFormat

getPageFormat

​(

PrintRequestAttributeSet

attributes)

Calculates a

PageFormat

with values consistent with those
supported by the current

PrintService

for this job
(ie the value returned by

getPrintService()

) and media,
printable area and orientation contained in

attributes

.

static

PrinterJob

getPrinterJob

()

Creates and returns a

PrinterJob

which is initially
associated with the default printer.

PrintService

getPrintService

()

Returns the service (printer) for this printer job.

abstract

String

getUserName

()

Gets the name of the printing user.

abstract boolean

isCancelled

()

Returns

true

if a print job is
in progress, but is going to be cancelled
at the next opportunity; otherwise returns

false

.

static

PrintService

[]

lookupPrintServices

()

A convenience method which looks up 2D print services.

static

StreamPrintServiceFactory

[]

lookupStreamPrintServices

​(

String

mimeType)

A convenience method which locates factories for stream print
services which can image 2D graphics.

abstract

PageFormat

pageDialog

​(

PageFormat

page)

Displays a dialog that allows modification of a

PageFormat

instance.

PageFormat

pageDialog

​(

PrintRequestAttributeSet

attributes)

A convenience method which displays a cross-platform page setup dialog.

abstract void

print

()

Prints a set of pages.

void

print

​(

PrintRequestAttributeSet

attributes)

Prints a set of pages using the settings in the attribute
set.

abstract boolean

printDialog

()

Presents a dialog to the user for changing the properties of
the print job.

boolean

printDialog

​(

PrintRequestAttributeSet

attributes)

A convenience method which displays a cross-platform print dialog
for all services which are capable of printing 2D graphics using the

Pageable

interface.

abstract void

setCopies

​(int copies)

Sets the number of copies to be printed.

abstract void

setJobName

​(

String

jobName)

Sets the name of the document to be printed.

abstract void

setPageable

​(

Pageable

document)

Queries

document

for the number of pages and
the

PageFormat

and

Printable

for each
page held in the

Pageable

instance,

document

.

abstract void

setPrintable

​(

Printable

painter)

Calls

painter

to render the pages.

abstract void

setPrintable

​(

Printable

painter,

PageFormat

format)

Calls

painter

to render the pages in the specified

format

.

void

setPrintService

​(

PrintService

service)

Associate this PrinterJob with a new PrintService.

abstract

PageFormat

validatePage

​(

PageFormat

page)

Returns the clone of

page

with its settings
adjusted to be compatible with the current printer of this

PrinterJob

.

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

Cancels a print job that is in progress.

Creates a new

PageFormat

instance and
sets it to a default size and orientation.

Clones the

PageFormat

argument and alters the
clone to describe a default page size and orientation.

Gets the number of copies to be printed.

Gets the name of the document to be printed.

Calculates a

PageFormat

with values consistent with those
supported by the current

PrintService

for this job
(ie the value returned by

getPrintService()

) and media,
printable area and orientation contained in

attributes

.

Creates and returns a

PrinterJob

which is initially
associated with the default printer.

Returns the service (printer) for this printer job.

Gets the name of the printing user.

Returns

true

if a print job is
in progress, but is going to be cancelled
at the next opportunity; otherwise returns

false

.

A convenience method which looks up 2D print services.

A convenience method which locates factories for stream print
services which can image 2D graphics.

Displays a dialog that allows modification of a

PageFormat

instance.

A convenience method which displays a cross-platform page setup dialog.

Prints a set of pages.

Prints a set of pages using the settings in the attribute
set.

Presents a dialog to the user for changing the properties of
the print job.

A convenience method which displays a cross-platform print dialog
for all services which are capable of printing 2D graphics using the

Pageable

interface.

Sets the number of copies to be printed.

Sets the name of the document to be printed.

Queries

document

for the number of pages and
the

PageFormat

and

Printable

for each
page held in the

Pageable

instance,

document

.

Calls

painter

to render the pages.

Calls

painter

to render the pages in the specified

format

.

Associate this PrinterJob with a new PrintService.

Returns the clone of

page

with its settings
adjusted to be compatible with the current printer of this

PrinterJob

.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PrinterJob

```java
public PrinterJob()
```

A

PrinterJob

object should be created using the
static

getPrinterJob

method.

============ METHOD DETAIL ==========

- Method Detail

- getPrinterJob

```java
public static
PrinterJob
getPrinterJob()
```

Creates and returns a

PrinterJob

which is initially
associated with the default printer.
If no printers are available on the system, a PrinterJob will still
be returned from this method, but

getPrintService()

will return

null

, and calling

print

with this

PrinterJob

might
generate an exception. Applications that need to determine if
there are suitable printers before creating a

PrinterJob

should ensure that the array returned from

lookupPrintServices

is not empty.

**Returns:** a new

PrinterJob

.
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkPrintJobAccess()

method disallows this thread from creating a print job request

- lookupPrintServices

```java
public static
PrintService
[] lookupPrintServices()
```

A convenience method which looks up 2D print services.
Services returned from this method may be installed on

PrinterJob

s which support print services.
Calling this method is equivalent to calling

PrintServiceLookup.lookupPrintServices()

and specifying a Pageable DocFlavor.

**Returns:** a possibly empty array of 2D print services.
**Since:** 1.4

- lookupStreamPrintServices

```java
public static
StreamPrintServiceFactory
[] lookupStreamPrintServices​(
String
mimeType)
```

A convenience method which locates factories for stream print
services which can image 2D graphics.
Sample usage :

```java
FileOutputStream outstream;
StreamPrintService psPrinter;
String psMimeType = "application/postscript";
PrinterJob pj = PrinterJob.getPrinterJob();

StreamPrintServiceFactory[] factories =
PrinterJob.lookupStreamPrintServices(psMimeType);
if (factories.length > 0) {
try {
outstream = new File("out.ps");
psPrinter = factories[0].getPrintService(outstream);
// psPrinter can now be set as the service on a PrinterJob
pj.setPrintService(psPrinter)
} catch (Exception e) {
e.printStackTrace();
}
}
```

Services returned from this method may be installed on

PrinterJob

instances which support print services.
Calling this method is equivalent to calling

StreamPrintServiceFactory.lookupStreamPrintServiceFactories()

and specifying a Pageable DocFlavor.

**Parameters:** mimeType

- the required output format, or null to mean any format.
**Returns:** a possibly empty array of 2D stream print service factories.
**Since:** 1.4

- getPrintService

```java
public
PrintService
getPrintService()
```

Returns the service (printer) for this printer job.
Implementations of this class which do not support print services
may return null. null will also be returned if no printers are
available.

**Returns:** the service for this printer job.
**Since:** 1.4
**See Also:** setPrintService(PrintService)

,

getPrinterJob()

- setPrintService

```java
public void setPrintService​(
PrintService
service)
throws
PrinterException
```

Associate this PrinterJob with a new PrintService.
This method is overridden by subclasses which support
specifying a Print Service.

Throws

PrinterException

if the specified service
cannot support the

Pageable

and

Printable

interfaces necessary to support 2D printing.

**Parameters:** service

- a print service that supports 2D printing
**Throws:** PrinterException

- if the specified service does not support
2D printing, or this PrinterJob class does not support
setting a 2D print service, or the specified service is
otherwise not a valid print service.
**Since:** 1.4
**See Also:** getPrintService()

- setPrintable

```java
public abstract void setPrintable​(
Printable
painter)
```

Calls

painter

to render the pages. The pages in the
document to be printed by this

PrinterJob

are rendered by the

Printable

object,

painter

. The

PageFormat

for each page
is the default page format.

**Parameters:** painter

- the

Printable

that renders each page of
the document.

- setPrintable

```java
public abstract void setPrintable​(
Printable
painter,

PageFormat
format)
```

Calls

painter

to render the pages in the specified

format

. The pages in the document to be printed by
this

PrinterJob

are rendered by the

Printable

object,

painter

. The

PageFormat

of each page is

format

.

**Parameters:** painter

- the

Printable

called to render
each page of the document
**Parameters:** format

- the size and orientation of each page to
be printed

- setPageable

```java
public abstract void setPageable​(
Pageable
document)
throws
NullPointerException
```

Queries

document

for the number of pages and
the

PageFormat

and

Printable

for each
page held in the

Pageable

instance,

document

.

**Parameters:** document

- the pages to be printed. It can not be

null

.
**Throws:** NullPointerException

- the

Pageable

passed in
was

null

.
**See Also:** PageFormat

,

Printable

- printDialog

```java
public abstract boolean printDialog()
throws
HeadlessException
```

Presents a dialog to the user for changing the properties of
the print job.
This method will display a native dialog if a native print
service is selected, and user choice of printers will be restricted
to these native print services.
To present the cross platform print dialog for all services,
including native ones instead use

printDialog(PrintRequestAttributeSet)

.

PrinterJob implementations which can use PrintService's will update
the PrintService for this PrinterJob to reflect the new service
selected by the user.

**Returns:** true

if the user does not cancel the dialog;

false

otherwise.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

- printDialog

```java
public boolean printDialog​(
PrintRequestAttributeSet
attributes)
throws
HeadlessException
```

A convenience method which displays a cross-platform print dialog
for all services which are capable of printing 2D graphics using the

Pageable

interface. The selected printer when the
dialog is initially displayed will reflect the print service currently
attached to this print job.
If the user changes the print service, the PrinterJob will be
updated to reflect this, unless the user cancels the dialog.
As well as allowing the user to select the destination printer,
the user can also select values of various print request attributes.

The attributes parameter on input will reflect the applications
required initial selections in the user dialog. Attributes not
specified display using the default for the service. On return it
will reflect the user's choices. Selections may be updated by
the implementation to be consistent with the supported values
for the currently selected print service.

As the user scrolls to a new print service selection, the values
copied are based on the settings for the previous service, together
with any user changes. The values are not based on the original
settings supplied by the client.

With the exception of selected printer, the PrinterJob state is
not updated to reflect the user's changes.
For the selections to affect a printer job, the attributes must
be specified in the call to the

print(PrintRequestAttributeSet)

method. If using
the Pageable interface, clients which intend to use media selected
by the user must create a PageFormat derived from the user's
selections.
If the user cancels the dialog, the attributes will not reflect
any changes made by the user.

**Parameters:** attributes

- on input is application supplied attributes,
on output the contents are updated to reflect user choices.
This parameter may not be null.
**Returns:** true

if the user does not cancel the dialog;

false

otherwise.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**Throws:** NullPointerException

- if

attributes

parameter
is null.
**Since:** 1.4
**See Also:** GraphicsEnvironment.isHeadless()

- pageDialog

```java
public abstract
PageFormat
pageDialog​(
PageFormat
page)
throws
HeadlessException
```

Displays a dialog that allows modification of a

PageFormat

instance.
The

page

argument is used to initialize controls
in the page setup dialog.
If the user cancels the dialog then this method returns the
original

page

object unmodified.
If the user okays the dialog then this method returns a new

PageFormat

object with the indicated changes.
In either case, the original

page

object is
not modified.

**Parameters:** page

- the default

PageFormat

presented to the
user for modification
**Returns:** the original

page

object if the dialog
is cancelled; a new

PageFormat

object
containing the format indicated by the user if the
dialog is acknowledged.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**Since:** 1.2
**See Also:** GraphicsEnvironment.isHeadless()

- pageDialog

```java
public
PageFormat
pageDialog​(
PrintRequestAttributeSet
attributes)
throws
HeadlessException
```

A convenience method which displays a cross-platform page setup dialog.
The choices available will reflect the print service currently
set on this PrinterJob.

The attributes parameter on input will reflect the client's
required initial selections in the user dialog. Attributes which are
not specified display using the default for the service. On return it
will reflect the user's choices. Selections may be updated by
the implementation to be consistent with the supported values
for the currently selected print service.

The return value will be a PageFormat equivalent to the
selections in the PrintRequestAttributeSet.
If the user cancels the dialog, the attributes will not reflect
any changes made by the user, and the return value will be null.

**Parameters:** attributes

- on input is application supplied attributes,
on output the contents are updated to reflect user choices.
This parameter may not be null.
**Returns:** a page format if the user does not cancel the dialog;

null

otherwise.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**Throws:** NullPointerException

- if

attributes

parameter
is null.
**Since:** 1.4
**See Also:** GraphicsEnvironment.isHeadless()

- defaultPage

```java
public abstract
PageFormat
defaultPage​(
PageFormat
page)
```

Clones the

PageFormat

argument and alters the
clone to describe a default page size and orientation.

**Parameters:** page

- the

PageFormat

to be cloned and altered
**Returns:** clone of

page

, altered to describe a default

PageFormat

.

- defaultPage

```java
public
PageFormat
defaultPage()
```

Creates a new

PageFormat

instance and
sets it to a default size and orientation.

**Returns:** a

PageFormat

set to a default size and
orientation.

- getPageFormat

```java
public
PageFormat
getPageFormat​(
PrintRequestAttributeSet
attributes)
```

Calculates a

PageFormat

with values consistent with those
supported by the current

PrintService

for this job
(ie the value returned by

getPrintService()

) and media,
printable area and orientation contained in

attributes

.

Calling this method does not update the job.
It is useful for clients that have a set of attributes obtained from

printDialog(PrintRequestAttributeSet attributes)

and need a PageFormat to print a Pageable object.

**Parameters:** attributes

- a set of printing attributes, for example obtained
from calling printDialog. If

attributes

is null a default
PageFormat is returned.
**Returns:** a

PageFormat

whose settings conform with
those of the current service and the specified attributes.
**Since:** 1.6

- validatePage

```java
public abstract
PageFormat
validatePage​(
PageFormat
page)
```

Returns the clone of

page

with its settings
adjusted to be compatible with the current printer of this

PrinterJob

. For example, the returned

PageFormat

could have its imageable area
adjusted to fit within the physical area of the paper that
is used by the current printer.

**Parameters:** page

- the

PageFormat

that is cloned and
whose settings are changed to be compatible with
the current printer
**Returns:** a

PageFormat

that is cloned from

page

and whose settings are changed
to conform with this

PrinterJob

.

- print

```java
public abstract void print()
throws
PrinterException
```

Prints a set of pages.

**Throws:** PrinterException

- an error in the print system
caused the job to be aborted.
**See Also:** Book

,

Pageable

,

Printable

- print

```java
public void print​(
PrintRequestAttributeSet
attributes)
throws
PrinterException
```

Prints a set of pages using the settings in the attribute
set. The default implementation ignores the attribute set.

Note that some attributes may be set directly on the PrinterJob
by equivalent method calls, (for example), copies:

setCopies(int)

, job name:

setJobName(String)

and specifying media size and orientation though the

PageFormat

object.

If a supported attribute-value is specified in this attribute set,
it will take precedence over the API settings for this print()
operation only.
The following behaviour is specified for PageFormat:
If a client uses the Printable interface, then the

attributes

parameter to this method is examined
for attributes which specify media (by size), orientation, and
imageable area, and those are used to construct a new PageFormat
which is passed to the Printable object's print() method.
See

Printable

for an explanation of the required
behaviour of a Printable to ensure optimal printing via PrinterJob.
For clients of the Pageable interface, the PageFormat will always
be as supplied by that interface, on a per page basis.

These behaviours allow an application to directly pass the
user settings returned from

printDialog(PrintRequestAttributeSet attributes

to
this print() method.

**Parameters:** attributes

- a set of attributes for the job
**Throws:** PrinterException

- an error in the print system
caused the job to be aborted.
**Since:** 1.4
**See Also:** Book

,

Pageable

,

Printable

- setCopies

```java
public abstract void setCopies​(int copies)
```

Sets the number of copies to be printed.

**Parameters:** copies

- the number of copies to be printed
**See Also:** getCopies()

- getCopies

```java
public abstract int getCopies()
```

Gets the number of copies to be printed.

**Returns:** the number of copies to be printed.
**See Also:** setCopies(int)

- getUserName

```java
public abstract
String
getUserName()
```

Gets the name of the printing user.

**Returns:** the name of the printing user
**Throws:** SecurityException

- if a security manager exists and
PropertyPermission - user.name is not given in the policy file

- setJobName

```java
public abstract void setJobName​(
String
jobName)
```

Sets the name of the document to be printed.
The document name can not be

null

.

**Parameters:** jobName

- the name of the document to be printed
**See Also:** getJobName()

- getJobName

```java
public abstract
String
getJobName()
```

Gets the name of the document to be printed.

**Returns:** the name of the document to be printed.
**See Also:** setJobName(java.lang.String)

- cancel

```java
public abstract void cancel()
```

Cancels a print job that is in progress. If

print

has been called but has not
returned then this method signals
that the job should be cancelled at the next
chance. If there is no print job in progress then
this call does nothing.

- isCancelled

```java
public abstract boolean isCancelled()
```

Returns

true

if a print job is
in progress, but is going to be cancelled
at the next opportunity; otherwise returns

false

.

**Returns:** true

if the job in progress
is going to be cancelled;

false

otherwise.

Constructor Detail

- PrinterJob

```java
public PrinterJob()
```

A

PrinterJob

object should be created using the
static

getPrinterJob

method.

---

#### Constructor Detail

PrinterJob

```java
public PrinterJob()
```

A

PrinterJob

object should be created using the
static

getPrinterJob

method.

---

#### PrinterJob

public PrinterJob()

A

PrinterJob

object should be created using the
static

getPrinterJob

method.

Method Detail

- getPrinterJob

```java
public static
PrinterJob
getPrinterJob()
```

Creates and returns a

PrinterJob

which is initially
associated with the default printer.
If no printers are available on the system, a PrinterJob will still
be returned from this method, but

getPrintService()

will return

null

, and calling

print

with this

PrinterJob

might
generate an exception. Applications that need to determine if
there are suitable printers before creating a

PrinterJob

should ensure that the array returned from

lookupPrintServices

is not empty.

**Returns:** a new

PrinterJob

.
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkPrintJobAccess()

method disallows this thread from creating a print job request

- lookupPrintServices

```java
public static
PrintService
[] lookupPrintServices()
```

A convenience method which looks up 2D print services.
Services returned from this method may be installed on

PrinterJob

s which support print services.
Calling this method is equivalent to calling

PrintServiceLookup.lookupPrintServices()

and specifying a Pageable DocFlavor.

**Returns:** a possibly empty array of 2D print services.
**Since:** 1.4

- lookupStreamPrintServices

```java
public static
StreamPrintServiceFactory
[] lookupStreamPrintServices​(
String
mimeType)
```

A convenience method which locates factories for stream print
services which can image 2D graphics.
Sample usage :

```java
FileOutputStream outstream;
StreamPrintService psPrinter;
String psMimeType = "application/postscript";
PrinterJob pj = PrinterJob.getPrinterJob();

StreamPrintServiceFactory[] factories =
PrinterJob.lookupStreamPrintServices(psMimeType);
if (factories.length > 0) {
try {
outstream = new File("out.ps");
psPrinter = factories[0].getPrintService(outstream);
// psPrinter can now be set as the service on a PrinterJob
pj.setPrintService(psPrinter)
} catch (Exception e) {
e.printStackTrace();
}
}
```

Services returned from this method may be installed on

PrinterJob

instances which support print services.
Calling this method is equivalent to calling

StreamPrintServiceFactory.lookupStreamPrintServiceFactories()

and specifying a Pageable DocFlavor.

**Parameters:** mimeType

- the required output format, or null to mean any format.
**Returns:** a possibly empty array of 2D stream print service factories.
**Since:** 1.4

- getPrintService

```java
public
PrintService
getPrintService()
```

Returns the service (printer) for this printer job.
Implementations of this class which do not support print services
may return null. null will also be returned if no printers are
available.

**Returns:** the service for this printer job.
**Since:** 1.4
**See Also:** setPrintService(PrintService)

,

getPrinterJob()

- setPrintService

```java
public void setPrintService​(
PrintService
service)
throws
PrinterException
```

Associate this PrinterJob with a new PrintService.
This method is overridden by subclasses which support
specifying a Print Service.

Throws

PrinterException

if the specified service
cannot support the

Pageable

and

Printable

interfaces necessary to support 2D printing.

**Parameters:** service

- a print service that supports 2D printing
**Throws:** PrinterException

- if the specified service does not support
2D printing, or this PrinterJob class does not support
setting a 2D print service, or the specified service is
otherwise not a valid print service.
**Since:** 1.4
**See Also:** getPrintService()

- setPrintable

```java
public abstract void setPrintable​(
Printable
painter)
```

Calls

painter

to render the pages. The pages in the
document to be printed by this

PrinterJob

are rendered by the

Printable

object,

painter

. The

PageFormat

for each page
is the default page format.

**Parameters:** painter

- the

Printable

that renders each page of
the document.

- setPrintable

```java
public abstract void setPrintable​(
Printable
painter,

PageFormat
format)
```

Calls

painter

to render the pages in the specified

format

. The pages in the document to be printed by
this

PrinterJob

are rendered by the

Printable

object,

painter

. The

PageFormat

of each page is

format

.

**Parameters:** painter

- the

Printable

called to render
each page of the document
**Parameters:** format

- the size and orientation of each page to
be printed

- setPageable

```java
public abstract void setPageable​(
Pageable
document)
throws
NullPointerException
```

Queries

document

for the number of pages and
the

PageFormat

and

Printable

for each
page held in the

Pageable

instance,

document

.

**Parameters:** document

- the pages to be printed. It can not be

null

.
**Throws:** NullPointerException

- the

Pageable

passed in
was

null

.
**See Also:** PageFormat

,

Printable

- printDialog

```java
public abstract boolean printDialog()
throws
HeadlessException
```

Presents a dialog to the user for changing the properties of
the print job.
This method will display a native dialog if a native print
service is selected, and user choice of printers will be restricted
to these native print services.
To present the cross platform print dialog for all services,
including native ones instead use

printDialog(PrintRequestAttributeSet)

.

PrinterJob implementations which can use PrintService's will update
the PrintService for this PrinterJob to reflect the new service
selected by the user.

**Returns:** true

if the user does not cancel the dialog;

false

otherwise.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

- printDialog

```java
public boolean printDialog​(
PrintRequestAttributeSet
attributes)
throws
HeadlessException
```

A convenience method which displays a cross-platform print dialog
for all services which are capable of printing 2D graphics using the

Pageable

interface. The selected printer when the
dialog is initially displayed will reflect the print service currently
attached to this print job.
If the user changes the print service, the PrinterJob will be
updated to reflect this, unless the user cancels the dialog.
As well as allowing the user to select the destination printer,
the user can also select values of various print request attributes.

The attributes parameter on input will reflect the applications
required initial selections in the user dialog. Attributes not
specified display using the default for the service. On return it
will reflect the user's choices. Selections may be updated by
the implementation to be consistent with the supported values
for the currently selected print service.

As the user scrolls to a new print service selection, the values
copied are based on the settings for the previous service, together
with any user changes. The values are not based on the original
settings supplied by the client.

With the exception of selected printer, the PrinterJob state is
not updated to reflect the user's changes.
For the selections to affect a printer job, the attributes must
be specified in the call to the

print(PrintRequestAttributeSet)

method. If using
the Pageable interface, clients which intend to use media selected
by the user must create a PageFormat derived from the user's
selections.
If the user cancels the dialog, the attributes will not reflect
any changes made by the user.

**Parameters:** attributes

- on input is application supplied attributes,
on output the contents are updated to reflect user choices.
This parameter may not be null.
**Returns:** true

if the user does not cancel the dialog;

false

otherwise.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**Throws:** NullPointerException

- if

attributes

parameter
is null.
**Since:** 1.4
**See Also:** GraphicsEnvironment.isHeadless()

- pageDialog

```java
public abstract
PageFormat
pageDialog​(
PageFormat
page)
throws
HeadlessException
```

Displays a dialog that allows modification of a

PageFormat

instance.
The

page

argument is used to initialize controls
in the page setup dialog.
If the user cancels the dialog then this method returns the
original

page

object unmodified.
If the user okays the dialog then this method returns a new

PageFormat

object with the indicated changes.
In either case, the original

page

object is
not modified.

**Parameters:** page

- the default

PageFormat

presented to the
user for modification
**Returns:** the original

page

object if the dialog
is cancelled; a new

PageFormat

object
containing the format indicated by the user if the
dialog is acknowledged.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**Since:** 1.2
**See Also:** GraphicsEnvironment.isHeadless()

- pageDialog

```java
public
PageFormat
pageDialog​(
PrintRequestAttributeSet
attributes)
throws
HeadlessException
```

A convenience method which displays a cross-platform page setup dialog.
The choices available will reflect the print service currently
set on this PrinterJob.

The attributes parameter on input will reflect the client's
required initial selections in the user dialog. Attributes which are
not specified display using the default for the service. On return it
will reflect the user's choices. Selections may be updated by
the implementation to be consistent with the supported values
for the currently selected print service.

The return value will be a PageFormat equivalent to the
selections in the PrintRequestAttributeSet.
If the user cancels the dialog, the attributes will not reflect
any changes made by the user, and the return value will be null.

**Parameters:** attributes

- on input is application supplied attributes,
on output the contents are updated to reflect user choices.
This parameter may not be null.
**Returns:** a page format if the user does not cancel the dialog;

null

otherwise.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**Throws:** NullPointerException

- if

attributes

parameter
is null.
**Since:** 1.4
**See Also:** GraphicsEnvironment.isHeadless()

- defaultPage

```java
public abstract
PageFormat
defaultPage​(
PageFormat
page)
```

Clones the

PageFormat

argument and alters the
clone to describe a default page size and orientation.

**Parameters:** page

- the

PageFormat

to be cloned and altered
**Returns:** clone of

page

, altered to describe a default

PageFormat

.

- defaultPage

```java
public
PageFormat
defaultPage()
```

Creates a new

PageFormat

instance and
sets it to a default size and orientation.

**Returns:** a

PageFormat

set to a default size and
orientation.

- getPageFormat

```java
public
PageFormat
getPageFormat​(
PrintRequestAttributeSet
attributes)
```

Calculates a

PageFormat

with values consistent with those
supported by the current

PrintService

for this job
(ie the value returned by

getPrintService()

) and media,
printable area and orientation contained in

attributes

.

Calling this method does not update the job.
It is useful for clients that have a set of attributes obtained from

printDialog(PrintRequestAttributeSet attributes)

and need a PageFormat to print a Pageable object.

**Parameters:** attributes

- a set of printing attributes, for example obtained
from calling printDialog. If

attributes

is null a default
PageFormat is returned.
**Returns:** a

PageFormat

whose settings conform with
those of the current service and the specified attributes.
**Since:** 1.6

- validatePage

```java
public abstract
PageFormat
validatePage​(
PageFormat
page)
```

Returns the clone of

page

with its settings
adjusted to be compatible with the current printer of this

PrinterJob

. For example, the returned

PageFormat

could have its imageable area
adjusted to fit within the physical area of the paper that
is used by the current printer.

**Parameters:** page

- the

PageFormat

that is cloned and
whose settings are changed to be compatible with
the current printer
**Returns:** a

PageFormat

that is cloned from

page

and whose settings are changed
to conform with this

PrinterJob

.

- print

```java
public abstract void print()
throws
PrinterException
```

Prints a set of pages.

**Throws:** PrinterException

- an error in the print system
caused the job to be aborted.
**See Also:** Book

,

Pageable

,

Printable

- print

```java
public void print​(
PrintRequestAttributeSet
attributes)
throws
PrinterException
```

Prints a set of pages using the settings in the attribute
set. The default implementation ignores the attribute set.

Note that some attributes may be set directly on the PrinterJob
by equivalent method calls, (for example), copies:

setCopies(int)

, job name:

setJobName(String)

and specifying media size and orientation though the

PageFormat

object.

If a supported attribute-value is specified in this attribute set,
it will take precedence over the API settings for this print()
operation only.
The following behaviour is specified for PageFormat:
If a client uses the Printable interface, then the

attributes

parameter to this method is examined
for attributes which specify media (by size), orientation, and
imageable area, and those are used to construct a new PageFormat
which is passed to the Printable object's print() method.
See

Printable

for an explanation of the required
behaviour of a Printable to ensure optimal printing via PrinterJob.
For clients of the Pageable interface, the PageFormat will always
be as supplied by that interface, on a per page basis.

These behaviours allow an application to directly pass the
user settings returned from

printDialog(PrintRequestAttributeSet attributes

to
this print() method.

**Parameters:** attributes

- a set of attributes for the job
**Throws:** PrinterException

- an error in the print system
caused the job to be aborted.
**Since:** 1.4
**See Also:** Book

,

Pageable

,

Printable

- setCopies

```java
public abstract void setCopies​(int copies)
```

Sets the number of copies to be printed.

**Parameters:** copies

- the number of copies to be printed
**See Also:** getCopies()

- getCopies

```java
public abstract int getCopies()
```

Gets the number of copies to be printed.

**Returns:** the number of copies to be printed.
**See Also:** setCopies(int)

- getUserName

```java
public abstract
String
getUserName()
```

Gets the name of the printing user.

**Returns:** the name of the printing user
**Throws:** SecurityException

- if a security manager exists and
PropertyPermission - user.name is not given in the policy file

- setJobName

```java
public abstract void setJobName​(
String
jobName)
```

Sets the name of the document to be printed.
The document name can not be

null

.

**Parameters:** jobName

- the name of the document to be printed
**See Also:** getJobName()

- getJobName

```java
public abstract
String
getJobName()
```

Gets the name of the document to be printed.

**Returns:** the name of the document to be printed.
**See Also:** setJobName(java.lang.String)

- cancel

```java
public abstract void cancel()
```

Cancels a print job that is in progress. If

print

has been called but has not
returned then this method signals
that the job should be cancelled at the next
chance. If there is no print job in progress then
this call does nothing.

- isCancelled

```java
public abstract boolean isCancelled()
```

Returns

true

if a print job is
in progress, but is going to be cancelled
at the next opportunity; otherwise returns

false

.

**Returns:** true

if the job in progress
is going to be cancelled;

false

otherwise.

---

#### Method Detail

getPrinterJob

```java
public static
PrinterJob
getPrinterJob()
```

Creates and returns a

PrinterJob

which is initially
associated with the default printer.
If no printers are available on the system, a PrinterJob will still
be returned from this method, but

getPrintService()

will return

null

, and calling

print

with this

PrinterJob

might
generate an exception. Applications that need to determine if
there are suitable printers before creating a

PrinterJob

should ensure that the array returned from

lookupPrintServices

is not empty.

**Returns:** a new

PrinterJob

.
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkPrintJobAccess()

method disallows this thread from creating a print job request

---

#### getPrinterJob

public static

PrinterJob

getPrinterJob()

Creates and returns a

PrinterJob

which is initially
associated with the default printer.
If no printers are available on the system, a PrinterJob will still
be returned from this method, but

getPrintService()

will return

null

, and calling

print

with this

PrinterJob

might
generate an exception. Applications that need to determine if
there are suitable printers before creating a

PrinterJob

should ensure that the array returned from

lookupPrintServices

is not empty.

lookupPrintServices

```java
public static
PrintService
[] lookupPrintServices()
```

A convenience method which looks up 2D print services.
Services returned from this method may be installed on

PrinterJob

s which support print services.
Calling this method is equivalent to calling

PrintServiceLookup.lookupPrintServices()

and specifying a Pageable DocFlavor.

**Returns:** a possibly empty array of 2D print services.
**Since:** 1.4

---

#### lookupPrintServices

public static

PrintService

[] lookupPrintServices()

A convenience method which looks up 2D print services.
Services returned from this method may be installed on

PrinterJob

s which support print services.
Calling this method is equivalent to calling

PrintServiceLookup.lookupPrintServices()

and specifying a Pageable DocFlavor.

lookupStreamPrintServices

```java
public static
StreamPrintServiceFactory
[] lookupStreamPrintServices​(
String
mimeType)
```

A convenience method which locates factories for stream print
services which can image 2D graphics.
Sample usage :

```java
FileOutputStream outstream;
StreamPrintService psPrinter;
String psMimeType = "application/postscript";
PrinterJob pj = PrinterJob.getPrinterJob();

StreamPrintServiceFactory[] factories =
PrinterJob.lookupStreamPrintServices(psMimeType);
if (factories.length > 0) {
try {
outstream = new File("out.ps");
psPrinter = factories[0].getPrintService(outstream);
// psPrinter can now be set as the service on a PrinterJob
pj.setPrintService(psPrinter)
} catch (Exception e) {
e.printStackTrace();
}
}
```

Services returned from this method may be installed on

PrinterJob

instances which support print services.
Calling this method is equivalent to calling

StreamPrintServiceFactory.lookupStreamPrintServiceFactories()

and specifying a Pageable DocFlavor.

**Parameters:** mimeType

- the required output format, or null to mean any format.
**Returns:** a possibly empty array of 2D stream print service factories.
**Since:** 1.4

---

#### lookupStreamPrintServices

public static

StreamPrintServiceFactory

[] lookupStreamPrintServices​(

String

mimeType)

A convenience method which locates factories for stream print
services which can image 2D graphics.
Sample usage :

```java
FileOutputStream outstream;
StreamPrintService psPrinter;
String psMimeType = "application/postscript";
PrinterJob pj = PrinterJob.getPrinterJob();

StreamPrintServiceFactory[] factories =
PrinterJob.lookupStreamPrintServices(psMimeType);
if (factories.length > 0) {
try {
outstream = new File("out.ps");
psPrinter = factories[0].getPrintService(outstream);
// psPrinter can now be set as the service on a PrinterJob
pj.setPrintService(psPrinter)
} catch (Exception e) {
e.printStackTrace();
}
}
```

Services returned from this method may be installed on

PrinterJob

instances which support print services.
Calling this method is equivalent to calling

StreamPrintServiceFactory.lookupStreamPrintServiceFactories()

and specifying a Pageable DocFlavor.

FileOutputStream outstream;
StreamPrintService psPrinter;
String psMimeType = "application/postscript";
PrinterJob pj = PrinterJob.getPrinterJob();

StreamPrintServiceFactory[] factories =
PrinterJob.lookupStreamPrintServices(psMimeType);
if (factories.length > 0) {
try {
outstream = new File("out.ps");
psPrinter = factories[0].getPrintService(outstream);
// psPrinter can now be set as the service on a PrinterJob
pj.setPrintService(psPrinter)
} catch (Exception e) {
e.printStackTrace();
}
}

getPrintService

```java
public
PrintService
getPrintService()
```

Returns the service (printer) for this printer job.
Implementations of this class which do not support print services
may return null. null will also be returned if no printers are
available.

**Returns:** the service for this printer job.
**Since:** 1.4
**See Also:** setPrintService(PrintService)

,

getPrinterJob()

---

#### getPrintService

public

PrintService

getPrintService()

Returns the service (printer) for this printer job.
Implementations of this class which do not support print services
may return null. null will also be returned if no printers are
available.

setPrintService

```java
public void setPrintService​(
PrintService
service)
throws
PrinterException
```

Associate this PrinterJob with a new PrintService.
This method is overridden by subclasses which support
specifying a Print Service.

Throws

PrinterException

if the specified service
cannot support the

Pageable

and

Printable

interfaces necessary to support 2D printing.

**Parameters:** service

- a print service that supports 2D printing
**Throws:** PrinterException

- if the specified service does not support
2D printing, or this PrinterJob class does not support
setting a 2D print service, or the specified service is
otherwise not a valid print service.
**Since:** 1.4
**See Also:** getPrintService()

---

#### setPrintService

public void setPrintService​(

PrintService

service)
throws

PrinterException

Associate this PrinterJob with a new PrintService.
This method is overridden by subclasses which support
specifying a Print Service.

Throws

PrinterException

if the specified service
cannot support the

Pageable

and

Printable

interfaces necessary to support 2D printing.

setPrintable

```java
public abstract void setPrintable​(
Printable
painter)
```

Calls

painter

to render the pages. The pages in the
document to be printed by this

PrinterJob

are rendered by the

Printable

object,

painter

. The

PageFormat

for each page
is the default page format.

**Parameters:** painter

- the

Printable

that renders each page of
the document.

---

#### setPrintable

public abstract void setPrintable​(

Printable

painter)

Calls

painter

to render the pages. The pages in the
document to be printed by this

PrinterJob

are rendered by the

Printable

object,

painter

. The

PageFormat

for each page
is the default page format.

setPrintable

```java
public abstract void setPrintable​(
Printable
painter,

PageFormat
format)
```

Calls

painter

to render the pages in the specified

format

. The pages in the document to be printed by
this

PrinterJob

are rendered by the

Printable

object,

painter

. The

PageFormat

of each page is

format

.

**Parameters:** painter

- the

Printable

called to render
each page of the document
**Parameters:** format

- the size and orientation of each page to
be printed

---

#### setPrintable

public abstract void setPrintable​(

Printable

painter,

PageFormat

format)

Calls

painter

to render the pages in the specified

format

. The pages in the document to be printed by
this

PrinterJob

are rendered by the

Printable

object,

painter

. The

PageFormat

of each page is

format

.

setPageable

```java
public abstract void setPageable​(
Pageable
document)
throws
NullPointerException
```

Queries

document

for the number of pages and
the

PageFormat

and

Printable

for each
page held in the

Pageable

instance,

document

.

**Parameters:** document

- the pages to be printed. It can not be

null

.
**Throws:** NullPointerException

- the

Pageable

passed in
was

null

.
**See Also:** PageFormat

,

Printable

---

#### setPageable

public abstract void setPageable​(

Pageable

document)
throws

NullPointerException

Queries

document

for the number of pages and
the

PageFormat

and

Printable

for each
page held in the

Pageable

instance,

document

.

printDialog

```java
public abstract boolean printDialog()
throws
HeadlessException
```

Presents a dialog to the user for changing the properties of
the print job.
This method will display a native dialog if a native print
service is selected, and user choice of printers will be restricted
to these native print services.
To present the cross platform print dialog for all services,
including native ones instead use

printDialog(PrintRequestAttributeSet)

.

PrinterJob implementations which can use PrintService's will update
the PrintService for this PrinterJob to reflect the new service
selected by the user.

**Returns:** true

if the user does not cancel the dialog;

false

otherwise.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

---

#### printDialog

public abstract boolean printDialog()
throws

HeadlessException

Presents a dialog to the user for changing the properties of
the print job.
This method will display a native dialog if a native print
service is selected, and user choice of printers will be restricted
to these native print services.
To present the cross platform print dialog for all services,
including native ones instead use

printDialog(PrintRequestAttributeSet)

.

PrinterJob implementations which can use PrintService's will update
the PrintService for this PrinterJob to reflect the new service
selected by the user.

PrinterJob implementations which can use PrintService's will update
the PrintService for this PrinterJob to reflect the new service
selected by the user.

printDialog

```java
public boolean printDialog​(
PrintRequestAttributeSet
attributes)
throws
HeadlessException
```

A convenience method which displays a cross-platform print dialog
for all services which are capable of printing 2D graphics using the

Pageable

interface. The selected printer when the
dialog is initially displayed will reflect the print service currently
attached to this print job.
If the user changes the print service, the PrinterJob will be
updated to reflect this, unless the user cancels the dialog.
As well as allowing the user to select the destination printer,
the user can also select values of various print request attributes.

The attributes parameter on input will reflect the applications
required initial selections in the user dialog. Attributes not
specified display using the default for the service. On return it
will reflect the user's choices. Selections may be updated by
the implementation to be consistent with the supported values
for the currently selected print service.

As the user scrolls to a new print service selection, the values
copied are based on the settings for the previous service, together
with any user changes. The values are not based on the original
settings supplied by the client.

With the exception of selected printer, the PrinterJob state is
not updated to reflect the user's changes.
For the selections to affect a printer job, the attributes must
be specified in the call to the

print(PrintRequestAttributeSet)

method. If using
the Pageable interface, clients which intend to use media selected
by the user must create a PageFormat derived from the user's
selections.
If the user cancels the dialog, the attributes will not reflect
any changes made by the user.

**Parameters:** attributes

- on input is application supplied attributes,
on output the contents are updated to reflect user choices.
This parameter may not be null.
**Returns:** true

if the user does not cancel the dialog;

false

otherwise.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**Throws:** NullPointerException

- if

attributes

parameter
is null.
**Since:** 1.4
**See Also:** GraphicsEnvironment.isHeadless()

---

#### printDialog

public boolean printDialog​(

PrintRequestAttributeSet

attributes)
throws

HeadlessException

A convenience method which displays a cross-platform print dialog
for all services which are capable of printing 2D graphics using the

Pageable

interface. The selected printer when the
dialog is initially displayed will reflect the print service currently
attached to this print job.
If the user changes the print service, the PrinterJob will be
updated to reflect this, unless the user cancels the dialog.
As well as allowing the user to select the destination printer,
the user can also select values of various print request attributes.

The attributes parameter on input will reflect the applications
required initial selections in the user dialog. Attributes not
specified display using the default for the service. On return it
will reflect the user's choices. Selections may be updated by
the implementation to be consistent with the supported values
for the currently selected print service.

As the user scrolls to a new print service selection, the values
copied are based on the settings for the previous service, together
with any user changes. The values are not based on the original
settings supplied by the client.

With the exception of selected printer, the PrinterJob state is
not updated to reflect the user's changes.
For the selections to affect a printer job, the attributes must
be specified in the call to the

print(PrintRequestAttributeSet)

method. If using
the Pageable interface, clients which intend to use media selected
by the user must create a PageFormat derived from the user's
selections.
If the user cancels the dialog, the attributes will not reflect
any changes made by the user.

The attributes parameter on input will reflect the applications
required initial selections in the user dialog. Attributes not
specified display using the default for the service. On return it
will reflect the user's choices. Selections may be updated by
the implementation to be consistent with the supported values
for the currently selected print service.

As the user scrolls to a new print service selection, the values
copied are based on the settings for the previous service, together
with any user changes. The values are not based on the original
settings supplied by the client.

With the exception of selected printer, the PrinterJob state is
not updated to reflect the user's changes.
For the selections to affect a printer job, the attributes must
be specified in the call to the

print(PrintRequestAttributeSet)

method. If using
the Pageable interface, clients which intend to use media selected
by the user must create a PageFormat derived from the user's
selections.
If the user cancels the dialog, the attributes will not reflect
any changes made by the user.

As the user scrolls to a new print service selection, the values
copied are based on the settings for the previous service, together
with any user changes. The values are not based on the original
settings supplied by the client.

With the exception of selected printer, the PrinterJob state is
not updated to reflect the user's changes.
For the selections to affect a printer job, the attributes must
be specified in the call to the

print(PrintRequestAttributeSet)

method. If using
the Pageable interface, clients which intend to use media selected
by the user must create a PageFormat derived from the user's
selections.
If the user cancels the dialog, the attributes will not reflect
any changes made by the user.

With the exception of selected printer, the PrinterJob state is
not updated to reflect the user's changes.
For the selections to affect a printer job, the attributes must
be specified in the call to the

print(PrintRequestAttributeSet)

method. If using
the Pageable interface, clients which intend to use media selected
by the user must create a PageFormat derived from the user's
selections.
If the user cancels the dialog, the attributes will not reflect
any changes made by the user.

pageDialog

```java
public abstract
PageFormat
pageDialog​(
PageFormat
page)
throws
HeadlessException
```

Displays a dialog that allows modification of a

PageFormat

instance.
The

page

argument is used to initialize controls
in the page setup dialog.
If the user cancels the dialog then this method returns the
original

page

object unmodified.
If the user okays the dialog then this method returns a new

PageFormat

object with the indicated changes.
In either case, the original

page

object is
not modified.

**Parameters:** page

- the default

PageFormat

presented to the
user for modification
**Returns:** the original

page

object if the dialog
is cancelled; a new

PageFormat

object
containing the format indicated by the user if the
dialog is acknowledged.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**Since:** 1.2
**See Also:** GraphicsEnvironment.isHeadless()

---

#### pageDialog

public abstract

PageFormat

pageDialog​(

PageFormat

page)
throws

HeadlessException

Displays a dialog that allows modification of a

PageFormat

instance.
The

page

argument is used to initialize controls
in the page setup dialog.
If the user cancels the dialog then this method returns the
original

page

object unmodified.
If the user okays the dialog then this method returns a new

PageFormat

object with the indicated changes.
In either case, the original

page

object is
not modified.

pageDialog

```java
public
PageFormat
pageDialog​(
PrintRequestAttributeSet
attributes)
throws
HeadlessException
```

A convenience method which displays a cross-platform page setup dialog.
The choices available will reflect the print service currently
set on this PrinterJob.

The attributes parameter on input will reflect the client's
required initial selections in the user dialog. Attributes which are
not specified display using the default for the service. On return it
will reflect the user's choices. Selections may be updated by
the implementation to be consistent with the supported values
for the currently selected print service.

The return value will be a PageFormat equivalent to the
selections in the PrintRequestAttributeSet.
If the user cancels the dialog, the attributes will not reflect
any changes made by the user, and the return value will be null.

**Parameters:** attributes

- on input is application supplied attributes,
on output the contents are updated to reflect user choices.
This parameter may not be null.
**Returns:** a page format if the user does not cancel the dialog;

null

otherwise.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**Throws:** NullPointerException

- if

attributes

parameter
is null.
**Since:** 1.4
**See Also:** GraphicsEnvironment.isHeadless()

---

#### pageDialog

public

PageFormat

pageDialog​(

PrintRequestAttributeSet

attributes)
throws

HeadlessException

A convenience method which displays a cross-platform page setup dialog.
The choices available will reflect the print service currently
set on this PrinterJob.

The attributes parameter on input will reflect the client's
required initial selections in the user dialog. Attributes which are
not specified display using the default for the service. On return it
will reflect the user's choices. Selections may be updated by
the implementation to be consistent with the supported values
for the currently selected print service.

The return value will be a PageFormat equivalent to the
selections in the PrintRequestAttributeSet.
If the user cancels the dialog, the attributes will not reflect
any changes made by the user, and the return value will be null.

The attributes parameter on input will reflect the client's
required initial selections in the user dialog. Attributes which are
not specified display using the default for the service. On return it
will reflect the user's choices. Selections may be updated by
the implementation to be consistent with the supported values
for the currently selected print service.

The return value will be a PageFormat equivalent to the
selections in the PrintRequestAttributeSet.
If the user cancels the dialog, the attributes will not reflect
any changes made by the user, and the return value will be null.

The return value will be a PageFormat equivalent to the
selections in the PrintRequestAttributeSet.
If the user cancels the dialog, the attributes will not reflect
any changes made by the user, and the return value will be null.

defaultPage

```java
public abstract
PageFormat
defaultPage​(
PageFormat
page)
```

Clones the

PageFormat

argument and alters the
clone to describe a default page size and orientation.

**Parameters:** page

- the

PageFormat

to be cloned and altered
**Returns:** clone of

page

, altered to describe a default

PageFormat

.

---

#### defaultPage

public abstract

PageFormat

defaultPage​(

PageFormat

page)

Clones the

PageFormat

argument and alters the
clone to describe a default page size and orientation.

defaultPage

```java
public
PageFormat
defaultPage()
```

Creates a new

PageFormat

instance and
sets it to a default size and orientation.

**Returns:** a

PageFormat

set to a default size and
orientation.

---

#### defaultPage

public

PageFormat

defaultPage()

Creates a new

PageFormat

instance and
sets it to a default size and orientation.

getPageFormat

```java
public
PageFormat
getPageFormat​(
PrintRequestAttributeSet
attributes)
```

Calculates a

PageFormat

with values consistent with those
supported by the current

PrintService

for this job
(ie the value returned by

getPrintService()

) and media,
printable area and orientation contained in

attributes

.

Calling this method does not update the job.
It is useful for clients that have a set of attributes obtained from

printDialog(PrintRequestAttributeSet attributes)

and need a PageFormat to print a Pageable object.

**Parameters:** attributes

- a set of printing attributes, for example obtained
from calling printDialog. If

attributes

is null a default
PageFormat is returned.
**Returns:** a

PageFormat

whose settings conform with
those of the current service and the specified attributes.
**Since:** 1.6

---

#### getPageFormat

public

PageFormat

getPageFormat​(

PrintRequestAttributeSet

attributes)

Calculates a

PageFormat

with values consistent with those
supported by the current

PrintService

for this job
(ie the value returned by

getPrintService()

) and media,
printable area and orientation contained in

attributes

.

Calling this method does not update the job.
It is useful for clients that have a set of attributes obtained from

printDialog(PrintRequestAttributeSet attributes)

and need a PageFormat to print a Pageable object.

Calling this method does not update the job.
It is useful for clients that have a set of attributes obtained from

printDialog(PrintRequestAttributeSet attributes)

and need a PageFormat to print a Pageable object.

validatePage

```java
public abstract
PageFormat
validatePage​(
PageFormat
page)
```

Returns the clone of

page

with its settings
adjusted to be compatible with the current printer of this

PrinterJob

. For example, the returned

PageFormat

could have its imageable area
adjusted to fit within the physical area of the paper that
is used by the current printer.

**Parameters:** page

- the

PageFormat

that is cloned and
whose settings are changed to be compatible with
the current printer
**Returns:** a

PageFormat

that is cloned from

page

and whose settings are changed
to conform with this

PrinterJob

.

---

#### validatePage

public abstract

PageFormat

validatePage​(

PageFormat

page)

Returns the clone of

page

with its settings
adjusted to be compatible with the current printer of this

PrinterJob

. For example, the returned

PageFormat

could have its imageable area
adjusted to fit within the physical area of the paper that
is used by the current printer.

print

```java
public abstract void print()
throws
PrinterException
```

Prints a set of pages.

**Throws:** PrinterException

- an error in the print system
caused the job to be aborted.
**See Also:** Book

,

Pageable

,

Printable

---

#### print

public abstract void print()
throws

PrinterException

Prints a set of pages.

print

```java
public void print​(
PrintRequestAttributeSet
attributes)
throws
PrinterException
```

Prints a set of pages using the settings in the attribute
set. The default implementation ignores the attribute set.

Note that some attributes may be set directly on the PrinterJob
by equivalent method calls, (for example), copies:

setCopies(int)

, job name:

setJobName(String)

and specifying media size and orientation though the

PageFormat

object.

If a supported attribute-value is specified in this attribute set,
it will take precedence over the API settings for this print()
operation only.
The following behaviour is specified for PageFormat:
If a client uses the Printable interface, then the

attributes

parameter to this method is examined
for attributes which specify media (by size), orientation, and
imageable area, and those are used to construct a new PageFormat
which is passed to the Printable object's print() method.
See

Printable

for an explanation of the required
behaviour of a Printable to ensure optimal printing via PrinterJob.
For clients of the Pageable interface, the PageFormat will always
be as supplied by that interface, on a per page basis.

These behaviours allow an application to directly pass the
user settings returned from

printDialog(PrintRequestAttributeSet attributes

to
this print() method.

**Parameters:** attributes

- a set of attributes for the job
**Throws:** PrinterException

- an error in the print system
caused the job to be aborted.
**Since:** 1.4
**See Also:** Book

,

Pageable

,

Printable

---

#### print

public void print​(

PrintRequestAttributeSet

attributes)
throws

PrinterException

Prints a set of pages using the settings in the attribute
set. The default implementation ignores the attribute set.

Note that some attributes may be set directly on the PrinterJob
by equivalent method calls, (for example), copies:

setCopies(int)

, job name:

setJobName(String)

and specifying media size and orientation though the

PageFormat

object.

If a supported attribute-value is specified in this attribute set,
it will take precedence over the API settings for this print()
operation only.
The following behaviour is specified for PageFormat:
If a client uses the Printable interface, then the

attributes

parameter to this method is examined
for attributes which specify media (by size), orientation, and
imageable area, and those are used to construct a new PageFormat
which is passed to the Printable object's print() method.
See

Printable

for an explanation of the required
behaviour of a Printable to ensure optimal printing via PrinterJob.
For clients of the Pageable interface, the PageFormat will always
be as supplied by that interface, on a per page basis.

These behaviours allow an application to directly pass the
user settings returned from

printDialog(PrintRequestAttributeSet attributes

to
this print() method.

Note that some attributes may be set directly on the PrinterJob
by equivalent method calls, (for example), copies:

setCopies(int)

, job name:

setJobName(String)

and specifying media size and orientation though the

PageFormat

object.

If a supported attribute-value is specified in this attribute set,
it will take precedence over the API settings for this print()
operation only.
The following behaviour is specified for PageFormat:
If a client uses the Printable interface, then the

attributes

parameter to this method is examined
for attributes which specify media (by size), orientation, and
imageable area, and those are used to construct a new PageFormat
which is passed to the Printable object's print() method.
See

Printable

for an explanation of the required
behaviour of a Printable to ensure optimal printing via PrinterJob.
For clients of the Pageable interface, the PageFormat will always
be as supplied by that interface, on a per page basis.

These behaviours allow an application to directly pass the
user settings returned from

printDialog(PrintRequestAttributeSet attributes

to
this print() method.

If a supported attribute-value is specified in this attribute set,
it will take precedence over the API settings for this print()
operation only.
The following behaviour is specified for PageFormat:
If a client uses the Printable interface, then the

attributes

parameter to this method is examined
for attributes which specify media (by size), orientation, and
imageable area, and those are used to construct a new PageFormat
which is passed to the Printable object's print() method.
See

Printable

for an explanation of the required
behaviour of a Printable to ensure optimal printing via PrinterJob.
For clients of the Pageable interface, the PageFormat will always
be as supplied by that interface, on a per page basis.

These behaviours allow an application to directly pass the
user settings returned from

printDialog(PrintRequestAttributeSet attributes

to
this print() method.

These behaviours allow an application to directly pass the
user settings returned from

printDialog(PrintRequestAttributeSet attributes

to
this print() method.

setCopies

```java
public abstract void setCopies​(int copies)
```

Sets the number of copies to be printed.

**Parameters:** copies

- the number of copies to be printed
**See Also:** getCopies()

---

#### setCopies

public abstract void setCopies​(int copies)

Sets the number of copies to be printed.

getCopies

```java
public abstract int getCopies()
```

Gets the number of copies to be printed.

**Returns:** the number of copies to be printed.
**See Also:** setCopies(int)

---

#### getCopies

public abstract int getCopies()

Gets the number of copies to be printed.

getUserName

```java
public abstract
String
getUserName()
```

Gets the name of the printing user.

**Returns:** the name of the printing user
**Throws:** SecurityException

- if a security manager exists and
PropertyPermission - user.name is not given in the policy file

---

#### getUserName

public abstract

String

getUserName()

Gets the name of the printing user.

setJobName

```java
public abstract void setJobName​(
String
jobName)
```

Sets the name of the document to be printed.
The document name can not be

null

.

**Parameters:** jobName

- the name of the document to be printed
**See Also:** getJobName()

---

#### setJobName

public abstract void setJobName​(

String

jobName)

Sets the name of the document to be printed.
The document name can not be

null

.

getJobName

```java
public abstract
String
getJobName()
```

Gets the name of the document to be printed.

**Returns:** the name of the document to be printed.
**See Also:** setJobName(java.lang.String)

---

#### getJobName

public abstract

String

getJobName()

Gets the name of the document to be printed.

cancel

```java
public abstract void cancel()
```

Cancels a print job that is in progress. If

print

has been called but has not
returned then this method signals
that the job should be cancelled at the next
chance. If there is no print job in progress then
this call does nothing.

---

#### cancel

public abstract void cancel()

Cancels a print job that is in progress. If

print

has been called but has not
returned then this method signals
that the job should be cancelled at the next
chance. If there is no print job in progress then
this call does nothing.

isCancelled

```java
public abstract boolean isCancelled()
```

Returns

true

if a print job is
in progress, but is going to be cancelled
at the next opportunity; otherwise returns

false

.

**Returns:** true

if the job in progress
is going to be cancelled;

false

otherwise.

---

#### isCancelled

public abstract boolean isCancelled()

Returns

true

if a print job is
in progress, but is going to be cancelled
at the next opportunity; otherwise returns

false

.

---

