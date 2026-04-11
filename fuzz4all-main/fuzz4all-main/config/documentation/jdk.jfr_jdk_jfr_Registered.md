# Annotation Type Registered

**Source:** `jdk.jfr\jdk\jfr\Registered.html`

### Class Description

```java
@Target
(
TYPE
)

@Inherited

@Retention
(
RUNTIME
)
public @interface
Registered
```

Event annotation, for programmatic event registration.

Events are automatically registered when they are first used. This annotation
can be used to override that registration. To register
events programmatically, use

FlightRecorder.register(Class)

.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### value

boolean Returns true if the event is to be registered when the event class is
first used, false otherwise.

---

### Additional Sections

#### Annotation Type Registered

```java
@Target
(
TYPE
)

@Inherited

@Retention
(
RUNTIME
)
public @interface
Registered
```

Event annotation, for programmatic event registration.

Events are automatically registered when they are first used. This annotation
can be used to override that registration. To register
events programmatically, use

FlightRecorder.register(Class)

.

**Since:** 9

@Target

(

TYPE

)

@Inherited

@Retention

(

RUNTIME

)
public @interface

Registered

Event annotation, for programmatic event registration.

Events are automatically registered when they are first used. This annotation
can be used to override that registration. To register
events programmatically, use

FlightRecorder.register(Class)

.

Events are automatically registered when they are first used. This annotation
can be used to override that registration. To register
events programmatically, use

FlightRecorder.register(Class)

.

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

if the event is to be registered when the event class is
first used,

false

otherwise.

Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

boolean

value

Returns

true

if the event is to be registered when the event class is
first used,

false

otherwise.

---

#### Optional Element Summary

Returns

true

if the event is to be registered when the event class is
first used,

false

otherwise.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
boolean value
```

Returns

true

if the event is to be registered when the event class is
first used,

false

otherwise.

**Returns:** true

if the event is to be registered when the event class is
first used,

false

otherwise.

**Default:** true

Element Detail

- value

```java
boolean value
```

Returns

true

if the event is to be registered when the event class is
first used,

false

otherwise.

**Returns:** true

if the event is to be registered when the event class is
first used,

false

otherwise.

**Default:** true

---

#### Element Detail

value

```java
boolean value
```

Returns

true

if the event is to be registered when the event class is
first used,

false

otherwise.

**Returns:** true

if the event is to be registered when the event class is
first used,

false

otherwise.

**Default:** true

---

#### value

boolean value

Returns

true

if the event is to be registered when the event class is
first used,

false

otherwise.

---

