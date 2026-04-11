# Class JobStateReason

**Source:** `java.desktop\javax\print\attribute\standard\JobStateReason.html`

### Class Description

```java
public class
JobStateReason

extends
EnumSyntax

implements
Attribute
```

Class

JobStateReason

is a printing attribute class, an enumeration,
that provides additional information about the job's current state, i.e.,
information that augments the value of the job's

JobState

attribute. Class

JobStateReason

defines standard job state reason
values. A Print Service implementation only needs to report those job state
reasons which are appropriate for the particular implementation; it does not
have to report every defined job state reason.

Instances of

JobStateReason

do not appear in a Print Job's attribute
set directly. Rather, a

JobStateReasons

attribute
appears in the Print Job's attribute set. The

JobStateReasons

attribute contains zero, one, or more
than one

JobStateReason

objects which pertain to the Print Job's
status. The printer adds a JobStateReason object to the Print Job's

JobStateReasons

attribute when the corresponding
condition becomes true of the Print Job, and the printer removes the

JobStateReason

object again when the corresponding condition becomes
false, regardless of whether the Print Job's overall

JobState

also changed.

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

---

### Field Details

#### public static final
JobStateReason
JOB_INCOMING

The printer has created the Print Job, but the printer has not finished
accessing or accepting all the print data yet.

---

#### public static final
JobStateReason
JOB_DATA_INSUFFICIENT

The printer has created the Print Job, but the printer is expecting
additional print data before it can move the job into the

PROCESSING

state. If a printer starts processing before it has
received all data, the printer removes the

JOB_DATA_INSUFFICIENT

reason, but the

JOB_INCOMING

reason remains. If a printer starts
processing after it has received all data, the printer removes the

JOB_DATA_INSUFFICIENT

and

JOB_INCOMING

reasons at the
same time.

---

#### public static final
JobStateReason
DOCUMENT_ACCESS_ERROR

The printer could not access one or more documents passed by reference
(i.e., the print data representation object is a

URL

). This
reason is intended to cover any file access problem,including file does
not exist and access denied because of an access control problem. Whether
the printer aborts the job and moves the job to the

ABORTED

job
state or prints all documents that are accessible and moves the job to
the

COMPLETED

job state and adds the

COMPLETED_WITH_ERRORS

reason to the job's

JobStateReasons

attribute depends on
implementation and/or site policy. This value should be supported if the
printer supports doc flavors with

URL

print data representation
objects.

---

#### public static final
JobStateReason
SUBMISSION_INTERRUPTED

The job was not completely submitted for some unforeseen reason.
Possibilities include (1) the printer has crashed before the job was
fully submitted by the client, (2) the printer or the document transfer
method has crashed in some non-recoverable way before the document data
was entirely transferred to the printer, (3) the client crashed before
the job was fully submitted.

---

#### public static final
JobStateReason
JOB_OUTGOING

The printer is transmitting the job to the output device.

---

#### public static final
JobStateReason
JOB_HOLD_UNTIL_SPECIFIED

The value of the job's

JobHoldUntil

attribute was
specified with a date-time that is still in the future. The job must not
be a candidate for processing until this reason is removed and there are
no other reasons to hold the job. This value should be supported if the

JobHoldUntil

job template attribute is supported.

---

#### public static final
JobStateReason
RESOURCES_ARE_NOT_READY

At least one of the resources needed by the job, such as media, fonts,
resource objects, etc., is not ready on any of the physical printers for
which the job is a candidate. This condition may be detected when the job
is accepted, or subsequently while the job is pending or processing,
depending on implementation. The job may remain in its current state or
be moved to the

PENDING_HELD

state, depending on implementation
and/or job scheduling policy.

---

#### public static final
JobStateReason
PRINTER_STOPPED_PARTLY

The value of the printer's

PrinterStateReasons

attribute contains a

PrinterStateReason

value of

STOPPED_PARTLY

.

---

#### public static final
JobStateReason
PRINTER_STOPPED

The value of the printer's

PrinterState

attribute ia

STOPPED

.

---

#### public static final
JobStateReason
JOB_INTERPRETING

The job is in the

PROCESSING

state, but more specifically, the
printer ia interpreting the document data.

---

#### public static final
JobStateReason
JOB_QUEUED

The job is in the

PROCESSING

state, but more specifically, the
printer has queued the document data.

---

#### public static final
JobStateReason
JOB_TRANSFORMING

The job is in the

PROCESSING

state, but more specifically, the
printer is interpreting document data and producing another electronic
representation.

---

#### public static final
JobStateReason
JOB_QUEUED_FOR_MARKER

The job is in the

PENDING_HELD

,

PENDING

, or

PROCESSING

state, but more specifically, the printer has
completed enough processing of the document to be able to start marking
and the job is waiting for the marker. Systems that require human
intervention to release jobs put the job into the

PENDING_HELD

job state. Systems that automatically select a job to use the marker put
the job into the

PENDING

job state or keep the job in the

PROCESSING

job state while waiting for the marker, depending on
implementation. All implementations put the job into (or back into) the

PROCESSING

state when marking does begin.

---

#### public static final
JobStateReason
JOB_PRINTING

The output device is marking media. This value is useful for printers
which spend a great deal of time processing (1) when no marking is
happening and then want to show that marking is now happening or (2) when
the job is in the process of being canceled or aborted while the job
remains in the

PROCESSING

state, but the marking has not yet
stopped so that impression or sheet counts are still increasing for the
job.

---

#### public static final
JobStateReason
JOB_CANCELED_BY_USER

The job was canceled by the owner of the job, i.e., by a user whose
authenticated identity is the same as the value of the originating user
that created the Print Job, or by some other authorized end-user, such as
a member of the job owner's security group. This value should be
supported.

---

#### public static final
JobStateReason
JOB_CANCELED_BY_OPERATOR

The job was canceled by the operator, i.e., by a user who has been
authenticated as having operator privileges (whether local or remote). If
the security policy is to allow anyone to cancel anyone's job, then this
value may be used when the job is canceled by someone other than the
owner of the job. For such a security policy, in effect, everyone is an
operator as far as canceling jobs is concerned. This value should be
supported if the implementation permits canceling by someone other than
the owner of the job.

---

#### public static final
JobStateReason
JOB_CANCELED_AT_DEVICE

The job was canceled by an unidentified local user, i.e., a user at a
console at the device. This value should be supported if the
implementation supports canceling jobs at the console.

---

#### public static final
JobStateReason
ABORTED_BY_SYSTEM

The job was aborted by the system. Either the job (1) is in the process
of being aborted, (2) has been aborted by the system and placed in the

ABORTED

state, or (3) has been aborted by the system and placed
in the

PENDING_HELD

state, so that a user or operator can
manually try the job again. This value should be supported.

---

#### public static final
JobStateReason
UNSUPPORTED_COMPRESSION

The job was aborted by the system because the printer determined while
attempting to decompress the document's data that the compression is
actually not among those supported by the printer. This value must be
supported, since

Compression

is a required doc
description attribute.

---

#### public static final
JobStateReason
COMPRESSION_ERROR

The job was aborted by the system because the printer encountered an
error in the document data while decompressing it. If the printer posts
this reason, the document data has already passed any tests that would
have led to the

UNSUPPORTED_COMPRESSION

job state reason.

---

#### public static final
JobStateReason
UNSUPPORTED_DOCUMENT_FORMAT

The job was aborted by the system because the document data's document
format (doc flavor) is not among those supported by the printer. If the
client specifies a doc flavor with a MIME type of

"application/octet-stream"

, the printer may abort the job if the
printer cannot determine the document data's actual format through
auto-sensing (even if the printer supports the document format if
specified explicitly). This value must be supported, since a doc flavor
is required to be specified for each doc.

---

#### public static final
JobStateReason
DOCUMENT_FORMAT_ERROR

The job was aborted by the system because the printer encountered an
error in the document data while processing it. If the printer posts this
reason, the document data has already passed any tests that would have
led to the

UNSUPPORTED_DOCUMENT_FORMAT

job state reason.

---

#### public static final
JobStateReason
PROCESSING_TO_STOP_POINT

The requester has canceled the job or the printer has aborted the job,
but the printer is still performing some actions on the job until a
specified stop point occurs or job termination/cleanup is completed.

If the implementation requires some measurable time to cancel the job in
the

PROCESSING

or

PROCESSING_STOPPED

job states, the
printer must use this reason to indicate that the printer is still
performing some actions on the job while the job remains in the

PROCESSING

or

PROCESSING_STOPPED

state. After all the
job's job description attributes have stopped incrementing, the printer
moves the job from the PROCESSING state to the

CANCELED

or

ABORTED

job states.

---

#### public static final
JobStateReason
SERVICE_OFF_LINE

The printer is off-line and accepting no jobs. All

PENDING

jobs
are put into the

PENDING_HELD

state. This situation could be true
if the service's or document transform's input is impaired or broken.

---

#### public static final
JobStateReason
JOB_COMPLETED_SUCCESSFULLY

The job completed successfully. This value should be supported.

---

#### public static final
JobStateReason
JOB_COMPLETED_WITH_WARNINGS

The job completed with warnings. This value should be supported if the
implementation detects warnings.

---

#### public static final
JobStateReason
JOB_COMPLETED_WITH_ERRORS

The job completed with errors (and possibly warnings too). This value
should be supported if the implementation detects errors.

---

#### public static final
JobStateReason
JOB_RESTARTABLE

This job is retained and is currently able to be restarted. If

JOB_RESTARTABLE

is contained in the job's

JobStateReasons

attribute, then the printer must
accept a request to restart that job. This value should be supported if
restarting jobs is supported.

[The capability for restarting jobs is
not in the Java Print Service API at present.]

---

#### public static final
JobStateReason
QUEUED_IN_DEVICE

The job has been forwarded to a device or print system that is unable to
send back status. The printer sets the job's

JobState

attribute to

COMPLETED

and adds the

QUEUED_IN_DEVICE

reason to the job's

JobStateReasons

attribute to
indicate that the printer has no additional information about the job and
never will have any better information.

---

### Constructor Details

#### protected JobStateReason​(int value)

Construct a new job state reason enumeration value with the given integer
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

JobStateReason

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

JobStateReason

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

JobStateReason

and any vendor-defined subclasses, the
category is class

JobStateReason

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

JobStateReason

and any vendor-defined subclasses, the
category name is

"job-state-reason"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class JobStateReason

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.JobStateReason

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.JobStateReason

javax.print.attribute.standard.JobStateReason

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

```java
public class
JobStateReason

extends
EnumSyntax

implements
Attribute
```

Class

JobStateReason

is a printing attribute class, an enumeration,
that provides additional information about the job's current state, i.e.,
information that augments the value of the job's

JobState

attribute. Class

JobStateReason

defines standard job state reason
values. A Print Service implementation only needs to report those job state
reasons which are appropriate for the particular implementation; it does not
have to report every defined job state reason.

Instances of

JobStateReason

do not appear in a Print Job's attribute
set directly. Rather, a

JobStateReasons

attribute
appears in the Print Job's attribute set. The

JobStateReasons

attribute contains zero, one, or more
than one

JobStateReason

objects which pertain to the Print Job's
status. The printer adds a JobStateReason object to the Print Job's

JobStateReasons

attribute when the corresponding
condition becomes true of the Print Job, and the printer removes the

JobStateReason

object again when the corresponding condition becomes
false, regardless of whether the Print Job's overall

JobState

also changed.

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

public class

JobStateReason

extends

EnumSyntax

implements

Attribute

Class

JobStateReason

is a printing attribute class, an enumeration,
that provides additional information about the job's current state, i.e.,
information that augments the value of the job's

JobState

attribute. Class

JobStateReason

defines standard job state reason
values. A Print Service implementation only needs to report those job state
reasons which are appropriate for the particular implementation; it does not
have to report every defined job state reason.

Instances of

JobStateReason

do not appear in a Print Job's attribute
set directly. Rather, a

JobStateReasons

attribute
appears in the Print Job's attribute set. The

JobStateReasons

attribute contains zero, one, or more
than one

JobStateReason

objects which pertain to the Print Job's
status. The printer adds a JobStateReason object to the Print Job's

JobStateReasons

attribute when the corresponding
condition becomes true of the Print Job, and the printer removes the

JobStateReason

object again when the corresponding condition becomes
false, regardless of whether the Print Job's overall

JobState

also changed.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

Instances of

JobStateReason

do not appear in a Print Job's attribute
set directly. Rather, a

JobStateReasons

attribute
appears in the Print Job's attribute set. The

JobStateReasons

attribute contains zero, one, or more
than one

JobStateReason

objects which pertain to the Print Job's
status. The printer adds a JobStateReason object to the Print Job's

JobStateReasons

attribute when the corresponding
condition becomes true of the Print Job, and the printer removes the

JobStateReason

object again when the corresponding condition becomes
false, regardless of whether the Print Job's overall

JobState

also changed.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

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

JobStateReason

ABORTED_BY_SYSTEM

The job was aborted by the system.

static

JobStateReason

COMPRESSION_ERROR

The job was aborted by the system because the printer encountered an
error in the document data while decompressing it.

static

JobStateReason

DOCUMENT_ACCESS_ERROR

The printer could not access one or more documents passed by reference
(i.e., the print data representation object is a

URL

).

static

JobStateReason

DOCUMENT_FORMAT_ERROR

The job was aborted by the system because the printer encountered an
error in the document data while processing it.

static

JobStateReason

JOB_CANCELED_AT_DEVICE

The job was canceled by an unidentified local user, i.e., a user at a
console at the device.

static

JobStateReason

JOB_CANCELED_BY_OPERATOR

The job was canceled by the operator, i.e., by a user who has been
authenticated as having operator privileges (whether local or remote).

static

JobStateReason

JOB_CANCELED_BY_USER

The job was canceled by the owner of the job, i.e., by a user whose
authenticated identity is the same as the value of the originating user
that created the Print Job, or by some other authorized end-user, such as
a member of the job owner's security group.

static

JobStateReason

JOB_COMPLETED_SUCCESSFULLY

The job completed successfully.

static

JobStateReason

JOB_COMPLETED_WITH_ERRORS

The job completed with errors (and possibly warnings too).

static

JobStateReason

JOB_COMPLETED_WITH_WARNINGS

The job completed with warnings.

static

JobStateReason

JOB_DATA_INSUFFICIENT

The printer has created the Print Job, but the printer is expecting
additional print data before it can move the job into the

PROCESSING

state.

static

JobStateReason

JOB_HOLD_UNTIL_SPECIFIED

The value of the job's

JobHoldUntil

attribute was
specified with a date-time that is still in the future.

static

JobStateReason

JOB_INCOMING

The printer has created the Print Job, but the printer has not finished
accessing or accepting all the print data yet.

static

JobStateReason

JOB_INTERPRETING

The job is in the

PROCESSING

state, but more specifically, the
printer ia interpreting the document data.

static

JobStateReason

JOB_OUTGOING

The printer is transmitting the job to the output device.

static

JobStateReason

JOB_PRINTING

The output device is marking media.

static

JobStateReason

JOB_QUEUED

The job is in the

PROCESSING

state, but more specifically, the
printer has queued the document data.

static

JobStateReason

JOB_QUEUED_FOR_MARKER

The job is in the

PENDING_HELD

,

PENDING

, or

PROCESSING

state, but more specifically, the printer has
completed enough processing of the document to be able to start marking
and the job is waiting for the marker.

static

JobStateReason

JOB_RESTARTABLE

This job is retained and is currently able to be restarted.

static

JobStateReason

JOB_TRANSFORMING

The job is in the

PROCESSING

state, but more specifically, the
printer is interpreting document data and producing another electronic
representation.

static

JobStateReason

PRINTER_STOPPED

The value of the printer's

PrinterState

attribute ia

STOPPED

.

static

JobStateReason

PRINTER_STOPPED_PARTLY

The value of the printer's

PrinterStateReasons

attribute contains a

PrinterStateReason

value of

STOPPED_PARTLY

.

static

JobStateReason

PROCESSING_TO_STOP_POINT

The requester has canceled the job or the printer has aborted the job,
but the printer is still performing some actions on the job until a
specified stop point occurs or job termination/cleanup is completed.

static

JobStateReason

QUEUED_IN_DEVICE

The job has been forwarded to a device or print system that is unable to
send back status.

static

JobStateReason

RESOURCES_ARE_NOT_READY

At least one of the resources needed by the job, such as media, fonts,
resource objects, etc., is not ready on any of the physical printers for
which the job is a candidate.

static

JobStateReason

SERVICE_OFF_LINE

The printer is off-line and accepting no jobs.

static

JobStateReason

SUBMISSION_INTERRUPTED

The job was not completely submitted for some unforeseen reason.

static

JobStateReason

UNSUPPORTED_COMPRESSION

The job was aborted by the system because the printer determined while
attempting to decompress the document's data that the compression is
actually not among those supported by the printer.

static

JobStateReason

UNSUPPORTED_DOCUMENT_FORMAT

The job was aborted by the system because the document data's document
format (doc flavor) is not among those supported by the printer.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

JobStateReason

​(int value)

Construct a new job state reason enumeration value with the given integer
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

JobStateReason

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

JobStateReason

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

JobStateReason

ABORTED_BY_SYSTEM

The job was aborted by the system.

static

JobStateReason

COMPRESSION_ERROR

The job was aborted by the system because the printer encountered an
error in the document data while decompressing it.

static

JobStateReason

DOCUMENT_ACCESS_ERROR

The printer could not access one or more documents passed by reference
(i.e., the print data representation object is a

URL

).

static

JobStateReason

DOCUMENT_FORMAT_ERROR

The job was aborted by the system because the printer encountered an
error in the document data while processing it.

static

JobStateReason

JOB_CANCELED_AT_DEVICE

The job was canceled by an unidentified local user, i.e., a user at a
console at the device.

static

JobStateReason

JOB_CANCELED_BY_OPERATOR

The job was canceled by the operator, i.e., by a user who has been
authenticated as having operator privileges (whether local or remote).

static

JobStateReason

JOB_CANCELED_BY_USER

The job was canceled by the owner of the job, i.e., by a user whose
authenticated identity is the same as the value of the originating user
that created the Print Job, or by some other authorized end-user, such as
a member of the job owner's security group.

static

JobStateReason

JOB_COMPLETED_SUCCESSFULLY

The job completed successfully.

static

JobStateReason

JOB_COMPLETED_WITH_ERRORS

The job completed with errors (and possibly warnings too).

static

JobStateReason

JOB_COMPLETED_WITH_WARNINGS

The job completed with warnings.

static

JobStateReason

JOB_DATA_INSUFFICIENT

The printer has created the Print Job, but the printer is expecting
additional print data before it can move the job into the

PROCESSING

state.

static

JobStateReason

JOB_HOLD_UNTIL_SPECIFIED

The value of the job's

JobHoldUntil

attribute was
specified with a date-time that is still in the future.

static

JobStateReason

JOB_INCOMING

The printer has created the Print Job, but the printer has not finished
accessing or accepting all the print data yet.

static

JobStateReason

JOB_INTERPRETING

The job is in the

PROCESSING

state, but more specifically, the
printer ia interpreting the document data.

static

JobStateReason

JOB_OUTGOING

The printer is transmitting the job to the output device.

static

JobStateReason

JOB_PRINTING

The output device is marking media.

static

JobStateReason

JOB_QUEUED

The job is in the

PROCESSING

state, but more specifically, the
printer has queued the document data.

static

JobStateReason

JOB_QUEUED_FOR_MARKER

The job is in the

PENDING_HELD

,

PENDING

, or

PROCESSING

state, but more specifically, the printer has
completed enough processing of the document to be able to start marking
and the job is waiting for the marker.

static

JobStateReason

JOB_RESTARTABLE

This job is retained and is currently able to be restarted.

static

JobStateReason

JOB_TRANSFORMING

The job is in the

PROCESSING

state, but more specifically, the
printer is interpreting document data and producing another electronic
representation.

static

JobStateReason

PRINTER_STOPPED

The value of the printer's

PrinterState

attribute ia

STOPPED

.

static

JobStateReason

PRINTER_STOPPED_PARTLY

The value of the printer's

PrinterStateReasons

attribute contains a

PrinterStateReason

value of

STOPPED_PARTLY

.

static

JobStateReason

PROCESSING_TO_STOP_POINT

The requester has canceled the job or the printer has aborted the job,
but the printer is still performing some actions on the job until a
specified stop point occurs or job termination/cleanup is completed.

static

JobStateReason

QUEUED_IN_DEVICE

The job has been forwarded to a device or print system that is unable to
send back status.

static

JobStateReason

RESOURCES_ARE_NOT_READY

At least one of the resources needed by the job, such as media, fonts,
resource objects, etc., is not ready on any of the physical printers for
which the job is a candidate.

static

JobStateReason

SERVICE_OFF_LINE

The printer is off-line and accepting no jobs.

static

JobStateReason

SUBMISSION_INTERRUPTED

The job was not completely submitted for some unforeseen reason.

static

JobStateReason

UNSUPPORTED_COMPRESSION

The job was aborted by the system because the printer determined while
attempting to decompress the document's data that the compression is
actually not among those supported by the printer.

static

JobStateReason

UNSUPPORTED_DOCUMENT_FORMAT

The job was aborted by the system because the document data's document
format (doc flavor) is not among those supported by the printer.

---

#### Field Summary

The job was aborted by the system.

The job was aborted by the system because the printer encountered an
error in the document data while decompressing it.

The printer could not access one or more documents passed by reference
(i.e., the print data representation object is a

URL

).

The job was aborted by the system because the printer encountered an
error in the document data while processing it.

The job was canceled by an unidentified local user, i.e., a user at a
console at the device.

The job was canceled by the operator, i.e., by a user who has been
authenticated as having operator privileges (whether local or remote).

The job was canceled by the owner of the job, i.e., by a user whose
authenticated identity is the same as the value of the originating user
that created the Print Job, or by some other authorized end-user, such as
a member of the job owner's security group.

The job completed successfully.

The job completed with errors (and possibly warnings too).

The job completed with warnings.

The printer has created the Print Job, but the printer is expecting
additional print data before it can move the job into the

PROCESSING

state.

The value of the job's

JobHoldUntil

attribute was
specified with a date-time that is still in the future.

The printer has created the Print Job, but the printer has not finished
accessing or accepting all the print data yet.

The job is in the

PROCESSING

state, but more specifically, the
printer ia interpreting the document data.

The printer is transmitting the job to the output device.

The output device is marking media.

The job is in the

PROCESSING

state, but more specifically, the
printer has queued the document data.

The job is in the

PENDING_HELD

,

PENDING

, or

PROCESSING

state, but more specifically, the printer has
completed enough processing of the document to be able to start marking
and the job is waiting for the marker.

This job is retained and is currently able to be restarted.

The job is in the

PROCESSING

state, but more specifically, the
printer is interpreting document data and producing another electronic
representation.

The value of the printer's

PrinterState

attribute ia

STOPPED

.

The value of the printer's

PrinterStateReasons

attribute contains a

PrinterStateReason

value of

STOPPED_PARTLY

.

The requester has canceled the job or the printer has aborted the job,
but the printer is still performing some actions on the job until a
specified stop point occurs or job termination/cleanup is completed.

The job has been forwarded to a device or print system that is unable to
send back status.

At least one of the resources needed by the job, such as media, fonts,
resource objects, etc., is not ready on any of the physical printers for
which the job is a candidate.

The printer is off-line and accepting no jobs.

The job was not completely submitted for some unforeseen reason.

The job was aborted by the system because the printer determined while
attempting to decompress the document's data that the compression is
actually not among those supported by the printer.

The job was aborted by the system because the document data's document
format (doc flavor) is not among those supported by the printer.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

JobStateReason

​(int value)

Construct a new job state reason enumeration value with the given integer
value.

---

#### Constructor Summary

Construct a new job state reason enumeration value with the given integer
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

JobStateReason

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

JobStateReason

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

JobStateReason

.

Get the name of the category of which this attribute value is an
instance.

Returns the string table for class

JobStateReason

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

- JOB_INCOMING

```java
public static final
JobStateReason
JOB_INCOMING
```

The printer has created the Print Job, but the printer has not finished
accessing or accepting all the print data yet.

- JOB_DATA_INSUFFICIENT

```java
public static final
JobStateReason
JOB_DATA_INSUFFICIENT
```

The printer has created the Print Job, but the printer is expecting
additional print data before it can move the job into the

PROCESSING

state. If a printer starts processing before it has
received all data, the printer removes the

JOB_DATA_INSUFFICIENT

reason, but the

JOB_INCOMING

reason remains. If a printer starts
processing after it has received all data, the printer removes the

JOB_DATA_INSUFFICIENT

and

JOB_INCOMING

reasons at the
same time.

- DOCUMENT_ACCESS_ERROR

```java
public static final
JobStateReason
DOCUMENT_ACCESS_ERROR
```

The printer could not access one or more documents passed by reference
(i.e., the print data representation object is a

URL

). This
reason is intended to cover any file access problem,including file does
not exist and access denied because of an access control problem. Whether
the printer aborts the job and moves the job to the

ABORTED

job
state or prints all documents that are accessible and moves the job to
the

COMPLETED

job state and adds the

COMPLETED_WITH_ERRORS

reason to the job's

JobStateReasons

attribute depends on
implementation and/or site policy. This value should be supported if the
printer supports doc flavors with

URL

print data representation
objects.

- SUBMISSION_INTERRUPTED

```java
public static final
JobStateReason
SUBMISSION_INTERRUPTED
```

The job was not completely submitted for some unforeseen reason.
Possibilities include (1) the printer has crashed before the job was
fully submitted by the client, (2) the printer or the document transfer
method has crashed in some non-recoverable way before the document data
was entirely transferred to the printer, (3) the client crashed before
the job was fully submitted.

- JOB_OUTGOING

```java
public static final
JobStateReason
JOB_OUTGOING
```

The printer is transmitting the job to the output device.

- JOB_HOLD_UNTIL_SPECIFIED

```java
public static final
JobStateReason
JOB_HOLD_UNTIL_SPECIFIED
```

The value of the job's

JobHoldUntil

attribute was
specified with a date-time that is still in the future. The job must not
be a candidate for processing until this reason is removed and there are
no other reasons to hold the job. This value should be supported if the

JobHoldUntil

job template attribute is supported.

- RESOURCES_ARE_NOT_READY

```java
public static final
JobStateReason
RESOURCES_ARE_NOT_READY
```

At least one of the resources needed by the job, such as media, fonts,
resource objects, etc., is not ready on any of the physical printers for
which the job is a candidate. This condition may be detected when the job
is accepted, or subsequently while the job is pending or processing,
depending on implementation. The job may remain in its current state or
be moved to the

PENDING_HELD

state, depending on implementation
and/or job scheduling policy.

- PRINTER_STOPPED_PARTLY

```java
public static final
JobStateReason
PRINTER_STOPPED_PARTLY
```

The value of the printer's

PrinterStateReasons

attribute contains a

PrinterStateReason

value of

STOPPED_PARTLY

.

- PRINTER_STOPPED

```java
public static final
JobStateReason
PRINTER_STOPPED
```

The value of the printer's

PrinterState

attribute ia

STOPPED

.

- JOB_INTERPRETING

```java
public static final
JobStateReason
JOB_INTERPRETING
```

The job is in the

PROCESSING

state, but more specifically, the
printer ia interpreting the document data.

- JOB_QUEUED

```java
public static final
JobStateReason
JOB_QUEUED
```

The job is in the

PROCESSING

state, but more specifically, the
printer has queued the document data.

- JOB_TRANSFORMING

```java
public static final
JobStateReason
JOB_TRANSFORMING
```

The job is in the

PROCESSING

state, but more specifically, the
printer is interpreting document data and producing another electronic
representation.

- JOB_QUEUED_FOR_MARKER

```java
public static final
JobStateReason
JOB_QUEUED_FOR_MARKER
```

The job is in the

PENDING_HELD

,

PENDING

, or

PROCESSING

state, but more specifically, the printer has
completed enough processing of the document to be able to start marking
and the job is waiting for the marker. Systems that require human
intervention to release jobs put the job into the

PENDING_HELD

job state. Systems that automatically select a job to use the marker put
the job into the

PENDING

job state or keep the job in the

PROCESSING

job state while waiting for the marker, depending on
implementation. All implementations put the job into (or back into) the

PROCESSING

state when marking does begin.

- JOB_PRINTING

```java
public static final
JobStateReason
JOB_PRINTING
```

The output device is marking media. This value is useful for printers
which spend a great deal of time processing (1) when no marking is
happening and then want to show that marking is now happening or (2) when
the job is in the process of being canceled or aborted while the job
remains in the

PROCESSING

state, but the marking has not yet
stopped so that impression or sheet counts are still increasing for the
job.

- JOB_CANCELED_BY_USER

```java
public static final
JobStateReason
JOB_CANCELED_BY_USER
```

The job was canceled by the owner of the job, i.e., by a user whose
authenticated identity is the same as the value of the originating user
that created the Print Job, or by some other authorized end-user, such as
a member of the job owner's security group. This value should be
supported.

- JOB_CANCELED_BY_OPERATOR

```java
public static final
JobStateReason
JOB_CANCELED_BY_OPERATOR
```

The job was canceled by the operator, i.e., by a user who has been
authenticated as having operator privileges (whether local or remote). If
the security policy is to allow anyone to cancel anyone's job, then this
value may be used when the job is canceled by someone other than the
owner of the job. For such a security policy, in effect, everyone is an
operator as far as canceling jobs is concerned. This value should be
supported if the implementation permits canceling by someone other than
the owner of the job.

- JOB_CANCELED_AT_DEVICE

```java
public static final
JobStateReason
JOB_CANCELED_AT_DEVICE
```

The job was canceled by an unidentified local user, i.e., a user at a
console at the device. This value should be supported if the
implementation supports canceling jobs at the console.

- ABORTED_BY_SYSTEM

```java
public static final
JobStateReason
ABORTED_BY_SYSTEM
```

The job was aborted by the system. Either the job (1) is in the process
of being aborted, (2) has been aborted by the system and placed in the

ABORTED

state, or (3) has been aborted by the system and placed
in the

PENDING_HELD

state, so that a user or operator can
manually try the job again. This value should be supported.

- UNSUPPORTED_COMPRESSION

```java
public static final
JobStateReason
UNSUPPORTED_COMPRESSION
```

The job was aborted by the system because the printer determined while
attempting to decompress the document's data that the compression is
actually not among those supported by the printer. This value must be
supported, since

Compression

is a required doc
description attribute.

- COMPRESSION_ERROR

```java
public static final
JobStateReason
COMPRESSION_ERROR
```

The job was aborted by the system because the printer encountered an
error in the document data while decompressing it. If the printer posts
this reason, the document data has already passed any tests that would
have led to the

UNSUPPORTED_COMPRESSION

job state reason.

- UNSUPPORTED_DOCUMENT_FORMAT

```java
public static final
JobStateReason
UNSUPPORTED_DOCUMENT_FORMAT
```

The job was aborted by the system because the document data's document
format (doc flavor) is not among those supported by the printer. If the
client specifies a doc flavor with a MIME type of

"application/octet-stream"

, the printer may abort the job if the
printer cannot determine the document data's actual format through
auto-sensing (even if the printer supports the document format if
specified explicitly). This value must be supported, since a doc flavor
is required to be specified for each doc.

- DOCUMENT_FORMAT_ERROR

```java
public static final
JobStateReason
DOCUMENT_FORMAT_ERROR
```

The job was aborted by the system because the printer encountered an
error in the document data while processing it. If the printer posts this
reason, the document data has already passed any tests that would have
led to the

UNSUPPORTED_DOCUMENT_FORMAT

job state reason.

- PROCESSING_TO_STOP_POINT

```java
public static final
JobStateReason
PROCESSING_TO_STOP_POINT
```

The requester has canceled the job or the printer has aborted the job,
but the printer is still performing some actions on the job until a
specified stop point occurs or job termination/cleanup is completed.

If the implementation requires some measurable time to cancel the job in
the

PROCESSING

or

PROCESSING_STOPPED

job states, the
printer must use this reason to indicate that the printer is still
performing some actions on the job while the job remains in the

PROCESSING

or

PROCESSING_STOPPED

state. After all the
job's job description attributes have stopped incrementing, the printer
moves the job from the PROCESSING state to the

CANCELED

or

ABORTED

job states.

- SERVICE_OFF_LINE

```java
public static final
JobStateReason
SERVICE_OFF_LINE
```

The printer is off-line and accepting no jobs. All

PENDING

jobs
are put into the

PENDING_HELD

state. This situation could be true
if the service's or document transform's input is impaired or broken.

- JOB_COMPLETED_SUCCESSFULLY

```java
public static final
JobStateReason
JOB_COMPLETED_SUCCESSFULLY
```

The job completed successfully. This value should be supported.

- JOB_COMPLETED_WITH_WARNINGS

```java
public static final
JobStateReason
JOB_COMPLETED_WITH_WARNINGS
```

The job completed with warnings. This value should be supported if the
implementation detects warnings.

- JOB_COMPLETED_WITH_ERRORS

```java
public static final
JobStateReason
JOB_COMPLETED_WITH_ERRORS
```

The job completed with errors (and possibly warnings too). This value
should be supported if the implementation detects errors.

- JOB_RESTARTABLE

```java
public static final
JobStateReason
JOB_RESTARTABLE
```

This job is retained and is currently able to be restarted. If

JOB_RESTARTABLE

is contained in the job's

JobStateReasons

attribute, then the printer must
accept a request to restart that job. This value should be supported if
restarting jobs is supported.

[The capability for restarting jobs is
not in the Java Print Service API at present.]

- QUEUED_IN_DEVICE

```java
public static final
JobStateReason
QUEUED_IN_DEVICE
```

The job has been forwarded to a device or print system that is unable to
send back status. The printer sets the job's

JobState

attribute to

COMPLETED

and adds the

QUEUED_IN_DEVICE

reason to the job's

JobStateReasons

attribute to
indicate that the printer has no additional information about the job and
never will have any better information.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JobStateReason

```java
protected JobStateReason​(int value)
```

Construct a new job state reason enumeration value with the given integer
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

JobStateReason

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

JobStateReason

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

JobStateReason

and any vendor-defined subclasses, the
category is class

JobStateReason

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

JobStateReason

and any vendor-defined subclasses, the
category name is

"job-state-reason"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Field Detail

- JOB_INCOMING

```java
public static final
JobStateReason
JOB_INCOMING
```

The printer has created the Print Job, but the printer has not finished
accessing or accepting all the print data yet.

- JOB_DATA_INSUFFICIENT

```java
public static final
JobStateReason
JOB_DATA_INSUFFICIENT
```

The printer has created the Print Job, but the printer is expecting
additional print data before it can move the job into the

PROCESSING

state. If a printer starts processing before it has
received all data, the printer removes the

JOB_DATA_INSUFFICIENT

reason, but the

JOB_INCOMING

reason remains. If a printer starts
processing after it has received all data, the printer removes the

JOB_DATA_INSUFFICIENT

and

JOB_INCOMING

reasons at the
same time.

- DOCUMENT_ACCESS_ERROR

```java
public static final
JobStateReason
DOCUMENT_ACCESS_ERROR
```

The printer could not access one or more documents passed by reference
(i.e., the print data representation object is a

URL

). This
reason is intended to cover any file access problem,including file does
not exist and access denied because of an access control problem. Whether
the printer aborts the job and moves the job to the

ABORTED

job
state or prints all documents that are accessible and moves the job to
the

COMPLETED

job state and adds the

COMPLETED_WITH_ERRORS

reason to the job's

JobStateReasons

attribute depends on
implementation and/or site policy. This value should be supported if the
printer supports doc flavors with

URL

print data representation
objects.

- SUBMISSION_INTERRUPTED

```java
public static final
JobStateReason
SUBMISSION_INTERRUPTED
```

The job was not completely submitted for some unforeseen reason.
Possibilities include (1) the printer has crashed before the job was
fully submitted by the client, (2) the printer or the document transfer
method has crashed in some non-recoverable way before the document data
was entirely transferred to the printer, (3) the client crashed before
the job was fully submitted.

- JOB_OUTGOING

```java
public static final
JobStateReason
JOB_OUTGOING
```

The printer is transmitting the job to the output device.

- JOB_HOLD_UNTIL_SPECIFIED

```java
public static final
JobStateReason
JOB_HOLD_UNTIL_SPECIFIED
```

The value of the job's

JobHoldUntil

attribute was
specified with a date-time that is still in the future. The job must not
be a candidate for processing until this reason is removed and there are
no other reasons to hold the job. This value should be supported if the

JobHoldUntil

job template attribute is supported.

- RESOURCES_ARE_NOT_READY

```java
public static final
JobStateReason
RESOURCES_ARE_NOT_READY
```

At least one of the resources needed by the job, such as media, fonts,
resource objects, etc., is not ready on any of the physical printers for
which the job is a candidate. This condition may be detected when the job
is accepted, or subsequently while the job is pending or processing,
depending on implementation. The job may remain in its current state or
be moved to the

PENDING_HELD

state, depending on implementation
and/or job scheduling policy.

- PRINTER_STOPPED_PARTLY

```java
public static final
JobStateReason
PRINTER_STOPPED_PARTLY
```

The value of the printer's

PrinterStateReasons

attribute contains a

PrinterStateReason

value of

STOPPED_PARTLY

.

- PRINTER_STOPPED

```java
public static final
JobStateReason
PRINTER_STOPPED
```

The value of the printer's

PrinterState

attribute ia

STOPPED

.

- JOB_INTERPRETING

```java
public static final
JobStateReason
JOB_INTERPRETING
```

The job is in the

PROCESSING

state, but more specifically, the
printer ia interpreting the document data.

- JOB_QUEUED

```java
public static final
JobStateReason
JOB_QUEUED
```

The job is in the

PROCESSING

state, but more specifically, the
printer has queued the document data.

- JOB_TRANSFORMING

```java
public static final
JobStateReason
JOB_TRANSFORMING
```

The job is in the

PROCESSING

state, but more specifically, the
printer is interpreting document data and producing another electronic
representation.

- JOB_QUEUED_FOR_MARKER

```java
public static final
JobStateReason
JOB_QUEUED_FOR_MARKER
```

The job is in the

PENDING_HELD

,

PENDING

, or

PROCESSING

state, but more specifically, the printer has
completed enough processing of the document to be able to start marking
and the job is waiting for the marker. Systems that require human
intervention to release jobs put the job into the

PENDING_HELD

job state. Systems that automatically select a job to use the marker put
the job into the

PENDING

job state or keep the job in the

PROCESSING

job state while waiting for the marker, depending on
implementation. All implementations put the job into (or back into) the

PROCESSING

state when marking does begin.

- JOB_PRINTING

```java
public static final
JobStateReason
JOB_PRINTING
```

The output device is marking media. This value is useful for printers
which spend a great deal of time processing (1) when no marking is
happening and then want to show that marking is now happening or (2) when
the job is in the process of being canceled or aborted while the job
remains in the

PROCESSING

state, but the marking has not yet
stopped so that impression or sheet counts are still increasing for the
job.

- JOB_CANCELED_BY_USER

```java
public static final
JobStateReason
JOB_CANCELED_BY_USER
```

The job was canceled by the owner of the job, i.e., by a user whose
authenticated identity is the same as the value of the originating user
that created the Print Job, or by some other authorized end-user, such as
a member of the job owner's security group. This value should be
supported.

- JOB_CANCELED_BY_OPERATOR

```java
public static final
JobStateReason
JOB_CANCELED_BY_OPERATOR
```

The job was canceled by the operator, i.e., by a user who has been
authenticated as having operator privileges (whether local or remote). If
the security policy is to allow anyone to cancel anyone's job, then this
value may be used when the job is canceled by someone other than the
owner of the job. For such a security policy, in effect, everyone is an
operator as far as canceling jobs is concerned. This value should be
supported if the implementation permits canceling by someone other than
the owner of the job.

- JOB_CANCELED_AT_DEVICE

```java
public static final
JobStateReason
JOB_CANCELED_AT_DEVICE
```

The job was canceled by an unidentified local user, i.e., a user at a
console at the device. This value should be supported if the
implementation supports canceling jobs at the console.

- ABORTED_BY_SYSTEM

```java
public static final
JobStateReason
ABORTED_BY_SYSTEM
```

The job was aborted by the system. Either the job (1) is in the process
of being aborted, (2) has been aborted by the system and placed in the

ABORTED

state, or (3) has been aborted by the system and placed
in the

PENDING_HELD

state, so that a user or operator can
manually try the job again. This value should be supported.

- UNSUPPORTED_COMPRESSION

```java
public static final
JobStateReason
UNSUPPORTED_COMPRESSION
```

The job was aborted by the system because the printer determined while
attempting to decompress the document's data that the compression is
actually not among those supported by the printer. This value must be
supported, since

Compression

is a required doc
description attribute.

- COMPRESSION_ERROR

```java
public static final
JobStateReason
COMPRESSION_ERROR
```

The job was aborted by the system because the printer encountered an
error in the document data while decompressing it. If the printer posts
this reason, the document data has already passed any tests that would
have led to the

UNSUPPORTED_COMPRESSION

job state reason.

- UNSUPPORTED_DOCUMENT_FORMAT

```java
public static final
JobStateReason
UNSUPPORTED_DOCUMENT_FORMAT
```

The job was aborted by the system because the document data's document
format (doc flavor) is not among those supported by the printer. If the
client specifies a doc flavor with a MIME type of

"application/octet-stream"

, the printer may abort the job if the
printer cannot determine the document data's actual format through
auto-sensing (even if the printer supports the document format if
specified explicitly). This value must be supported, since a doc flavor
is required to be specified for each doc.

- DOCUMENT_FORMAT_ERROR

```java
public static final
JobStateReason
DOCUMENT_FORMAT_ERROR
```

The job was aborted by the system because the printer encountered an
error in the document data while processing it. If the printer posts this
reason, the document data has already passed any tests that would have
led to the

UNSUPPORTED_DOCUMENT_FORMAT

job state reason.

- PROCESSING_TO_STOP_POINT

```java
public static final
JobStateReason
PROCESSING_TO_STOP_POINT
```

The requester has canceled the job or the printer has aborted the job,
but the printer is still performing some actions on the job until a
specified stop point occurs or job termination/cleanup is completed.

If the implementation requires some measurable time to cancel the job in
the

PROCESSING

or

PROCESSING_STOPPED

job states, the
printer must use this reason to indicate that the printer is still
performing some actions on the job while the job remains in the

PROCESSING

or

PROCESSING_STOPPED

state. After all the
job's job description attributes have stopped incrementing, the printer
moves the job from the PROCESSING state to the

CANCELED

or

ABORTED

job states.

- SERVICE_OFF_LINE

```java
public static final
JobStateReason
SERVICE_OFF_LINE
```

The printer is off-line and accepting no jobs. All

PENDING

jobs
are put into the

PENDING_HELD

state. This situation could be true
if the service's or document transform's input is impaired or broken.

- JOB_COMPLETED_SUCCESSFULLY

```java
public static final
JobStateReason
JOB_COMPLETED_SUCCESSFULLY
```

The job completed successfully. This value should be supported.

- JOB_COMPLETED_WITH_WARNINGS

```java
public static final
JobStateReason
JOB_COMPLETED_WITH_WARNINGS
```

The job completed with warnings. This value should be supported if the
implementation detects warnings.

- JOB_COMPLETED_WITH_ERRORS

```java
public static final
JobStateReason
JOB_COMPLETED_WITH_ERRORS
```

The job completed with errors (and possibly warnings too). This value
should be supported if the implementation detects errors.

- JOB_RESTARTABLE

```java
public static final
JobStateReason
JOB_RESTARTABLE
```

This job is retained and is currently able to be restarted. If

JOB_RESTARTABLE

is contained in the job's

JobStateReasons

attribute, then the printer must
accept a request to restart that job. This value should be supported if
restarting jobs is supported.

[The capability for restarting jobs is
not in the Java Print Service API at present.]

- QUEUED_IN_DEVICE

```java
public static final
JobStateReason
QUEUED_IN_DEVICE
```

The job has been forwarded to a device or print system that is unable to
send back status. The printer sets the job's

JobState

attribute to

COMPLETED

and adds the

QUEUED_IN_DEVICE

reason to the job's

JobStateReasons

attribute to
indicate that the printer has no additional information about the job and
never will have any better information.

---

#### Field Detail

JOB_INCOMING

```java
public static final
JobStateReason
JOB_INCOMING
```

The printer has created the Print Job, but the printer has not finished
accessing or accepting all the print data yet.

---

#### JOB_INCOMING

public static final

JobStateReason

JOB_INCOMING

The printer has created the Print Job, but the printer has not finished
accessing or accepting all the print data yet.

JOB_DATA_INSUFFICIENT

```java
public static final
JobStateReason
JOB_DATA_INSUFFICIENT
```

The printer has created the Print Job, but the printer is expecting
additional print data before it can move the job into the

PROCESSING

state. If a printer starts processing before it has
received all data, the printer removes the

JOB_DATA_INSUFFICIENT

reason, but the

JOB_INCOMING

reason remains. If a printer starts
processing after it has received all data, the printer removes the

JOB_DATA_INSUFFICIENT

and

JOB_INCOMING

reasons at the
same time.

---

#### JOB_DATA_INSUFFICIENT

public static final

JobStateReason

JOB_DATA_INSUFFICIENT

The printer has created the Print Job, but the printer is expecting
additional print data before it can move the job into the

PROCESSING

state. If a printer starts processing before it has
received all data, the printer removes the

JOB_DATA_INSUFFICIENT

reason, but the

JOB_INCOMING

reason remains. If a printer starts
processing after it has received all data, the printer removes the

JOB_DATA_INSUFFICIENT

and

JOB_INCOMING

reasons at the
same time.

DOCUMENT_ACCESS_ERROR

```java
public static final
JobStateReason
DOCUMENT_ACCESS_ERROR
```

The printer could not access one or more documents passed by reference
(i.e., the print data representation object is a

URL

). This
reason is intended to cover any file access problem,including file does
not exist and access denied because of an access control problem. Whether
the printer aborts the job and moves the job to the

ABORTED

job
state or prints all documents that are accessible and moves the job to
the

COMPLETED

job state and adds the

COMPLETED_WITH_ERRORS

reason to the job's

JobStateReasons

attribute depends on
implementation and/or site policy. This value should be supported if the
printer supports doc flavors with

URL

print data representation
objects.

---

#### DOCUMENT_ACCESS_ERROR

public static final

JobStateReason

DOCUMENT_ACCESS_ERROR

The printer could not access one or more documents passed by reference
(i.e., the print data representation object is a

URL

). This
reason is intended to cover any file access problem,including file does
not exist and access denied because of an access control problem. Whether
the printer aborts the job and moves the job to the

ABORTED

job
state or prints all documents that are accessible and moves the job to
the

COMPLETED

job state and adds the

COMPLETED_WITH_ERRORS

reason to the job's

JobStateReasons

attribute depends on
implementation and/or site policy. This value should be supported if the
printer supports doc flavors with

URL

print data representation
objects.

SUBMISSION_INTERRUPTED

```java
public static final
JobStateReason
SUBMISSION_INTERRUPTED
```

The job was not completely submitted for some unforeseen reason.
Possibilities include (1) the printer has crashed before the job was
fully submitted by the client, (2) the printer or the document transfer
method has crashed in some non-recoverable way before the document data
was entirely transferred to the printer, (3) the client crashed before
the job was fully submitted.

---

#### SUBMISSION_INTERRUPTED

public static final

JobStateReason

SUBMISSION_INTERRUPTED

The job was not completely submitted for some unforeseen reason.
Possibilities include (1) the printer has crashed before the job was
fully submitted by the client, (2) the printer or the document transfer
method has crashed in some non-recoverable way before the document data
was entirely transferred to the printer, (3) the client crashed before
the job was fully submitted.

JOB_OUTGOING

```java
public static final
JobStateReason
JOB_OUTGOING
```

The printer is transmitting the job to the output device.

---

#### JOB_OUTGOING

public static final

JobStateReason

JOB_OUTGOING

The printer is transmitting the job to the output device.

JOB_HOLD_UNTIL_SPECIFIED

```java
public static final
JobStateReason
JOB_HOLD_UNTIL_SPECIFIED
```

The value of the job's

JobHoldUntil

attribute was
specified with a date-time that is still in the future. The job must not
be a candidate for processing until this reason is removed and there are
no other reasons to hold the job. This value should be supported if the

JobHoldUntil

job template attribute is supported.

---

#### JOB_HOLD_UNTIL_SPECIFIED

public static final

JobStateReason

JOB_HOLD_UNTIL_SPECIFIED

The value of the job's

JobHoldUntil

attribute was
specified with a date-time that is still in the future. The job must not
be a candidate for processing until this reason is removed and there are
no other reasons to hold the job. This value should be supported if the

JobHoldUntil

job template attribute is supported.

RESOURCES_ARE_NOT_READY

```java
public static final
JobStateReason
RESOURCES_ARE_NOT_READY
```

At least one of the resources needed by the job, such as media, fonts,
resource objects, etc., is not ready on any of the physical printers for
which the job is a candidate. This condition may be detected when the job
is accepted, or subsequently while the job is pending or processing,
depending on implementation. The job may remain in its current state or
be moved to the

PENDING_HELD

state, depending on implementation
and/or job scheduling policy.

---

#### RESOURCES_ARE_NOT_READY

public static final

JobStateReason

RESOURCES_ARE_NOT_READY

At least one of the resources needed by the job, such as media, fonts,
resource objects, etc., is not ready on any of the physical printers for
which the job is a candidate. This condition may be detected when the job
is accepted, or subsequently while the job is pending or processing,
depending on implementation. The job may remain in its current state or
be moved to the

PENDING_HELD

state, depending on implementation
and/or job scheduling policy.

PRINTER_STOPPED_PARTLY

```java
public static final
JobStateReason
PRINTER_STOPPED_PARTLY
```

The value of the printer's

PrinterStateReasons

attribute contains a

PrinterStateReason

value of

STOPPED_PARTLY

.

---

#### PRINTER_STOPPED_PARTLY

public static final

JobStateReason

PRINTER_STOPPED_PARTLY

The value of the printer's

PrinterStateReasons

attribute contains a

PrinterStateReason

value of

STOPPED_PARTLY

.

PRINTER_STOPPED

```java
public static final
JobStateReason
PRINTER_STOPPED
```

The value of the printer's

PrinterState

attribute ia

STOPPED

.

---

#### PRINTER_STOPPED

public static final

JobStateReason

PRINTER_STOPPED

The value of the printer's

PrinterState

attribute ia

STOPPED

.

JOB_INTERPRETING

```java
public static final
JobStateReason
JOB_INTERPRETING
```

The job is in the

PROCESSING

state, but more specifically, the
printer ia interpreting the document data.

---

#### JOB_INTERPRETING

public static final

JobStateReason

JOB_INTERPRETING

The job is in the

PROCESSING

state, but more specifically, the
printer ia interpreting the document data.

JOB_QUEUED

```java
public static final
JobStateReason
JOB_QUEUED
```

The job is in the

PROCESSING

state, but more specifically, the
printer has queued the document data.

---

#### JOB_QUEUED

public static final

JobStateReason

JOB_QUEUED

The job is in the

PROCESSING

state, but more specifically, the
printer has queued the document data.

JOB_TRANSFORMING

```java
public static final
JobStateReason
JOB_TRANSFORMING
```

The job is in the

PROCESSING

state, but more specifically, the
printer is interpreting document data and producing another electronic
representation.

---

#### JOB_TRANSFORMING

public static final

JobStateReason

JOB_TRANSFORMING

The job is in the

PROCESSING

state, but more specifically, the
printer is interpreting document data and producing another electronic
representation.

JOB_QUEUED_FOR_MARKER

```java
public static final
JobStateReason
JOB_QUEUED_FOR_MARKER
```

The job is in the

PENDING_HELD

,

PENDING

, or

PROCESSING

state, but more specifically, the printer has
completed enough processing of the document to be able to start marking
and the job is waiting for the marker. Systems that require human
intervention to release jobs put the job into the

PENDING_HELD

job state. Systems that automatically select a job to use the marker put
the job into the

PENDING

job state or keep the job in the

PROCESSING

job state while waiting for the marker, depending on
implementation. All implementations put the job into (or back into) the

PROCESSING

state when marking does begin.

---

#### JOB_QUEUED_FOR_MARKER

public static final

JobStateReason

JOB_QUEUED_FOR_MARKER

The job is in the

PENDING_HELD

,

PENDING

, or

PROCESSING

state, but more specifically, the printer has
completed enough processing of the document to be able to start marking
and the job is waiting for the marker. Systems that require human
intervention to release jobs put the job into the

PENDING_HELD

job state. Systems that automatically select a job to use the marker put
the job into the

PENDING

job state or keep the job in the

PROCESSING

job state while waiting for the marker, depending on
implementation. All implementations put the job into (or back into) the

PROCESSING

state when marking does begin.

JOB_PRINTING

```java
public static final
JobStateReason
JOB_PRINTING
```

The output device is marking media. This value is useful for printers
which spend a great deal of time processing (1) when no marking is
happening and then want to show that marking is now happening or (2) when
the job is in the process of being canceled or aborted while the job
remains in the

PROCESSING

state, but the marking has not yet
stopped so that impression or sheet counts are still increasing for the
job.

---

#### JOB_PRINTING

public static final

JobStateReason

JOB_PRINTING

The output device is marking media. This value is useful for printers
which spend a great deal of time processing (1) when no marking is
happening and then want to show that marking is now happening or (2) when
the job is in the process of being canceled or aborted while the job
remains in the

PROCESSING

state, but the marking has not yet
stopped so that impression or sheet counts are still increasing for the
job.

JOB_CANCELED_BY_USER

```java
public static final
JobStateReason
JOB_CANCELED_BY_USER
```

The job was canceled by the owner of the job, i.e., by a user whose
authenticated identity is the same as the value of the originating user
that created the Print Job, or by some other authorized end-user, such as
a member of the job owner's security group. This value should be
supported.

---

#### JOB_CANCELED_BY_USER

public static final

JobStateReason

JOB_CANCELED_BY_USER

The job was canceled by the owner of the job, i.e., by a user whose
authenticated identity is the same as the value of the originating user
that created the Print Job, or by some other authorized end-user, such as
a member of the job owner's security group. This value should be
supported.

JOB_CANCELED_BY_OPERATOR

```java
public static final
JobStateReason
JOB_CANCELED_BY_OPERATOR
```

The job was canceled by the operator, i.e., by a user who has been
authenticated as having operator privileges (whether local or remote). If
the security policy is to allow anyone to cancel anyone's job, then this
value may be used when the job is canceled by someone other than the
owner of the job. For such a security policy, in effect, everyone is an
operator as far as canceling jobs is concerned. This value should be
supported if the implementation permits canceling by someone other than
the owner of the job.

---

#### JOB_CANCELED_BY_OPERATOR

public static final

JobStateReason

JOB_CANCELED_BY_OPERATOR

The job was canceled by the operator, i.e., by a user who has been
authenticated as having operator privileges (whether local or remote). If
the security policy is to allow anyone to cancel anyone's job, then this
value may be used when the job is canceled by someone other than the
owner of the job. For such a security policy, in effect, everyone is an
operator as far as canceling jobs is concerned. This value should be
supported if the implementation permits canceling by someone other than
the owner of the job.

JOB_CANCELED_AT_DEVICE

```java
public static final
JobStateReason
JOB_CANCELED_AT_DEVICE
```

The job was canceled by an unidentified local user, i.e., a user at a
console at the device. This value should be supported if the
implementation supports canceling jobs at the console.

---

#### JOB_CANCELED_AT_DEVICE

public static final

JobStateReason

JOB_CANCELED_AT_DEVICE

The job was canceled by an unidentified local user, i.e., a user at a
console at the device. This value should be supported if the
implementation supports canceling jobs at the console.

ABORTED_BY_SYSTEM

```java
public static final
JobStateReason
ABORTED_BY_SYSTEM
```

The job was aborted by the system. Either the job (1) is in the process
of being aborted, (2) has been aborted by the system and placed in the

ABORTED

state, or (3) has been aborted by the system and placed
in the

PENDING_HELD

state, so that a user or operator can
manually try the job again. This value should be supported.

---

#### ABORTED_BY_SYSTEM

public static final

JobStateReason

ABORTED_BY_SYSTEM

The job was aborted by the system. Either the job (1) is in the process
of being aborted, (2) has been aborted by the system and placed in the

ABORTED

state, or (3) has been aborted by the system and placed
in the

PENDING_HELD

state, so that a user or operator can
manually try the job again. This value should be supported.

UNSUPPORTED_COMPRESSION

```java
public static final
JobStateReason
UNSUPPORTED_COMPRESSION
```

The job was aborted by the system because the printer determined while
attempting to decompress the document's data that the compression is
actually not among those supported by the printer. This value must be
supported, since

Compression

is a required doc
description attribute.

---

#### UNSUPPORTED_COMPRESSION

public static final

JobStateReason

UNSUPPORTED_COMPRESSION

The job was aborted by the system because the printer determined while
attempting to decompress the document's data that the compression is
actually not among those supported by the printer. This value must be
supported, since

Compression

is a required doc
description attribute.

COMPRESSION_ERROR

```java
public static final
JobStateReason
COMPRESSION_ERROR
```

The job was aborted by the system because the printer encountered an
error in the document data while decompressing it. If the printer posts
this reason, the document data has already passed any tests that would
have led to the

UNSUPPORTED_COMPRESSION

job state reason.

---

#### COMPRESSION_ERROR

public static final

JobStateReason

COMPRESSION_ERROR

The job was aborted by the system because the printer encountered an
error in the document data while decompressing it. If the printer posts
this reason, the document data has already passed any tests that would
have led to the

UNSUPPORTED_COMPRESSION

job state reason.

UNSUPPORTED_DOCUMENT_FORMAT

```java
public static final
JobStateReason
UNSUPPORTED_DOCUMENT_FORMAT
```

The job was aborted by the system because the document data's document
format (doc flavor) is not among those supported by the printer. If the
client specifies a doc flavor with a MIME type of

"application/octet-stream"

, the printer may abort the job if the
printer cannot determine the document data's actual format through
auto-sensing (even if the printer supports the document format if
specified explicitly). This value must be supported, since a doc flavor
is required to be specified for each doc.

---

#### UNSUPPORTED_DOCUMENT_FORMAT

public static final

JobStateReason

UNSUPPORTED_DOCUMENT_FORMAT

The job was aborted by the system because the document data's document
format (doc flavor) is not among those supported by the printer. If the
client specifies a doc flavor with a MIME type of

"application/octet-stream"

, the printer may abort the job if the
printer cannot determine the document data's actual format through
auto-sensing (even if the printer supports the document format if
specified explicitly). This value must be supported, since a doc flavor
is required to be specified for each doc.

DOCUMENT_FORMAT_ERROR

```java
public static final
JobStateReason
DOCUMENT_FORMAT_ERROR
```

The job was aborted by the system because the printer encountered an
error in the document data while processing it. If the printer posts this
reason, the document data has already passed any tests that would have
led to the

UNSUPPORTED_DOCUMENT_FORMAT

job state reason.

---

#### DOCUMENT_FORMAT_ERROR

public static final

JobStateReason

DOCUMENT_FORMAT_ERROR

The job was aborted by the system because the printer encountered an
error in the document data while processing it. If the printer posts this
reason, the document data has already passed any tests that would have
led to the

UNSUPPORTED_DOCUMENT_FORMAT

job state reason.

PROCESSING_TO_STOP_POINT

```java
public static final
JobStateReason
PROCESSING_TO_STOP_POINT
```

The requester has canceled the job or the printer has aborted the job,
but the printer is still performing some actions on the job until a
specified stop point occurs or job termination/cleanup is completed.

If the implementation requires some measurable time to cancel the job in
the

PROCESSING

or

PROCESSING_STOPPED

job states, the
printer must use this reason to indicate that the printer is still
performing some actions on the job while the job remains in the

PROCESSING

or

PROCESSING_STOPPED

state. After all the
job's job description attributes have stopped incrementing, the printer
moves the job from the PROCESSING state to the

CANCELED

or

ABORTED

job states.

---

#### PROCESSING_TO_STOP_POINT

public static final

JobStateReason

PROCESSING_TO_STOP_POINT

The requester has canceled the job or the printer has aborted the job,
but the printer is still performing some actions on the job until a
specified stop point occurs or job termination/cleanup is completed.

If the implementation requires some measurable time to cancel the job in
the

PROCESSING

or

PROCESSING_STOPPED

job states, the
printer must use this reason to indicate that the printer is still
performing some actions on the job while the job remains in the

PROCESSING

or

PROCESSING_STOPPED

state. After all the
job's job description attributes have stopped incrementing, the printer
moves the job from the PROCESSING state to the

CANCELED

or

ABORTED

job states.

If the implementation requires some measurable time to cancel the job in
the

PROCESSING

or

PROCESSING_STOPPED

job states, the
printer must use this reason to indicate that the printer is still
performing some actions on the job while the job remains in the

PROCESSING

or

PROCESSING_STOPPED

state. After all the
job's job description attributes have stopped incrementing, the printer
moves the job from the PROCESSING state to the

CANCELED

or

ABORTED

job states.

SERVICE_OFF_LINE

```java
public static final
JobStateReason
SERVICE_OFF_LINE
```

The printer is off-line and accepting no jobs. All

PENDING

jobs
are put into the

PENDING_HELD

state. This situation could be true
if the service's or document transform's input is impaired or broken.

---

#### SERVICE_OFF_LINE

public static final

JobStateReason

SERVICE_OFF_LINE

The printer is off-line and accepting no jobs. All

PENDING

jobs
are put into the

PENDING_HELD

state. This situation could be true
if the service's or document transform's input is impaired or broken.

JOB_COMPLETED_SUCCESSFULLY

```java
public static final
JobStateReason
JOB_COMPLETED_SUCCESSFULLY
```

The job completed successfully. This value should be supported.

---

#### JOB_COMPLETED_SUCCESSFULLY

public static final

JobStateReason

JOB_COMPLETED_SUCCESSFULLY

The job completed successfully. This value should be supported.

JOB_COMPLETED_WITH_WARNINGS

```java
public static final
JobStateReason
JOB_COMPLETED_WITH_WARNINGS
```

The job completed with warnings. This value should be supported if the
implementation detects warnings.

---

#### JOB_COMPLETED_WITH_WARNINGS

public static final

JobStateReason

JOB_COMPLETED_WITH_WARNINGS

The job completed with warnings. This value should be supported if the
implementation detects warnings.

JOB_COMPLETED_WITH_ERRORS

```java
public static final
JobStateReason
JOB_COMPLETED_WITH_ERRORS
```

The job completed with errors (and possibly warnings too). This value
should be supported if the implementation detects errors.

---

#### JOB_COMPLETED_WITH_ERRORS

public static final

JobStateReason

JOB_COMPLETED_WITH_ERRORS

The job completed with errors (and possibly warnings too). This value
should be supported if the implementation detects errors.

JOB_RESTARTABLE

```java
public static final
JobStateReason
JOB_RESTARTABLE
```

This job is retained and is currently able to be restarted. If

JOB_RESTARTABLE

is contained in the job's

JobStateReasons

attribute, then the printer must
accept a request to restart that job. This value should be supported if
restarting jobs is supported.

[The capability for restarting jobs is
not in the Java Print Service API at present.]

---

#### JOB_RESTARTABLE

public static final

JobStateReason

JOB_RESTARTABLE

This job is retained and is currently able to be restarted. If

JOB_RESTARTABLE

is contained in the job's

JobStateReasons

attribute, then the printer must
accept a request to restart that job. This value should be supported if
restarting jobs is supported.

[The capability for restarting jobs is
not in the Java Print Service API at present.]

QUEUED_IN_DEVICE

```java
public static final
JobStateReason
QUEUED_IN_DEVICE
```

The job has been forwarded to a device or print system that is unable to
send back status. The printer sets the job's

JobState

attribute to

COMPLETED

and adds the

QUEUED_IN_DEVICE

reason to the job's

JobStateReasons

attribute to
indicate that the printer has no additional information about the job and
never will have any better information.

---

#### QUEUED_IN_DEVICE

public static final

JobStateReason

QUEUED_IN_DEVICE

The job has been forwarded to a device or print system that is unable to
send back status. The printer sets the job's

JobState

attribute to

COMPLETED

and adds the

QUEUED_IN_DEVICE

reason to the job's

JobStateReasons

attribute to
indicate that the printer has no additional information about the job and
never will have any better information.

Constructor Detail

- JobStateReason

```java
protected JobStateReason​(int value)
```

Construct a new job state reason enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

JobStateReason

```java
protected JobStateReason​(int value)
```

Construct a new job state reason enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### JobStateReason

protected JobStateReason​(int value)

Construct a new job state reason enumeration value with the given integer
value.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

JobStateReason

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

JobStateReason

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

JobStateReason

and any vendor-defined subclasses, the
category is class

JobStateReason

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

JobStateReason

and any vendor-defined subclasses, the
category name is

"job-state-reason"

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

JobStateReason

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

JobStateReason

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

JobStateReason

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

JobStateReason

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

JobStateReason

and any vendor-defined subclasses, the
category is class

JobStateReason

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

JobStateReason

and any vendor-defined subclasses, the
category is class

JobStateReason

itself.

For class

JobStateReason

and any vendor-defined subclasses, the
category is class

JobStateReason

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

JobStateReason

and any vendor-defined subclasses, the
category name is

"job-state-reason"

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

JobStateReason

and any vendor-defined subclasses, the
category name is

"job-state-reason"

.

For class

JobStateReason

and any vendor-defined subclasses, the
category name is

"job-state-reason"

.

---

