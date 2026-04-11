# Annotation Type Target

**Source:** `java.base\java\lang\annotation\Target.html`

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
Target
```

Indicates the contexts in which an annotation type is applicable. The
declaration contexts and type contexts in which an annotation type may be
applicable are specified in JLS 9.6.4.1, and denoted in source code by enum
constants of

java.lang.annotation.ElementType

.

If an

@Target

meta-annotation is not present on an annotation type

T

, then an annotation of type

T

may be written as a
modifier for any declaration except a type parameter declaration.

If an

@Target

meta-annotation is present, the compiler will enforce
the usage restrictions indicated by

ElementType

enum constants, in line with JLS 9.7.4.

For example, this

@Target

meta-annotation indicates that the
declared type is itself a meta-annotation type. It can only be used on
annotation type declarations:

```java
@Target(ElementType.ANNOTATION_TYPE)
public @interface MetaAnnotationType {
...
}
```

This

@Target

meta-annotation indicates that the declared type is
intended solely for use as a member type in complex annotation type
declarations. It cannot be used to annotate anything directly:

```java
@Target({})
public @interface MemberType {
...
}
```

It is a compile-time error for a single

ElementType

constant to
appear more than once in an

@Target

annotation. For example, the
following

@Target

meta-annotation is illegal:

```java
@Target({ElementType.FIELD, ElementType.METHOD, ElementType.FIELD})
public @interface Bogus {
...
}
```

**Since:** 1.5
**See The Java™ Language Specification :** 9.6.4.1 @Target, 9.7.4 Where Annotations May Appear, 9.7.5 Multiple Annotations of the Same Type

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### value

ElementType [] Returns an array of the kinds of elements an annotation type
can be applied to.

---

### Additional Sections

#### Annotation Type Target

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
Target
```

Indicates the contexts in which an annotation type is applicable. The
declaration contexts and type contexts in which an annotation type may be
applicable are specified in JLS 9.6.4.1, and denoted in source code by enum
constants of

java.lang.annotation.ElementType

.

If an

@Target

meta-annotation is not present on an annotation type

T

, then an annotation of type

T

may be written as a
modifier for any declaration except a type parameter declaration.

If an

@Target

meta-annotation is present, the compiler will enforce
the usage restrictions indicated by

ElementType

enum constants, in line with JLS 9.7.4.

For example, this

@Target

meta-annotation indicates that the
declared type is itself a meta-annotation type. It can only be used on
annotation type declarations:

```java
@Target(ElementType.ANNOTATION_TYPE)
public @interface MetaAnnotationType {
...
}
```

This

@Target

meta-annotation indicates that the declared type is
intended solely for use as a member type in complex annotation type
declarations. It cannot be used to annotate anything directly:

```java
@Target({})
public @interface MemberType {
...
}
```

It is a compile-time error for a single

ElementType

constant to
appear more than once in an

@Target

annotation. For example, the
following

@Target

meta-annotation is illegal:

```java
@Target({ElementType.FIELD, ElementType.METHOD, ElementType.FIELD})
public @interface Bogus {
...
}
```

**Since:** 1.5
**See The Java™ Language Specification :** 9.6.4.1 @Target, 9.7.4 Where Annotations May Appear, 9.7.5 Multiple Annotations of the Same Type

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

Target

Indicates the contexts in which an annotation type is applicable. The
declaration contexts and type contexts in which an annotation type may be
applicable are specified in JLS 9.6.4.1, and denoted in source code by enum
constants of

java.lang.annotation.ElementType

.

If an

@Target

meta-annotation is not present on an annotation type

T

, then an annotation of type

T

may be written as a
modifier for any declaration except a type parameter declaration.

If an

@Target

meta-annotation is present, the compiler will enforce
the usage restrictions indicated by

ElementType

enum constants, in line with JLS 9.7.4.

For example, this

@Target

meta-annotation indicates that the
declared type is itself a meta-annotation type. It can only be used on
annotation type declarations:

```java
@Target(ElementType.ANNOTATION_TYPE)
public @interface MetaAnnotationType {
...
}
```

This

@Target

meta-annotation indicates that the declared type is
intended solely for use as a member type in complex annotation type
declarations. It cannot be used to annotate anything directly:

```java
@Target({})
public @interface MemberType {
...
}
```

It is a compile-time error for a single

ElementType

constant to
appear more than once in an

@Target

annotation. For example, the
following

@Target

meta-annotation is illegal:

```java
@Target({ElementType.FIELD, ElementType.METHOD, ElementType.FIELD})
public @interface Bogus {
...
}
```

If an

@Target

meta-annotation is not present on an annotation type

T

, then an annotation of type

T

may be written as a
modifier for any declaration except a type parameter declaration.

If an

@Target

meta-annotation is present, the compiler will enforce
the usage restrictions indicated by

ElementType

enum constants, in line with JLS 9.7.4.

For example, this

@Target

meta-annotation indicates that the
declared type is itself a meta-annotation type. It can only be used on
annotation type declarations:

```java
@Target(ElementType.ANNOTATION_TYPE)
public @interface MetaAnnotationType {
...
}
```

This

@Target

meta-annotation indicates that the declared type is
intended solely for use as a member type in complex annotation type
declarations. It cannot be used to annotate anything directly:

```java
@Target({})
public @interface MemberType {
...
}
```

It is a compile-time error for a single

ElementType

constant to
appear more than once in an

@Target

annotation. For example, the
following

@Target

meta-annotation is illegal:

```java
@Target({ElementType.FIELD, ElementType.METHOD, ElementType.FIELD})
public @interface Bogus {
...
}
```

If an

@Target

meta-annotation is present, the compiler will enforce
the usage restrictions indicated by

ElementType

enum constants, in line with JLS 9.7.4.

For example, this

@Target

meta-annotation indicates that the
declared type is itself a meta-annotation type. It can only be used on
annotation type declarations:

```java
@Target(ElementType.ANNOTATION_TYPE)
public @interface MetaAnnotationType {
...
}
```

This

@Target

meta-annotation indicates that the declared type is
intended solely for use as a member type in complex annotation type
declarations. It cannot be used to annotate anything directly:

```java
@Target({})
public @interface MemberType {
...
}
```

It is a compile-time error for a single

ElementType

constant to
appear more than once in an

@Target

annotation. For example, the
following

@Target

meta-annotation is illegal:

```java
@Target({ElementType.FIELD, ElementType.METHOD, ElementType.FIELD})
public @interface Bogus {
...
}
```

For example, this

@Target

meta-annotation indicates that the
declared type is itself a meta-annotation type. It can only be used on
annotation type declarations:

```java
@Target(ElementType.ANNOTATION_TYPE)
public @interface MetaAnnotationType {
...
}
```

This

@Target

meta-annotation indicates that the declared type is
intended solely for use as a member type in complex annotation type
declarations. It cannot be used to annotate anything directly:

```java
@Target({})
public @interface MemberType {
...
}
```

It is a compile-time error for a single

ElementType

constant to
appear more than once in an

@Target

annotation. For example, the
following

@Target

meta-annotation is illegal:

```java
@Target({ElementType.FIELD, ElementType.METHOD, ElementType.FIELD})
public @interface Bogus {
...
}
```

@Target(ElementType.ANNOTATION_TYPE)
public @interface MetaAnnotationType {
...
}

This

@Target

meta-annotation indicates that the declared type is
intended solely for use as a member type in complex annotation type
declarations. It cannot be used to annotate anything directly:

```java
@Target({})
public @interface MemberType {
...
}
```

It is a compile-time error for a single

ElementType

constant to
appear more than once in an

@Target

annotation. For example, the
following

@Target

meta-annotation is illegal:

```java
@Target({ElementType.FIELD, ElementType.METHOD, ElementType.FIELD})
public @interface Bogus {
...
}
```

@Target({})
public @interface MemberType {
...
}

It is a compile-time error for a single

ElementType

constant to
appear more than once in an

@Target

annotation. For example, the
following

@Target

meta-annotation is illegal:

```java
@Target({ElementType.FIELD, ElementType.METHOD, ElementType.FIELD})
public @interface Bogus {
...
}
```

@Target({ElementType.FIELD, ElementType.METHOD, ElementType.FIELD})
public @interface Bogus {
...
}

=========== ANNOTATION TYPE REQUIRED MEMBER SUMMARY ===========

- Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

ElementType

[]

value

Returns an array of the kinds of elements an annotation type
can be applied to.

Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

ElementType

[]

value

Returns an array of the kinds of elements an annotation type
can be applied to.

---

#### Required Element Summary

Returns an array of the kinds of elements an annotation type
can be applied to.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
ElementType
[] value
```

Returns an array of the kinds of elements an annotation type
can be applied to.

**Returns:** an array of the kinds of elements an annotation type
can be applied to

Element Detail

- value

```java
ElementType
[] value
```

Returns an array of the kinds of elements an annotation type
can be applied to.

**Returns:** an array of the kinds of elements an annotation type
can be applied to

---

#### Element Detail

value

```java
ElementType
[] value
```

Returns an array of the kinds of elements an annotation type
can be applied to.

**Returns:** an array of the kinds of elements an annotation type
can be applied to

---

#### value

ElementType

[] value

Returns an array of the kinds of elements an annotation type
can be applied to.

---

