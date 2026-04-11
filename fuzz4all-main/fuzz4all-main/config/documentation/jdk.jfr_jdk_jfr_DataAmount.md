# Annotation Type DataAmount

**Source:** `jdk.jfr\jdk\jfr\DataAmount.html`

### Class Description

```java
@Retention
(
RUNTIME
)

@Target
({
FIELD
,
TYPE
,
METHOD
})
public @interface
DataAmount
```

Event field annotation, specifies that a value represents an amount of data (for example, bytes).

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### BITS

static String Unit for bits

---

#### BYTES

static String Unit for bytes

---

#### value

String Returns the unit for the data amount, by default bytes.

---

### Additional Sections

#### Annotation Type DataAmount

```java
@Retention
(
RUNTIME
)

@Target
({
FIELD
,
TYPE
,
METHOD
})
public @interface
DataAmount
```

Event field annotation, specifies that a value represents an amount of data (for example, bytes).

**Since:** 9

@Retention

(

RUNTIME

)

@Target

({

FIELD

,

TYPE

,

METHOD

})
public @interface

DataAmount

Event field annotation, specifies that a value represents an amount of data (for example, bytes).

=========== ANNOTATION TYPE FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Fields

Description

static

String

BITS

Unit for bits

static

String

BYTES

Unit for bytes

=========== ANNOTATION TYPE OPTIONAL MEMBER SUMMARY ===========

- Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

String

value

Returns the unit for the data amount, by default bytes.

Field Summary

Fields

Modifier and Type

Fields

Description

static

String

BITS

Unit for bits

static

String

BYTES

Unit for bytes

---

#### Field Summary

Unit for bits

Unit for bytes

Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

String

value

Returns the unit for the data amount, by default bytes.

---

#### Optional Element Summary

Returns the unit for the data amount, by default bytes.

============ ANNOTATION TYPE FIELD DETAIL ===========

- Field Detail

- BITS

```java
static final
String
BITS
```

Unit for bits

- - BYTES

```java
static final
String
BYTES
```

Unit for bytes

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
String
value
```

Returns the unit for the data amount, by default bytes.

**Returns:** the data amount unit, default

BYTES

, not

null

**Default:** "BYTES"

Field Detail

- BITS

```java
static final
String
BITS
```

Unit for bits

---

#### Field Detail

BITS

```java
static final
String
BITS
```

Unit for bits

---

#### BITS

static final

String

BITS

Unit for bits

- BYTES

```java
static final
String
BYTES
```

Unit for bytes

BYTES

```java
static final
String
BYTES
```

Unit for bytes

---

#### BYTES

static final

String

BYTES

Unit for bytes

Element Detail

- value

```java
String
value
```

Returns the unit for the data amount, by default bytes.

**Returns:** the data amount unit, default

BYTES

, not

null

**Default:** "BYTES"

---

#### Element Detail

value

```java
String
value
```

Returns the unit for the data amount, by default bytes.

**Returns:** the data amount unit, default

BYTES

, not

null

**Default:** "BYTES"

---

#### value

String

value

Returns the unit for the data amount, by default bytes.

---

