# Interface Result

**Source:** `java.xml\javax\xml\transform\Result.html`

### Class Description

```java
public interface
Result
```

An object that implements this interface contains the information
needed to build a transformation result tree.

**All Known Implementing Classes:** DOMResult

,

SAXResult

,

StAXResult

,

StreamResult

---

### Field Details

#### static final
String
PI_DISABLE_OUTPUT_ESCAPING

The name of the processing instruction that is sent if the
result tree disables output escaping.

Normally, result tree serialization escapes& and < (and
possibly other characters) when outputting text nodes.
This ensures that the output is well-formed XML. However,
it is sometimes convenient to be able to produce output that is
almost, but not quite well-formed XML; for example,
the output may include ill-formed sections that will
be transformed into well-formed XML by a subsequent non-XML aware
process. If a processing instruction is sent with this name,
serialization should be output without any escaping.

Result DOM trees may also have PI_DISABLE_OUTPUT_ESCAPING and
PI_ENABLE_OUTPUT_ESCAPING inserted into the tree.

**See Also:**
- disable-output-escaping in XSLT Specification

,

Constant Field Values

---

#### static final
String
PI_ENABLE_OUTPUT_ESCAPING

The name of the processing instruction that is sent
if the result tree enables output escaping at some point after having
received a PI_DISABLE_OUTPUT_ESCAPING processing instruction.

**See Also:**
- disable-output-escaping in XSLT Specification

,

Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### void setSystemId​(
String
systemId)

Set the system identifier for this Result.

If the Result is not to be written to a file, the system identifier is optional.
The application may still want to provide one, however, for use in error messages
and warnings, or to resolve relative output identifiers.

**Parameters:**
- systemId

- The system identifier as a URI string.

---

#### String
getSystemId()

Get the system identifier that was set with setSystemId.

**Returns:**
- The system identifier that was set with setSystemId,
or null if setSystemId was not called.

---

### Additional Sections

#### Interface Result

**All Known Implementing Classes:** DOMResult

,

SAXResult

,

StAXResult

,

StreamResult

```java
public interface
Result
```

An object that implements this interface contains the information
needed to build a transformation result tree.

**Since:** 1.4

public interface

Result

An object that implements this interface contains the information
needed to build a transformation result tree.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

PI_DISABLE_OUTPUT_ESCAPING

The name of the processing instruction that is sent if the
result tree disables output escaping.

static

String

PI_ENABLE_OUTPUT_ESCAPING

The name of the processing instruction that is sent
if the result tree enables output escaping at some point after having
received a PI_DISABLE_OUTPUT_ESCAPING processing instruction.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getSystemId

()

Get the system identifier that was set with setSystemId.

void

setSystemId

​(

String

systemId)

Set the system identifier for this Result.

Field Summary

Fields

Modifier and Type

Field

Description

static

String

PI_DISABLE_OUTPUT_ESCAPING

The name of the processing instruction that is sent if the
result tree disables output escaping.

static

String

PI_ENABLE_OUTPUT_ESCAPING

The name of the processing instruction that is sent
if the result tree enables output escaping at some point after having
received a PI_DISABLE_OUTPUT_ESCAPING processing instruction.

---

#### Field Summary

The name of the processing instruction that is sent if the
result tree disables output escaping.

The name of the processing instruction that is sent
if the result tree enables output escaping at some point after having
received a PI_DISABLE_OUTPUT_ESCAPING processing instruction.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getSystemId

()

Get the system identifier that was set with setSystemId.

void

setSystemId

​(

String

systemId)

Set the system identifier for this Result.

---

#### Method Summary

Get the system identifier that was set with setSystemId.

Set the system identifier for this Result.

============ FIELD DETAIL ===========

- Field Detail

- PI_DISABLE_OUTPUT_ESCAPING

```java
static final
String
PI_DISABLE_OUTPUT_ESCAPING
```

The name of the processing instruction that is sent if the
result tree disables output escaping.

Normally, result tree serialization escapes& and < (and
possibly other characters) when outputting text nodes.
This ensures that the output is well-formed XML. However,
it is sometimes convenient to be able to produce output that is
almost, but not quite well-formed XML; for example,
the output may include ill-formed sections that will
be transformed into well-formed XML by a subsequent non-XML aware
process. If a processing instruction is sent with this name,
serialization should be output without any escaping.

Result DOM trees may also have PI_DISABLE_OUTPUT_ESCAPING and
PI_ENABLE_OUTPUT_ESCAPING inserted into the tree.

**See Also:** disable-output-escaping in XSLT Specification

,

Constant Field Values

- PI_ENABLE_OUTPUT_ESCAPING

```java
static final
String
PI_ENABLE_OUTPUT_ESCAPING
```

The name of the processing instruction that is sent
if the result tree enables output escaping at some point after having
received a PI_DISABLE_OUTPUT_ESCAPING processing instruction.

**See Also:** disable-output-escaping in XSLT Specification

,

Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- setSystemId

```java
void setSystemId​(
String
systemId)
```

Set the system identifier for this Result.

If the Result is not to be written to a file, the system identifier is optional.
The application may still want to provide one, however, for use in error messages
and warnings, or to resolve relative output identifiers.

**Parameters:** systemId

- The system identifier as a URI string.

- getSystemId

```java
String
getSystemId()
```

Get the system identifier that was set with setSystemId.

**Returns:** The system identifier that was set with setSystemId,
or null if setSystemId was not called.

Field Detail

- PI_DISABLE_OUTPUT_ESCAPING

```java
static final
String
PI_DISABLE_OUTPUT_ESCAPING
```

The name of the processing instruction that is sent if the
result tree disables output escaping.

Normally, result tree serialization escapes& and < (and
possibly other characters) when outputting text nodes.
This ensures that the output is well-formed XML. However,
it is sometimes convenient to be able to produce output that is
almost, but not quite well-formed XML; for example,
the output may include ill-formed sections that will
be transformed into well-formed XML by a subsequent non-XML aware
process. If a processing instruction is sent with this name,
serialization should be output without any escaping.

Result DOM trees may also have PI_DISABLE_OUTPUT_ESCAPING and
PI_ENABLE_OUTPUT_ESCAPING inserted into the tree.

**See Also:** disable-output-escaping in XSLT Specification

,

Constant Field Values

- PI_ENABLE_OUTPUT_ESCAPING

```java
static final
String
PI_ENABLE_OUTPUT_ESCAPING
```

The name of the processing instruction that is sent
if the result tree enables output escaping at some point after having
received a PI_DISABLE_OUTPUT_ESCAPING processing instruction.

**See Also:** disable-output-escaping in XSLT Specification

,

Constant Field Values

---

#### Field Detail

PI_DISABLE_OUTPUT_ESCAPING

```java
static final
String
PI_DISABLE_OUTPUT_ESCAPING
```

The name of the processing instruction that is sent if the
result tree disables output escaping.

Normally, result tree serialization escapes& and < (and
possibly other characters) when outputting text nodes.
This ensures that the output is well-formed XML. However,
it is sometimes convenient to be able to produce output that is
almost, but not quite well-formed XML; for example,
the output may include ill-formed sections that will
be transformed into well-formed XML by a subsequent non-XML aware
process. If a processing instruction is sent with this name,
serialization should be output without any escaping.

Result DOM trees may also have PI_DISABLE_OUTPUT_ESCAPING and
PI_ENABLE_OUTPUT_ESCAPING inserted into the tree.

**See Also:** disable-output-escaping in XSLT Specification

,

Constant Field Values

---

#### PI_DISABLE_OUTPUT_ESCAPING

static final

String

PI_DISABLE_OUTPUT_ESCAPING

The name of the processing instruction that is sent if the
result tree disables output escaping.

Normally, result tree serialization escapes& and < (and
possibly other characters) when outputting text nodes.
This ensures that the output is well-formed XML. However,
it is sometimes convenient to be able to produce output that is
almost, but not quite well-formed XML; for example,
the output may include ill-formed sections that will
be transformed into well-formed XML by a subsequent non-XML aware
process. If a processing instruction is sent with this name,
serialization should be output without any escaping.

Result DOM trees may also have PI_DISABLE_OUTPUT_ESCAPING and
PI_ENABLE_OUTPUT_ESCAPING inserted into the tree.

Normally, result tree serialization escapes& and < (and
possibly other characters) when outputting text nodes.
This ensures that the output is well-formed XML. However,
it is sometimes convenient to be able to produce output that is
almost, but not quite well-formed XML; for example,
the output may include ill-formed sections that will
be transformed into well-formed XML by a subsequent non-XML aware
process. If a processing instruction is sent with this name,
serialization should be output without any escaping.

Result DOM trees may also have PI_DISABLE_OUTPUT_ESCAPING and
PI_ENABLE_OUTPUT_ESCAPING inserted into the tree.

Result DOM trees may also have PI_DISABLE_OUTPUT_ESCAPING and
PI_ENABLE_OUTPUT_ESCAPING inserted into the tree.

PI_ENABLE_OUTPUT_ESCAPING

```java
static final
String
PI_ENABLE_OUTPUT_ESCAPING
```

The name of the processing instruction that is sent
if the result tree enables output escaping at some point after having
received a PI_DISABLE_OUTPUT_ESCAPING processing instruction.

**See Also:** disable-output-escaping in XSLT Specification

,

Constant Field Values

---

#### PI_ENABLE_OUTPUT_ESCAPING

static final

String

PI_ENABLE_OUTPUT_ESCAPING

The name of the processing instruction that is sent
if the result tree enables output escaping at some point after having
received a PI_DISABLE_OUTPUT_ESCAPING processing instruction.

Method Detail

- setSystemId

```java
void setSystemId​(
String
systemId)
```

Set the system identifier for this Result.

If the Result is not to be written to a file, the system identifier is optional.
The application may still want to provide one, however, for use in error messages
and warnings, or to resolve relative output identifiers.

**Parameters:** systemId

- The system identifier as a URI string.

- getSystemId

```java
String
getSystemId()
```

Get the system identifier that was set with setSystemId.

**Returns:** The system identifier that was set with setSystemId,
or null if setSystemId was not called.

---

#### Method Detail

setSystemId

```java
void setSystemId​(
String
systemId)
```

Set the system identifier for this Result.

If the Result is not to be written to a file, the system identifier is optional.
The application may still want to provide one, however, for use in error messages
and warnings, or to resolve relative output identifiers.

**Parameters:** systemId

- The system identifier as a URI string.

---

#### setSystemId

void setSystemId​(

String

systemId)

Set the system identifier for this Result.

If the Result is not to be written to a file, the system identifier is optional.
The application may still want to provide one, however, for use in error messages
and warnings, or to resolve relative output identifiers.

If the Result is not to be written to a file, the system identifier is optional.
The application may still want to provide one, however, for use in error messages
and warnings, or to resolve relative output identifiers.

getSystemId

```java
String
getSystemId()
```

Get the system identifier that was set with setSystemId.

**Returns:** The system identifier that was set with setSystemId,
or null if setSystemId was not called.

---

#### getSystemId

String

getSystemId()

Get the system identifier that was set with setSystemId.

---

