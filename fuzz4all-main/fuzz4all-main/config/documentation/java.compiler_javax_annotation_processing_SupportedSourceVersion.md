# Annotation Type SupportedSourceVersion

**Source:** `java.compiler\javax\annotation\processing\SupportedSourceVersion.html`

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
SupportedSourceVersion
```

An annotation used to indicate the latest source version an
annotation processor supports. The

Processor.getSupportedSourceVersion()

method can construct its
result from the value of this annotation, as done by

AbstractProcessor.getSupportedSourceVersion()

.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### value

SourceVersion Returns the latest supported source version.

---

### Additional Sections

#### Annotation Type SupportedSourceVersion

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
SupportedSourceVersion
```

An annotation used to indicate the latest source version an
annotation processor supports. The

Processor.getSupportedSourceVersion()

method can construct its
result from the value of this annotation, as done by

AbstractProcessor.getSupportedSourceVersion()

.

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

SupportedSourceVersion

An annotation used to indicate the latest source version an
annotation processor supports. The

Processor.getSupportedSourceVersion()

method can construct its
result from the value of this annotation, as done by

AbstractProcessor.getSupportedSourceVersion()

.

=========== ANNOTATION TYPE REQUIRED MEMBER SUMMARY ===========

- Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

SourceVersion

value

Returns the latest supported source version.

Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

SourceVersion

value

Returns the latest supported source version.

---

#### Required Element Summary

Returns the latest supported source version.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
SourceVersion
value
```

Returns the latest supported source version.

**Returns:** the latest supported source version

Element Detail

- value

```java
SourceVersion
value
```

Returns the latest supported source version.

**Returns:** the latest supported source version

---

#### Element Detail

value

```java
SourceVersion
value
```

Returns the latest supported source version.

**Returns:** the latest supported source version

---

#### value

SourceVersion

value

Returns the latest supported source version.

---

