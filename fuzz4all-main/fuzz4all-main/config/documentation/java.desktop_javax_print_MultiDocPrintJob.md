# Interface MultiDocPrintJob

**Source:** `java.desktop\javax\print\MultiDocPrintJob.html`

### Class Description

```java
public interface
MultiDocPrintJob

extends
DocPrintJob
```

Obtained from a

MultiDocPrintService

, a

MultiDocPrintJob

can
print a specified collection of documents as a single print job with a set of
job attributes.

**All Superinterfaces:** DocPrintJob

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void print​(
MultiDoc
multiDoc,

PrintRequestAttributeSet
attributes)
throws
PrintException

Print a

MultiDoc

with the specified job attributes. This method
should only be called once for a given print job. Calling it again will
not result in a new job being spooled to the printer. The service
implementation will define policy for service interruption and recovery.
Application clients which want to monitor the success or failure should
register a

PrintJobListener

.

**Parameters:**
- multiDoc

- the documents to be printed. ALL must be a flavor
supported by the PrintJob & PrintService.
- attributes

- the job attributes to be applied to this print job. If
this parameter is

null

then the default attributes are
used.

**Throws:**
- PrintException

- the exception additionally may implement an
interfaces which more precisely describes the cause of the
exception

- FlavorException

. If the document has a flavor not
supported by this print job.

AttributeException

. If one or more of the
attributes are not valid for this print job.

---

### Additional Sections

#### Interface MultiDocPrintJob

**All Superinterfaces:** DocPrintJob

```java
public interface
MultiDocPrintJob

extends
DocPrintJob
```

Obtained from a

MultiDocPrintService

, a

MultiDocPrintJob

can
print a specified collection of documents as a single print job with a set of
job attributes.

public interface

MultiDocPrintJob

extends

DocPrintJob

Obtained from a

MultiDocPrintService

, a

MultiDocPrintJob

can
print a specified collection of documents as a single print job with a set of
job attributes.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

print

​(

MultiDoc

multiDoc,

PrintRequestAttributeSet

attributes)

Print a

MultiDoc

with the specified job attributes.

- Methods declared in interface javax.print.

DocPrintJob

addPrintJobAttributeListener

,

addPrintJobListener

,

getAttributes

,

getPrintService

,

print

,

removePrintJobAttributeListener

,

removePrintJobListener

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

print

​(

MultiDoc

multiDoc,

PrintRequestAttributeSet

attributes)

Print a

MultiDoc

with the specified job attributes.

- Methods declared in interface javax.print.

DocPrintJob

addPrintJobAttributeListener

,

addPrintJobListener

,

getAttributes

,

getPrintService

,

print

,

removePrintJobAttributeListener

,

removePrintJobListener

---

#### Method Summary

Print a

MultiDoc

with the specified job attributes.

Methods declared in interface javax.print.

DocPrintJob

addPrintJobAttributeListener

,

addPrintJobListener

,

getAttributes

,

getPrintService

,

print

,

removePrintJobAttributeListener

,

removePrintJobListener

---

#### Methods declared in interface javax.print. DocPrintJob

============ METHOD DETAIL ==========

- Method Detail

- print

```java
void print​(
MultiDoc
multiDoc,

PrintRequestAttributeSet
attributes)
throws
PrintException
```

Print a

MultiDoc

with the specified job attributes. This method
should only be called once for a given print job. Calling it again will
not result in a new job being spooled to the printer. The service
implementation will define policy for service interruption and recovery.
Application clients which want to monitor the success or failure should
register a

PrintJobListener

.

**Parameters:** multiDoc

- the documents to be printed. ALL must be a flavor
supported by the PrintJob & PrintService.
**Parameters:** attributes

- the job attributes to be applied to this print job. If
this parameter is

null

then the default attributes are
used.
**Throws:** PrintException

- the exception additionally may implement an
interfaces which more precisely describes the cause of the
exception

- FlavorException

. If the document has a flavor not
supported by this print job.

AttributeException

. If one or more of the
attributes are not valid for this print job.

Method Detail

- print

```java
void print​(
MultiDoc
multiDoc,

PrintRequestAttributeSet
attributes)
throws
PrintException
```

Print a

MultiDoc

with the specified job attributes. This method
should only be called once for a given print job. Calling it again will
not result in a new job being spooled to the printer. The service
implementation will define policy for service interruption and recovery.
Application clients which want to monitor the success or failure should
register a

PrintJobListener

.

**Parameters:** multiDoc

- the documents to be printed. ALL must be a flavor
supported by the PrintJob & PrintService.
**Parameters:** attributes

- the job attributes to be applied to this print job. If
this parameter is

null

then the default attributes are
used.
**Throws:** PrintException

- the exception additionally may implement an
interfaces which more precisely describes the cause of the
exception

- FlavorException

. If the document has a flavor not
supported by this print job.

AttributeException

. If one or more of the
attributes are not valid for this print job.

---

#### Method Detail

print

```java
void print​(
MultiDoc
multiDoc,

PrintRequestAttributeSet
attributes)
throws
PrintException
```

Print a

MultiDoc

with the specified job attributes. This method
should only be called once for a given print job. Calling it again will
not result in a new job being spooled to the printer. The service
implementation will define policy for service interruption and recovery.
Application clients which want to monitor the success or failure should
register a

PrintJobListener

.

**Parameters:** multiDoc

- the documents to be printed. ALL must be a flavor
supported by the PrintJob & PrintService.
**Parameters:** attributes

- the job attributes to be applied to this print job. If
this parameter is

null

then the default attributes are
used.
**Throws:** PrintException

- the exception additionally may implement an
interfaces which more precisely describes the cause of the
exception

- FlavorException

. If the document has a flavor not
supported by this print job.

AttributeException

. If one or more of the
attributes are not valid for this print job.

---

#### print

void print​(

MultiDoc

multiDoc,

PrintRequestAttributeSet

attributes)
throws

PrintException

Print a

MultiDoc

with the specified job attributes. This method
should only be called once for a given print job. Calling it again will
not result in a new job being spooled to the printer. The service
implementation will define policy for service interruption and recovery.
Application clients which want to monitor the success or failure should
register a

PrintJobListener

.

FlavorException

. If the document has a flavor not
supported by this print job.

AttributeException

. If one or more of the
attributes are not valid for this print job.

---

