# Annotation Type Override

**Source:** `java.base\java\lang\Override.html`

### Class Description

```java
@Target
(
METHOD
)

@Retention
(
SOURCE
)
public @interface
Override
```

Indicates that a method declaration is intended to override a
method declaration in a supertype. If a method is annotated with
this annotation type compilers are required to generate an error
message unless at least one of the following conditions hold:

- The method does override or implement a method declared in a
supertype.
- The method has a signature that is override-equivalent to that of
any public method declared in

Object

.

**Since:** 1.5
**See The Java™ Language Specification :** 8.4.8 Inheritance, Overriding, and Hiding, 9.4.1 Inheritance and Overriding, 9.6.4.4 @Override

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Annotation Type Override

```java
@Target
(
METHOD
)

@Retention
(
SOURCE
)
public @interface
Override
```

Indicates that a method declaration is intended to override a
method declaration in a supertype. If a method is annotated with
this annotation type compilers are required to generate an error
message unless at least one of the following conditions hold:

- The method does override or implement a method declared in a
supertype.
- The method has a signature that is override-equivalent to that of
any public method declared in

Object

.

**Since:** 1.5
**See The Java™ Language Specification :** 8.4.8 Inheritance, Overriding, and Hiding, 9.4.1 Inheritance and Overriding, 9.6.4.4 @Override

@Target

(

METHOD

)

@Retention

(

SOURCE

)
public @interface

Override

Indicates that a method declaration is intended to override a
method declaration in a supertype. If a method is annotated with
this annotation type compilers are required to generate an error
message unless at least one of the following conditions hold:

- The method does override or implement a method declared in a
supertype.
- The method has a signature that is override-equivalent to that of
any public method declared in

Object

.

The method does override or implement a method declared in a
supertype.

The method has a signature that is override-equivalent to that of
any public method declared in

Object

.

---

