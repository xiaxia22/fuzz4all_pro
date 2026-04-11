# Class SAXResult

**Source:** `java.xml\javax\xml\transform\sax\SAXResult.html`

### Class Description

```java
public class
SAXResult

extends
Object

implements
Result
```

Acts as an holder for a transformation Result.

**All Implemented Interfaces:** Result

---

### Field Details

#### public static final
String
FEATURE

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Result output of this type.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public SAXResult()

Zero-argument default constructor.

---

#### public SAXResult​(
ContentHandler
handler)

Create a SAXResult that targets a SAX2

ContentHandler

.

**Parameters:**
- handler

- Must be a non-null ContentHandler reference.

---

### Method Details

#### public void setHandler​(
ContentHandler
handler)

Set the target to be a SAX2

ContentHandler

.

**Parameters:**
- handler

- Must be a non-null ContentHandler reference.

---

#### public
ContentHandler
getHandler()

Get the

ContentHandler

that is the Result.

**Returns:**
- The ContentHandler that is to be transformation output.

---

#### public void setLexicalHandler​(
LexicalHandler
handler)

Set the SAX2

LexicalHandler

for the output.

This is needed to handle XML comments and the like. If the
lexical handler is not set, an attempt should be made by the
transformer to cast the

ContentHandler

to a

LexicalHandler

.

**Parameters:**
- handler

- A non-null

LexicalHandler

for
handling lexical parse events.

---

#### public
LexicalHandler
getLexicalHandler()

Get a SAX2

LexicalHandler

for the output.

**Returns:**
- A

LexicalHandler

, or null.

---

#### public void setSystemId​(
String
systemId)

Method setSystemId Set the systemID that may be used in association
with the

ContentHandler

.

**Specified by:**
- setSystemId

in interface

Result

**Parameters:**
- systemId

- The system identifier as a URI string.

---

#### public
String
getSystemId()

Get the system identifier that was set with setSystemId.

**Specified by:**
- getSystemId

in interface

Result

**Returns:**
- The system identifier that was set with setSystemId, or null
if setSystemId was not called.

---

### Additional Sections

#### Class SAXResult

java.lang.Object

- javax.xml.transform.sax.SAXResult

javax.xml.transform.sax.SAXResult

**All Implemented Interfaces:** Result

```java
public class
SAXResult

extends
Object

implements
Result
```

Acts as an holder for a transformation Result.

**Since:** 1.4

public class

SAXResult

extends

Object

implements

Result

Acts as an holder for a transformation Result.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

FEATURE

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Result output of this type.

- Fields declared in interface javax.xml.transform.

Result

PI_DISABLE_OUTPUT_ESCAPING

,

PI_ENABLE_OUTPUT_ESCAPING

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SAXResult

()

Zero-argument default constructor.

SAXResult

​(

ContentHandler

handler)

Create a SAXResult that targets a SAX2

ContentHandler

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ContentHandler

getHandler

()

Get the

ContentHandler

that is the Result.

LexicalHandler

getLexicalHandler

()

Get a SAX2

LexicalHandler

for the output.

String

getSystemId

()

Get the system identifier that was set with setSystemId.

void

setHandler

​(

ContentHandler

handler)

Set the target to be a SAX2

ContentHandler

.

void

setLexicalHandler

​(

LexicalHandler

handler)

Set the SAX2

LexicalHandler

for the output.

void

setSystemId

​(

String

systemId)

Method setSystemId Set the systemID that may be used in association
with the

ContentHandler

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

Field Summary

Fields

Modifier and Type

Field

Description

static

String

FEATURE

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Result output of this type.

- Fields declared in interface javax.xml.transform.

Result

PI_DISABLE_OUTPUT_ESCAPING

,

PI_ENABLE_OUTPUT_ESCAPING

---

#### Field Summary

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Result output of this type.

Fields declared in interface javax.xml.transform.

Result

PI_DISABLE_OUTPUT_ESCAPING

,

PI_ENABLE_OUTPUT_ESCAPING

---

#### Fields declared in interface javax.xml.transform. Result

Constructor Summary

Constructors

Constructor

Description

SAXResult

()

Zero-argument default constructor.

SAXResult

​(

ContentHandler

handler)

Create a SAXResult that targets a SAX2

ContentHandler

.

---

#### Constructor Summary

Zero-argument default constructor.

Create a SAXResult that targets a SAX2

ContentHandler

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ContentHandler

getHandler

()

Get the

ContentHandler

that is the Result.

LexicalHandler

getLexicalHandler

()

Get a SAX2

LexicalHandler

for the output.

String

getSystemId

()

Get the system identifier that was set with setSystemId.

void

setHandler

​(

ContentHandler

handler)

Set the target to be a SAX2

ContentHandler

.

void

setLexicalHandler

​(

LexicalHandler

handler)

Set the SAX2

LexicalHandler

for the output.

void

setSystemId

​(

String

systemId)

Method setSystemId Set the systemID that may be used in association
with the

ContentHandler

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

Get the

ContentHandler

that is the Result.

Get a SAX2

LexicalHandler

for the output.

Get the system identifier that was set with setSystemId.

Set the target to be a SAX2

ContentHandler

.

Set the SAX2

LexicalHandler

for the output.

Method setSystemId Set the systemID that may be used in association
with the

ContentHandler

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

============ FIELD DETAIL ===========

- Field Detail

- FEATURE

```java
public static final
String
FEATURE
```

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Result output of this type.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SAXResult

```java
public SAXResult()
```

Zero-argument default constructor.

- SAXResult

```java
public SAXResult​(
ContentHandler
handler)
```

Create a SAXResult that targets a SAX2

ContentHandler

.

**Parameters:** handler

- Must be a non-null ContentHandler reference.

============ METHOD DETAIL ==========

- Method Detail

- setHandler

```java
public void setHandler​(
ContentHandler
handler)
```

Set the target to be a SAX2

ContentHandler

.

**Parameters:** handler

- Must be a non-null ContentHandler reference.

- getHandler

```java
public
ContentHandler
getHandler()
```

Get the

ContentHandler

that is the Result.

**Returns:** The ContentHandler that is to be transformation output.

- setLexicalHandler

```java
public void setLexicalHandler​(
LexicalHandler
handler)
```

Set the SAX2

LexicalHandler

for the output.

This is needed to handle XML comments and the like. If the
lexical handler is not set, an attempt should be made by the
transformer to cast the

ContentHandler

to a

LexicalHandler

.

**Parameters:** handler

- A non-null

LexicalHandler

for
handling lexical parse events.

- getLexicalHandler

```java
public
LexicalHandler
getLexicalHandler()
```

Get a SAX2

LexicalHandler

for the output.

**Returns:** A

LexicalHandler

, or null.

- setSystemId

```java
public void setSystemId​(
String
systemId)
```

Method setSystemId Set the systemID that may be used in association
with the

ContentHandler

.

**Specified by:** setSystemId

in interface

Result
**Parameters:** systemId

- The system identifier as a URI string.

- getSystemId

```java
public
String
getSystemId()
```

Get the system identifier that was set with setSystemId.

**Specified by:** getSystemId

in interface

Result
**Returns:** The system identifier that was set with setSystemId, or null
if setSystemId was not called.

Field Detail

- FEATURE

```java
public static final
String
FEATURE
```

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Result output of this type.

**See Also:** Constant Field Values

---

#### Field Detail

FEATURE

```java
public static final
String
FEATURE
```

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Result output of this type.

**See Also:** Constant Field Values

---

#### FEATURE

public static final

String

FEATURE

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Result output of this type.

Constructor Detail

- SAXResult

```java
public SAXResult()
```

Zero-argument default constructor.

- SAXResult

```java
public SAXResult​(
ContentHandler
handler)
```

Create a SAXResult that targets a SAX2

ContentHandler

.

**Parameters:** handler

- Must be a non-null ContentHandler reference.

---

#### Constructor Detail

SAXResult

```java
public SAXResult()
```

Zero-argument default constructor.

---

#### SAXResult

public SAXResult()

Zero-argument default constructor.

SAXResult

```java
public SAXResult​(
ContentHandler
handler)
```

Create a SAXResult that targets a SAX2

ContentHandler

.

**Parameters:** handler

- Must be a non-null ContentHandler reference.

---

#### SAXResult

public SAXResult​(

ContentHandler

handler)

Create a SAXResult that targets a SAX2

ContentHandler

.

Method Detail

- setHandler

```java
public void setHandler​(
ContentHandler
handler)
```

Set the target to be a SAX2

ContentHandler

.

**Parameters:** handler

- Must be a non-null ContentHandler reference.

- getHandler

```java
public
ContentHandler
getHandler()
```

Get the

ContentHandler

that is the Result.

**Returns:** The ContentHandler that is to be transformation output.

- setLexicalHandler

```java
public void setLexicalHandler​(
LexicalHandler
handler)
```

Set the SAX2

LexicalHandler

for the output.

This is needed to handle XML comments and the like. If the
lexical handler is not set, an attempt should be made by the
transformer to cast the

ContentHandler

to a

LexicalHandler

.

**Parameters:** handler

- A non-null

LexicalHandler

for
handling lexical parse events.

- getLexicalHandler

```java
public
LexicalHandler
getLexicalHandler()
```

Get a SAX2

LexicalHandler

for the output.

**Returns:** A

LexicalHandler

, or null.

- setSystemId

```java
public void setSystemId​(
String
systemId)
```

Method setSystemId Set the systemID that may be used in association
with the

ContentHandler

.

**Specified by:** setSystemId

in interface

Result
**Parameters:** systemId

- The system identifier as a URI string.

- getSystemId

```java
public
String
getSystemId()
```

Get the system identifier that was set with setSystemId.

**Specified by:** getSystemId

in interface

Result
**Returns:** The system identifier that was set with setSystemId, or null
if setSystemId was not called.

---

#### Method Detail

setHandler

```java
public void setHandler​(
ContentHandler
handler)
```

Set the target to be a SAX2

ContentHandler

.

**Parameters:** handler

- Must be a non-null ContentHandler reference.

---

#### setHandler

public void setHandler​(

ContentHandler

handler)

Set the target to be a SAX2

ContentHandler

.

getHandler

```java
public
ContentHandler
getHandler()
```

Get the

ContentHandler

that is the Result.

**Returns:** The ContentHandler that is to be transformation output.

---

#### getHandler

public

ContentHandler

getHandler()

Get the

ContentHandler

that is the Result.

setLexicalHandler

```java
public void setLexicalHandler​(
LexicalHandler
handler)
```

Set the SAX2

LexicalHandler

for the output.

This is needed to handle XML comments and the like. If the
lexical handler is not set, an attempt should be made by the
transformer to cast the

ContentHandler

to a

LexicalHandler

.

**Parameters:** handler

- A non-null

LexicalHandler

for
handling lexical parse events.

---

#### setLexicalHandler

public void setLexicalHandler​(

LexicalHandler

handler)

Set the SAX2

LexicalHandler

for the output.

This is needed to handle XML comments and the like. If the
lexical handler is not set, an attempt should be made by the
transformer to cast the

ContentHandler

to a

LexicalHandler

.

This is needed to handle XML comments and the like. If the
lexical handler is not set, an attempt should be made by the
transformer to cast the

ContentHandler

to a

LexicalHandler

.

getLexicalHandler

```java
public
LexicalHandler
getLexicalHandler()
```

Get a SAX2

LexicalHandler

for the output.

**Returns:** A

LexicalHandler

, or null.

---

#### getLexicalHandler

public

LexicalHandler

getLexicalHandler()

Get a SAX2

LexicalHandler

for the output.

setSystemId

```java
public void setSystemId​(
String
systemId)
```

Method setSystemId Set the systemID that may be used in association
with the

ContentHandler

.

**Specified by:** setSystemId

in interface

Result
**Parameters:** systemId

- The system identifier as a URI string.

---

#### setSystemId

public void setSystemId​(

String

systemId)

Method setSystemId Set the systemID that may be used in association
with the

ContentHandler

.

getSystemId

```java
public
String
getSystemId()
```

Get the system identifier that was set with setSystemId.

**Specified by:** getSystemId

in interface

Result
**Returns:** The system identifier that was set with setSystemId, or null
if setSystemId was not called.

---

#### getSystemId

public

String

getSystemId()

Get the system identifier that was set with setSystemId.

---

