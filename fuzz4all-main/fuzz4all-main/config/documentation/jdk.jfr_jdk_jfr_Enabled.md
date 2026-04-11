# Annotation Type Enabled

**Source:** `jdk.jfr\jdk\jfr\Enabled.html`

### Class Description

```java
@Target
(
TYPE
)

@Retention
(
RUNTIME
)

@Inherited

public @interface
Enabled
```

Event annotation, determines if an event should be enabled by default.

If an event doesn't have the annotation, then by default the event is enabled.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### NAME

static String Setting name "enabled" , signifies that the event should be
recorded.

---

#### value

boolean Returns true if by default the event should be enabled, false otherwise.

---

### Additional Sections

#### Annotation Type Enabled

```java
@Target
(
TYPE
)

@Retention
(
RUNTIME
)

@Inherited

public @interface
Enabled
```

Event annotation, determines if an event should be enabled by default.

If an event doesn't have the annotation, then by default the event is enabled.

**Since:** 9

@Target

(

TYPE

)

@Retention

(

RUNTIME

)

@Inherited

public @interface

Enabled

Event annotation, determines if an event should be enabled by default.

If an event doesn't have the annotation, then by default the event is enabled.

If an event doesn't have the annotation, then by default the event is enabled.

=========== ANNOTATION TYPE FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Fields

Description

static

String

NAME

Setting name

"enabled"

, signifies that the event should be
recorded.

=========== ANNOTATION TYPE OPTIONAL MEMBER SUMMARY ===========

- Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

boolean

value

Returns

true

if by default the event should be enabled,

false

otherwise.

Field Summary

Fields

Modifier and Type

Fields

Description

static

String

NAME

Setting name

"enabled"

, signifies that the event should be
recorded.

---

#### Field Summary

Setting name

"enabled"

, signifies that the event should be
recorded.

Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

boolean

value

Returns

true

if by default the event should be enabled,

false

otherwise.

---

#### Optional Element Summary

Returns

true

if by default the event should be enabled,

false

otherwise.

============ ANNOTATION TYPE FIELD DETAIL ===========

- Field Detail

- NAME

```java
static final
String
NAME
```

Setting name

"enabled"

, signifies that the event should be
recorded.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
boolean value
```

Returns

true

if by default the event should be enabled,

false

otherwise.

**Returns:** true

if by default the event should be enabled by default,

false

otherwise

**Default:** true

Field Detail

- NAME

```java
static final
String
NAME
```

Setting name

"enabled"

, signifies that the event should be
recorded.

---

#### Field Detail

NAME

```java
static final
String
NAME
```

Setting name

"enabled"

, signifies that the event should be
recorded.

---

#### NAME

static final

String

NAME

Setting name

"enabled"

, signifies that the event should be
recorded.

Element Detail

- value

```java
boolean value
```

Returns

true

if by default the event should be enabled,

false

otherwise.

**Returns:** true

if by default the event should be enabled by default,

false

otherwise

**Default:** true

---

#### Element Detail

value

```java
boolean value
```

Returns

true

if by default the event should be enabled,

false

otherwise.

**Returns:** true

if by default the event should be enabled by default,

false

otherwise

**Default:** true

---

#### value

boolean value

Returns

true

if by default the event should be enabled,

false

otherwise.

---

