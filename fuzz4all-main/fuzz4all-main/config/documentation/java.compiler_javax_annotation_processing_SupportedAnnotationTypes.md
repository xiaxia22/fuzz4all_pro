# Annotation Type SupportedAnnotationTypes

**Source:** `java.compiler\javax\annotation\processing\SupportedAnnotationTypes.html`

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
SupportedAnnotationTypes
```

An annotation used to indicate what annotation types an annotation
processor supports. The

Processor.getSupportedAnnotationTypes()

method can construct its
result from the value of this annotation, as done by

AbstractProcessor.getSupportedAnnotationTypes()

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

String [] Returns the names of the supported annotation types.

---

### Additional Sections

#### Annotation Type SupportedAnnotationTypes

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
SupportedAnnotationTypes
```

An annotation used to indicate what annotation types an annotation
processor supports. The

Processor.getSupportedAnnotationTypes()

method can construct its
result from the value of this annotation, as done by

AbstractProcessor.getSupportedAnnotationTypes()

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

SupportedAnnotationTypes

An annotation used to indicate what annotation types an annotation
processor supports. The

Processor.getSupportedAnnotationTypes()

method can construct its
result from the value of this annotation, as done by

AbstractProcessor.getSupportedAnnotationTypes()

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

Returns the names of the supported annotation types.

Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

String

[]

value

Returns the names of the supported annotation types.

---

#### Required Element Summary

Returns the names of the supported annotation types.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
String
[] value
```

Returns the names of the supported annotation types.

**Returns:** the names of the supported annotation types

Element Detail

- value

```java
String
[] value
```

Returns the names of the supported annotation types.

**Returns:** the names of the supported annotation types

---

#### Element Detail

value

```java
String
[] value
```

Returns the names of the supported annotation types.

**Returns:** the names of the supported annotation types

---

#### value

String

[] value

Returns the names of the supported annotation types.

---

