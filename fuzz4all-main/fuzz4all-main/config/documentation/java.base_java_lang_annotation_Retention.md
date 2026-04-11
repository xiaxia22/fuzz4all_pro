# Annotation Type Retention

**Source:** `java.base\java\lang\annotation\Retention.html`

### Class Description

```java
@Documented

@Retention
(
RUNTIME
)

@Target
(
ANNOTATION_TYPE
)
public @interface
Retention
```

Indicates how long annotations with the annotated type are to
be retained. If no Retention annotation is present on
an annotation type declaration, the retention policy defaults to

RetentionPolicy.CLASS

.

A Retention meta-annotation has effect only if the
meta-annotated type is used directly for annotation. It has no
effect if the meta-annotated type is used as a member type in
another annotation type.

**Since:** 1.5
**See The Java™ Language Specification :** 9.6.4.2 @Retention

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### value

RetentionPolicy Returns the retention policy.

---

### Additional Sections

#### Annotation Type Retention

```java
@Documented

@Retention
(
RUNTIME
)

@Target
(
ANNOTATION_TYPE
)
public @interface
Retention
```

Indicates how long annotations with the annotated type are to
be retained. If no Retention annotation is present on
an annotation type declaration, the retention policy defaults to

RetentionPolicy.CLASS

.

A Retention meta-annotation has effect only if the
meta-annotated type is used directly for annotation. It has no
effect if the meta-annotated type is used as a member type in
another annotation type.

**Since:** 1.5
**See The Java™ Language Specification :** 9.6.4.2 @Retention

@Documented

@Retention

(

RUNTIME

)

@Target

(

ANNOTATION_TYPE

)
public @interface

Retention

Indicates how long annotations with the annotated type are to
be retained. If no Retention annotation is present on
an annotation type declaration, the retention policy defaults to

RetentionPolicy.CLASS

.

A Retention meta-annotation has effect only if the
meta-annotated type is used directly for annotation. It has no
effect if the meta-annotated type is used as a member type in
another annotation type.

A Retention meta-annotation has effect only if the
meta-annotated type is used directly for annotation. It has no
effect if the meta-annotated type is used as a member type in
another annotation type.

=========== ANNOTATION TYPE REQUIRED MEMBER SUMMARY ===========

- Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

RetentionPolicy

value

Returns the retention policy.

Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

RetentionPolicy

value

Returns the retention policy.

---

#### Required Element Summary

Returns the retention policy.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
RetentionPolicy
value
```

Returns the retention policy.

**Returns:** the retention policy

Element Detail

- value

```java
RetentionPolicy
value
```

Returns the retention policy.

**Returns:** the retention policy

---

#### Element Detail

value

```java
RetentionPolicy
value
```

Returns the retention policy.

**Returns:** the retention policy

---

#### value

RetentionPolicy

value

Returns the retention policy.

---

