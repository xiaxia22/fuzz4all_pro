# Annotation Type SupportedOptions

**Source:** `java.compiler\javax\annotation\processing\SupportedOptions.html`

### Class Description

```java
@Documented

@Target
(
TYPE
)

@Retention
(
RUNTIME
)
public @interface
SupportedOptions
```

An annotation used to indicate what options an annotation processor
supports. The

Processor.getSupportedOptions()

method can
construct its result from the value of this annotation, as done by

AbstractProcessor.getSupportedOptions()

. Only

strings conforming to the
grammar

should be used as values.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### value

String [] Returns the supported options.

---

### Additional Sections

#### Annotation Type SupportedOptions

```java
@Documented

@Target
(
TYPE
)

@Retention
(
RUNTIME
)
public @interface
SupportedOptions
```

An annotation used to indicate what options an annotation processor
supports. The

Processor.getSupportedOptions()

method can
construct its result from the value of this annotation, as done by

AbstractProcessor.getSupportedOptions()

. Only

strings conforming to the
grammar

should be used as values.

**Since:** 1.6

@Documented

@Target

(

TYPE

)

@Retention

(

RUNTIME

)
public @interface

SupportedOptions

An annotation used to indicate what options an annotation processor
supports. The

Processor.getSupportedOptions()

method can
construct its result from the value of this annotation, as done by

AbstractProcessor.getSupportedOptions()

. Only

strings conforming to the
grammar

should be used as values.

=========== ANNOTATION TYPE REQUIRED MEMBER SUMMARY ===========

- Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

String

[]

value

Returns the supported options.

Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

String

[]

value

Returns the supported options.

---

#### Required Element Summary

Returns the supported options.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
String
[] value
```

Returns the supported options.

**Returns:** the supported options

Element Detail

- value

```java
String
[] value
```

Returns the supported options.

**Returns:** the supported options

---

#### Element Detail

value

```java
String
[] value
```

Returns the supported options.

**Returns:** the supported options

---

#### value

String

[] value

Returns the supported options.

---

