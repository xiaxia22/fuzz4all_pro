# Interface XMLReporter

**Source:** `java.xml\javax\xml\stream\XMLReporter.html`

### Class Description

```java
public interface
XMLReporter
```

This interface is used to report non-fatal errors.
Only warnings should be echoed through this interface.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void report​(
String
message,

String
errorType,

Object
relatedInformation,

Location
location)
throws
XMLStreamException

Report the desired message in an application specific format.

Only warnings and non-fatal errors should be reported through

this interface.

Fatal errors should be thrown as XMLStreamException.

**Parameters:**
- message

- the error message
- errorType

- an implementation defined error type
- relatedInformation

- information related to the error, if available
- location

- the location of the error, if available

**Throws:**
- XMLStreamException

---

### Additional Sections

#### Interface XMLReporter

```java
public interface
XMLReporter
```

This interface is used to report non-fatal errors.
Only warnings should be echoed through this interface.

**Since:** 1.6

public interface

XMLReporter

This interface is used to report non-fatal errors.
Only warnings should be echoed through this interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

report

​(

String

message,

String

errorType,

Object

relatedInformation,

Location

location)

Report the desired message in an application specific format.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

report

​(

String

message,

String

errorType,

Object

relatedInformation,

Location

location)

Report the desired message in an application specific format.

---

#### Method Summary

Report the desired message in an application specific format.

============ METHOD DETAIL ==========

- Method Detail

- report

```java
void report​(
String
message,

String
errorType,

Object
relatedInformation,

Location
location)
throws
XMLStreamException
```

Report the desired message in an application specific format.

Only warnings and non-fatal errors should be reported through

this interface.

Fatal errors should be thrown as XMLStreamException.

**Parameters:** message

- the error message
**Parameters:** errorType

- an implementation defined error type
**Parameters:** relatedInformation

- information related to the error, if available
**Parameters:** location

- the location of the error, if available
**Throws:** XMLStreamException

Method Detail

- report

```java
void report​(
String
message,

String
errorType,

Object
relatedInformation,

Location
location)
throws
XMLStreamException
```

Report the desired message in an application specific format.

Only warnings and non-fatal errors should be reported through

this interface.

Fatal errors should be thrown as XMLStreamException.

**Parameters:** message

- the error message
**Parameters:** errorType

- an implementation defined error type
**Parameters:** relatedInformation

- information related to the error, if available
**Parameters:** location

- the location of the error, if available
**Throws:** XMLStreamException

---

#### Method Detail

report

```java
void report​(
String
message,

String
errorType,

Object
relatedInformation,

Location
location)
throws
XMLStreamException
```

Report the desired message in an application specific format.

Only warnings and non-fatal errors should be reported through

this interface.

Fatal errors should be thrown as XMLStreamException.

**Parameters:** message

- the error message
**Parameters:** errorType

- an implementation defined error type
**Parameters:** relatedInformation

- information related to the error, if available
**Parameters:** location

- the location of the error, if available
**Throws:** XMLStreamException

---

#### report

void report​(

String

message,

String

errorType,

Object

relatedInformation,

Location

location)
throws

XMLStreamException

Report the desired message in an application specific format.

Only warnings and non-fatal errors should be reported through

this interface.

Fatal errors should be thrown as XMLStreamException.

---

