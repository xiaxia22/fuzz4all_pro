# Interface Location

**Source:** `java.xml\javax\xml\stream\Location.html`

### Class Description

```java
public interface
Location
```

Provides information on the location of an event.

All the information provided by a Location is optional. For example
an application may only report line numbers.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getLineNumber()

Return the line number where the current event ends,
returns -1 if none is available.

**Returns:**
- the current line number

---

#### int getColumnNumber()

Return the column number where the current event ends,
returns -1 if none is available.

**Returns:**
- the current column number

---

#### int getCharacterOffset()

Return the byte or character offset into the input source this location
is pointing to. If the input source is a file or a byte stream then
this is the byte offset into that stream, but if the input source is
a character media then the offset is the character offset.
Returns -1 if there is no offset available.

**Returns:**
- the current offset

---

#### String
getPublicId()

Returns the public ID of the XML

**Returns:**
- the public ID, or null if not available

---

#### String
getSystemId()

Returns the system ID of the XML

**Returns:**
- the system ID, or null if not available

---

### Additional Sections

#### Interface Location

```java
public interface
Location
```

Provides information on the location of an event.

All the information provided by a Location is optional. For example
an application may only report line numbers.

**Since:** 1.6

public interface

Location

Provides information on the location of an event.

All the information provided by a Location is optional. For example
an application may only report line numbers.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getCharacterOffset

()

Return the byte or character offset into the input source this location
is pointing to.

int

getColumnNumber

()

Return the column number where the current event ends,
returns -1 if none is available.

int

getLineNumber

()

Return the line number where the current event ends,
returns -1 if none is available.

String

getPublicId

()

Returns the public ID of the XML

String

getSystemId

()

Returns the system ID of the XML

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getCharacterOffset

()

Return the byte or character offset into the input source this location
is pointing to.

int

getColumnNumber

()

Return the column number where the current event ends,
returns -1 if none is available.

int

getLineNumber

()

Return the line number where the current event ends,
returns -1 if none is available.

String

getPublicId

()

Returns the public ID of the XML

String

getSystemId

()

Returns the system ID of the XML

---

#### Method Summary

Return the byte or character offset into the input source this location
is pointing to.

Return the column number where the current event ends,
returns -1 if none is available.

Return the line number where the current event ends,
returns -1 if none is available.

Returns the public ID of the XML

Returns the system ID of the XML

============ METHOD DETAIL ==========

- Method Detail

- getLineNumber

```java
int getLineNumber()
```

Return the line number where the current event ends,
returns -1 if none is available.

**Returns:** the current line number

- getColumnNumber

```java
int getColumnNumber()
```

Return the column number where the current event ends,
returns -1 if none is available.

**Returns:** the current column number

- getCharacterOffset

```java
int getCharacterOffset()
```

Return the byte or character offset into the input source this location
is pointing to. If the input source is a file or a byte stream then
this is the byte offset into that stream, but if the input source is
a character media then the offset is the character offset.
Returns -1 if there is no offset available.

**Returns:** the current offset

- getPublicId

```java
String
getPublicId()
```

Returns the public ID of the XML

**Returns:** the public ID, or null if not available

- getSystemId

```java
String
getSystemId()
```

Returns the system ID of the XML

**Returns:** the system ID, or null if not available

Method Detail

- getLineNumber

```java
int getLineNumber()
```

Return the line number where the current event ends,
returns -1 if none is available.

**Returns:** the current line number

- getColumnNumber

```java
int getColumnNumber()
```

Return the column number where the current event ends,
returns -1 if none is available.

**Returns:** the current column number

- getCharacterOffset

```java
int getCharacterOffset()
```

Return the byte or character offset into the input source this location
is pointing to. If the input source is a file or a byte stream then
this is the byte offset into that stream, but if the input source is
a character media then the offset is the character offset.
Returns -1 if there is no offset available.

**Returns:** the current offset

- getPublicId

```java
String
getPublicId()
```

Returns the public ID of the XML

**Returns:** the public ID, or null if not available

- getSystemId

```java
String
getSystemId()
```

Returns the system ID of the XML

**Returns:** the system ID, or null if not available

---

#### Method Detail

getLineNumber

```java
int getLineNumber()
```

Return the line number where the current event ends,
returns -1 if none is available.

**Returns:** the current line number

---

#### getLineNumber

int getLineNumber()

Return the line number where the current event ends,
returns -1 if none is available.

getColumnNumber

```java
int getColumnNumber()
```

Return the column number where the current event ends,
returns -1 if none is available.

**Returns:** the current column number

---

#### getColumnNumber

int getColumnNumber()

Return the column number where the current event ends,
returns -1 if none is available.

getCharacterOffset

```java
int getCharacterOffset()
```

Return the byte or character offset into the input source this location
is pointing to. If the input source is a file or a byte stream then
this is the byte offset into that stream, but if the input source is
a character media then the offset is the character offset.
Returns -1 if there is no offset available.

**Returns:** the current offset

---

#### getCharacterOffset

int getCharacterOffset()

Return the byte or character offset into the input source this location
is pointing to. If the input source is a file or a byte stream then
this is the byte offset into that stream, but if the input source is
a character media then the offset is the character offset.
Returns -1 if there is no offset available.

getPublicId

```java
String
getPublicId()
```

Returns the public ID of the XML

**Returns:** the public ID, or null if not available

---

#### getPublicId

String

getPublicId()

Returns the public ID of the XML

getSystemId

```java
String
getSystemId()
```

Returns the system ID of the XML

**Returns:** the system ID, or null if not available

---

#### getSystemId

String

getSystemId()

Returns the system ID of the XML

---

