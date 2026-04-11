# Interface ModuleElement

**Source:** `java.compiler\javax\lang\model\element\ModuleElement.html`

### Class Description

```java
public interface
ModuleElement

extends
Element
,
QualifiedNameable
```

Represents a module program element. Provides access to
information about the module, its directives, and its members.

**All Superinterfaces:** AnnotatedConstruct

,

Element

,

QualifiedNameable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Name
getQualifiedName()

Returns the fully qualified name of this module. For an

unnamed module

, an empty name is returned.

**Specified by:**
- getQualifiedName

in interface

QualifiedNameable

**Returns:**
- the fully qualified name of this module, or an
empty name if this is an unnamed module

**API Note:**
- If the module name consists of one identifier, then
this method returns that identifier, which is deemed to be
module's fully qualified name despite not being in qualified
form. If the module name consists of more than one identifier,
then this method returns the entire name.

**See The Java™ Language Specification :**
- 6.2 Names and Identifiers

---

#### Name
getSimpleName()

Returns the simple name of this module. For an

unnamed module

, an empty name is returned.

**Specified by:**
- getSimpleName

in interface

Element

**Returns:**
- the simple name of this module or an empty name if
this is an unnamed module

**See Also:**
- PackageElement.getSimpleName()

,

ExecutableElement.getSimpleName()

,

TypeElement.getSimpleName()

,

VariableElement.getSimpleName()

,

getSimpleName()

**API Note:**
- If the module name consists of one identifier, then
this method returns that identifier. If the module name
consists of more than one identifier, then this method returns
the rightmost such identifier, which is deemed to be the
module's simple name.

**See The Java™ Language Specification :**
- 6.2 Names and Identifiers

---

#### List
<? extends
Element
> getEnclosedElements()

Returns the packages within this module.

**Specified by:**
- getEnclosedElements

in interface

Element

**Returns:**
- the packages within this module

**See Also:**
- TypeElement.getEnclosedElements()

,

PackageElement.getEnclosedElements()

,

getEnclosedElements()

,

Elements.getAllMembers(javax.lang.model.element.TypeElement)

---

#### boolean isOpen()

Returns

true

if this is an open module and

false

otherwise.

**Returns:**
- true

if this is an open module and

false

otherwise

---

#### boolean isUnnamed()

Returns

true

if this is an unnamed module and

false

otherwise.

**Returns:**
- true

if this is an unnamed module and

false

otherwise

**See The Java™ Language Specification :**
- 7.7.5 Unnamed Modules

---

#### Element
getEnclosingElement()

Returns

null

since a module is not enclosed by another
element.

**Specified by:**
- getEnclosingElement

in interface

Element

**Returns:**
- null

**See Also:**
- Elements.getPackageOf(javax.lang.model.element.Element)

---

#### List
<? extends
ModuleElement.Directive
> getDirectives()

Returns the directives contained in the declaration of this module.

**Returns:**
- the directives in the declaration of this module

---

### Additional Sections

#### Interface ModuleElement

**All Superinterfaces:** AnnotatedConstruct

,

Element

,

QualifiedNameable

```java
public interface
ModuleElement

extends
Element
,
QualifiedNameable
```

Represents a module program element. Provides access to
information about the module, its directives, and its members.

**Since:** 9
**See Also:** Elements.getModuleOf(javax.lang.model.element.Element)
**See The Java™ Language Specification :** 7.7 Module Declarations

public interface

ModuleElement

extends

Element

,

QualifiedNameable

Represents a module program element. Provides access to
information about the module, its directives, and its members.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

ModuleElement.Directive

Represents a directive within the declaration of this
module.

static class

ModuleElement.DirectiveKind

The

kind

of a directive.

static interface

ModuleElement.DirectiveVisitor

<

R

,​

P

>

A visitor of module directives, in the style of the visitor design
pattern.

static interface

ModuleElement.ExportsDirective

An exported package of a module.

static interface

ModuleElement.OpensDirective

An opened package of a module.

static interface

ModuleElement.ProvidesDirective

An implementation of a service provided by a module.

static interface

ModuleElement.RequiresDirective

A dependency of a module.

static interface

ModuleElement.UsesDirective

A reference to a service used by a module.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<? extends

ModuleElement.Directive

>

getDirectives

()

Returns the directives contained in the declaration of this module.

List

<? extends

Element

>

getEnclosedElements

()

Returns the packages within this module.

Element

getEnclosingElement

()

Returns

null

since a module is not enclosed by another
element.

Name

getQualifiedName

()

Returns the fully qualified name of this module.

Name

getSimpleName

()

Returns the simple name of this module.

boolean

isOpen

()

Returns

true

if this is an open module and

false

otherwise.

boolean

isUnnamed

()

Returns

true

if this is an unnamed module and

false

otherwise.

- Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotationsByType

- Methods declared in interface javax.lang.model.element.

Element

accept

,

asType

,

equals

,

getAnnotation

,

getAnnotationMirrors

,

getKind

,

getModifiers

,

hashCode

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

ModuleElement.Directive

Represents a directive within the declaration of this
module.

static class

ModuleElement.DirectiveKind

The

kind

of a directive.

static interface

ModuleElement.DirectiveVisitor

<

R

,​

P

>

A visitor of module directives, in the style of the visitor design
pattern.

static interface

ModuleElement.ExportsDirective

An exported package of a module.

static interface

ModuleElement.OpensDirective

An opened package of a module.

static interface

ModuleElement.ProvidesDirective

An implementation of a service provided by a module.

static interface

ModuleElement.RequiresDirective

A dependency of a module.

static interface

ModuleElement.UsesDirective

A reference to a service used by a module.

---

#### Nested Class Summary

Represents a directive within the declaration of this
module.

The

kind

of a directive.

A visitor of module directives, in the style of the visitor design
pattern.

An exported package of a module.

An opened package of a module.

An implementation of a service provided by a module.

A dependency of a module.

A reference to a service used by a module.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<? extends

ModuleElement.Directive

>

getDirectives

()

Returns the directives contained in the declaration of this module.

List

<? extends

Element

>

getEnclosedElements

()

Returns the packages within this module.

Element

getEnclosingElement

()

Returns

null

since a module is not enclosed by another
element.

Name

getQualifiedName

()

Returns the fully qualified name of this module.

Name

getSimpleName

()

Returns the simple name of this module.

boolean

isOpen

()

Returns

true

if this is an open module and

false

otherwise.

boolean

isUnnamed

()

Returns

true

if this is an unnamed module and

false

otherwise.

- Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotationsByType

- Methods declared in interface javax.lang.model.element.

Element

accept

,

asType

,

equals

,

getAnnotation

,

getAnnotationMirrors

,

getKind

,

getModifiers

,

hashCode

---

#### Method Summary

Returns the directives contained in the declaration of this module.

Returns the packages within this module.

Returns

null

since a module is not enclosed by another
element.

Returns the fully qualified name of this module.

Returns the simple name of this module.

Returns

true

if this is an open module and

false

otherwise.

Returns

true

if this is an unnamed module and

false

otherwise.

Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotationsByType

---

#### Methods declared in interface javax.lang.model. AnnotatedConstruct

Methods declared in interface javax.lang.model.element.

Element

accept

,

asType

,

equals

,

getAnnotation

,

getAnnotationMirrors

,

getKind

,

getModifiers

,

hashCode

---

#### Methods declared in interface javax.lang.model.element. Element

============ METHOD DETAIL ==========

- Method Detail

- getQualifiedName

```java
Name
getQualifiedName()
```

Returns the fully qualified name of this module. For an

unnamed module

, an empty name is returned.

**Specified by:** getQualifiedName

in interface

QualifiedNameable
**API Note:** If the module name consists of one identifier, then
this method returns that identifier, which is deemed to be
module's fully qualified name despite not being in qualified
form. If the module name consists of more than one identifier,
then this method returns the entire name.
**Returns:** the fully qualified name of this module, or an
empty name if this is an unnamed module
**See The Java™ Language Specification :** 6.2 Names and Identifiers

- getSimpleName

```java
Name
getSimpleName()
```

Returns the simple name of this module. For an

unnamed module

, an empty name is returned.

**Specified by:** getSimpleName

in interface

Element
**API Note:** If the module name consists of one identifier, then
this method returns that identifier. If the module name
consists of more than one identifier, then this method returns
the rightmost such identifier, which is deemed to be the
module's simple name.
**Returns:** the simple name of this module or an empty name if
this is an unnamed module
**See Also:** PackageElement.getSimpleName()

,

ExecutableElement.getSimpleName()

,

TypeElement.getSimpleName()

,

VariableElement.getSimpleName()

,

getSimpleName()
**See The Java™ Language Specification :** 6.2 Names and Identifiers

- getEnclosedElements

```java
List
<? extends
Element
> getEnclosedElements()
```

Returns the packages within this module.

**Specified by:** getEnclosedElements

in interface

Element
**Returns:** the packages within this module
**See Also:** TypeElement.getEnclosedElements()

,

PackageElement.getEnclosedElements()

,

getEnclosedElements()

,

Elements.getAllMembers(javax.lang.model.element.TypeElement)

- isOpen

```java
boolean isOpen()
```

Returns

true

if this is an open module and

false

otherwise.

**Returns:** true

if this is an open module and

false

otherwise

- isUnnamed

```java
boolean isUnnamed()
```

Returns

true

if this is an unnamed module and

false

otherwise.

**Returns:** true

if this is an unnamed module and

false

otherwise
**See The Java™ Language Specification :** 7.7.5 Unnamed Modules

- getEnclosingElement

```java
Element
getEnclosingElement()
```

Returns

null

since a module is not enclosed by another
element.

**Specified by:** getEnclosingElement

in interface

Element
**Returns:** null
**See Also:** Elements.getPackageOf(javax.lang.model.element.Element)

- getDirectives

```java
List
<? extends
ModuleElement.Directive
> getDirectives()
```

Returns the directives contained in the declaration of this module.

**Returns:** the directives in the declaration of this module

Method Detail

- getQualifiedName

```java
Name
getQualifiedName()
```

Returns the fully qualified name of this module. For an

unnamed module

, an empty name is returned.

**Specified by:** getQualifiedName

in interface

QualifiedNameable
**API Note:** If the module name consists of one identifier, then
this method returns that identifier, which is deemed to be
module's fully qualified name despite not being in qualified
form. If the module name consists of more than one identifier,
then this method returns the entire name.
**Returns:** the fully qualified name of this module, or an
empty name if this is an unnamed module
**See The Java™ Language Specification :** 6.2 Names and Identifiers

- getSimpleName

```java
Name
getSimpleName()
```

Returns the simple name of this module. For an

unnamed module

, an empty name is returned.

**Specified by:** getSimpleName

in interface

Element
**API Note:** If the module name consists of one identifier, then
this method returns that identifier. If the module name
consists of more than one identifier, then this method returns
the rightmost such identifier, which is deemed to be the
module's simple name.
**Returns:** the simple name of this module or an empty name if
this is an unnamed module
**See Also:** PackageElement.getSimpleName()

,

ExecutableElement.getSimpleName()

,

TypeElement.getSimpleName()

,

VariableElement.getSimpleName()

,

getSimpleName()
**See The Java™ Language Specification :** 6.2 Names and Identifiers

- getEnclosedElements

```java
List
<? extends
Element
> getEnclosedElements()
```

Returns the packages within this module.

**Specified by:** getEnclosedElements

in interface

Element
**Returns:** the packages within this module
**See Also:** TypeElement.getEnclosedElements()

,

PackageElement.getEnclosedElements()

,

getEnclosedElements()

,

Elements.getAllMembers(javax.lang.model.element.TypeElement)

- isOpen

```java
boolean isOpen()
```

Returns

true

if this is an open module and

false

otherwise.

**Returns:** true

if this is an open module and

false

otherwise

- isUnnamed

```java
boolean isUnnamed()
```

Returns

true

if this is an unnamed module and

false

otherwise.

**Returns:** true

if this is an unnamed module and

false

otherwise
**See The Java™ Language Specification :** 7.7.5 Unnamed Modules

- getEnclosingElement

```java
Element
getEnclosingElement()
```

Returns

null

since a module is not enclosed by another
element.

**Specified by:** getEnclosingElement

in interface

Element
**Returns:** null
**See Also:** Elements.getPackageOf(javax.lang.model.element.Element)

- getDirectives

```java
List
<? extends
ModuleElement.Directive
> getDirectives()
```

Returns the directives contained in the declaration of this module.

**Returns:** the directives in the declaration of this module

---

#### Method Detail

getQualifiedName

```java
Name
getQualifiedName()
```

Returns the fully qualified name of this module. For an

unnamed module

, an empty name is returned.

**Specified by:** getQualifiedName

in interface

QualifiedNameable
**API Note:** If the module name consists of one identifier, then
this method returns that identifier, which is deemed to be
module's fully qualified name despite not being in qualified
form. If the module name consists of more than one identifier,
then this method returns the entire name.
**Returns:** the fully qualified name of this module, or an
empty name if this is an unnamed module
**See The Java™ Language Specification :** 6.2 Names and Identifiers

---

#### getQualifiedName

Name

getQualifiedName()

Returns the fully qualified name of this module. For an

unnamed module

, an empty name is returned.

getSimpleName

```java
Name
getSimpleName()
```

Returns the simple name of this module. For an

unnamed module

, an empty name is returned.

**Specified by:** getSimpleName

in interface

Element
**API Note:** If the module name consists of one identifier, then
this method returns that identifier. If the module name
consists of more than one identifier, then this method returns
the rightmost such identifier, which is deemed to be the
module's simple name.
**Returns:** the simple name of this module or an empty name if
this is an unnamed module
**See Also:** PackageElement.getSimpleName()

,

ExecutableElement.getSimpleName()

,

TypeElement.getSimpleName()

,

VariableElement.getSimpleName()

,

getSimpleName()
**See The Java™ Language Specification :** 6.2 Names and Identifiers

---

#### getSimpleName

Name

getSimpleName()

Returns the simple name of this module. For an

unnamed module

, an empty name is returned.

getEnclosedElements

```java
List
<? extends
Element
> getEnclosedElements()
```

Returns the packages within this module.

**Specified by:** getEnclosedElements

in interface

Element
**Returns:** the packages within this module
**See Also:** TypeElement.getEnclosedElements()

,

PackageElement.getEnclosedElements()

,

getEnclosedElements()

,

Elements.getAllMembers(javax.lang.model.element.TypeElement)

---

#### getEnclosedElements

List

<? extends

Element

> getEnclosedElements()

Returns the packages within this module.

isOpen

```java
boolean isOpen()
```

Returns

true

if this is an open module and

false

otherwise.

**Returns:** true

if this is an open module and

false

otherwise

---

#### isOpen

boolean isOpen()

Returns

true

if this is an open module and

false

otherwise.

isUnnamed

```java
boolean isUnnamed()
```

Returns

true

if this is an unnamed module and

false

otherwise.

**Returns:** true

if this is an unnamed module and

false

otherwise
**See The Java™ Language Specification :** 7.7.5 Unnamed Modules

---

#### isUnnamed

boolean isUnnamed()

Returns

true

if this is an unnamed module and

false

otherwise.

getEnclosingElement

```java
Element
getEnclosingElement()
```

Returns

null

since a module is not enclosed by another
element.

**Specified by:** getEnclosingElement

in interface

Element
**Returns:** null
**See Also:** Elements.getPackageOf(javax.lang.model.element.Element)

---

#### getEnclosingElement

Element

getEnclosingElement()

Returns

null

since a module is not enclosed by another
element.

getDirectives

```java
List
<? extends
ModuleElement.Directive
> getDirectives()
```

Returns the directives contained in the declaration of this module.

**Returns:** the directives in the declaration of this module

---

#### getDirectives

List

<? extends

ModuleElement.Directive

> getDirectives()

Returns the directives contained in the declaration of this module.

---

