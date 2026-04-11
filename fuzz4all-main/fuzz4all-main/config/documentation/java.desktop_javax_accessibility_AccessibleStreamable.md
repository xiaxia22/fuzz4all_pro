# Interface AccessibleStreamable

**Source:** `java.desktop\javax\accessibility\AccessibleStreamable.html`

### Class Description

```java
public interface
AccessibleStreamable
```

The

AccessibleStreamable

interface should be implemented by the

AccessibleContext

of any component that presents the raw stream
behind a component on the display screen. Examples of such components are
HTML, bitmap images and MathML. An object that implements

AccessibleStreamable

provides two things: a list of MIME types
supported by the object and a streaming interface for each MIME type to get
the data.

**Since:** 1.5
**See Also:** AccessibleContext

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### DataFlavor
[] getMimeTypes()

Returns an array of

DataFlavor

objects for the MIME types this
object supports.

**Returns:**
- an array of

DataFlavor

objects for the MIME types this
object supports

---

#### InputStream
getStream​(
DataFlavor
flavor)

Returns an

InputStream

for a

DataFlavor

.

**Parameters:**
- flavor

- the

DataFlavor

**Returns:**
- an

ImputStream

if an input stream for this

DataFlavor

exists. Otherwise,

null

is returned.

---

### Additional Sections

#### Interface AccessibleStreamable

```java
public interface
AccessibleStreamable
```

The

AccessibleStreamable

interface should be implemented by the

AccessibleContext

of any component that presents the raw stream
behind a component on the display screen. Examples of such components are
HTML, bitmap images and MathML. An object that implements

AccessibleStreamable

provides two things: a list of MIME types
supported by the object and a streaming interface for each MIME type to get
the data.

**Since:** 1.5
**See Also:** AccessibleContext

public interface

AccessibleStreamable

The

AccessibleStreamable

interface should be implemented by the

AccessibleContext

of any component that presents the raw stream
behind a component on the display screen. Examples of such components are
HTML, bitmap images and MathML. An object that implements

AccessibleStreamable

provides two things: a list of MIME types
supported by the object and a streaming interface for each MIME type to get
the data.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

DataFlavor

[]

getMimeTypes

()

Returns an array of

DataFlavor

objects for the MIME types this
object supports.

InputStream

getStream

​(

DataFlavor

flavor)

Returns an

InputStream

for a

DataFlavor

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

DataFlavor

[]

getMimeTypes

()

Returns an array of

DataFlavor

objects for the MIME types this
object supports.

InputStream

getStream

​(

DataFlavor

flavor)

Returns an

InputStream

for a

DataFlavor

.

---

#### Method Summary

Returns an array of

DataFlavor

objects for the MIME types this
object supports.

Returns an

InputStream

for a

DataFlavor

.

============ METHOD DETAIL ==========

- Method Detail

- getMimeTypes

```java
DataFlavor
[] getMimeTypes()
```

Returns an array of

DataFlavor

objects for the MIME types this
object supports.

**Returns:** an array of

DataFlavor

objects for the MIME types this
object supports

- getStream

```java
InputStream
getStream​(
DataFlavor
flavor)
```

Returns an

InputStream

for a

DataFlavor

.

**Parameters:** flavor

- the

DataFlavor
**Returns:** an

ImputStream

if an input stream for this

DataFlavor

exists. Otherwise,

null

is returned.

Method Detail

- getMimeTypes

```java
DataFlavor
[] getMimeTypes()
```

Returns an array of

DataFlavor

objects for the MIME types this
object supports.

**Returns:** an array of

DataFlavor

objects for the MIME types this
object supports

- getStream

```java
InputStream
getStream​(
DataFlavor
flavor)
```

Returns an

InputStream

for a

DataFlavor

.

**Parameters:** flavor

- the

DataFlavor
**Returns:** an

ImputStream

if an input stream for this

DataFlavor

exists. Otherwise,

null

is returned.

---

#### Method Detail

getMimeTypes

```java
DataFlavor
[] getMimeTypes()
```

Returns an array of

DataFlavor

objects for the MIME types this
object supports.

**Returns:** an array of

DataFlavor

objects for the MIME types this
object supports

---

#### getMimeTypes

DataFlavor

[] getMimeTypes()

Returns an array of

DataFlavor

objects for the MIME types this
object supports.

getStream

```java
InputStream
getStream​(
DataFlavor
flavor)
```

Returns an

InputStream

for a

DataFlavor

.

**Parameters:** flavor

- the

DataFlavor
**Returns:** an

ImputStream

if an input stream for this

DataFlavor

exists. Otherwise,

null

is returned.

---

#### getStream

InputStream

getStream​(

DataFlavor

flavor)

Returns an

InputStream

for a

DataFlavor

.

---

