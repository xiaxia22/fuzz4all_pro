# Interface ProcessingEnvironment

**Source:** `java.compiler\javax\annotation\processing\ProcessingEnvironment.html`

### Class Description

```java
public interface
ProcessingEnvironment
```

An annotation processing tool framework will

provide an annotation processor with an object
implementing this interface

so the processor can use facilities
provided by the framework to write new files, report error
messages, and find other utilities.

Third parties may wish to provide value-add wrappers around the
facility objects from this interface, for example a

Filer

extension that allows multiple processors to coordinate writing out
a single source file. To enable this, for processors running in a
context where their side effects via the API could be visible to
each other, the tool infrastructure must provide corresponding
facility objects that are

.equals

,

Filer

s that are

.equals

, and so on. In addition, the tool invocation must
be able to be configured such that from the perspective of the
running annotation processors, at least the chosen subset of helper
classes are viewed as being loaded by the same class loader.
(Since the facility objects manage shared state, the implementation
of a wrapper class must know whether or not the same base facility
object has been wrapped before.)

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Map
<
String
,​
String
> getOptions()

Returns the processor-specific options passed to the annotation
processing tool. Options are returned in the form of a map from
option name to option value. For an option with no value, the
corresponding value in the map is

null

.

See documentation of the particular tool infrastructure
being used for details on how to pass in processor-specific
options. For example, a command-line implementation may
distinguish processor-specific options by prefixing them with a
known string like

"-A"

; other tool implementations may
follow different conventions or provide alternative mechanisms.
A given implementation may also provide implementation-specific
ways of finding options passed to the tool in addition to the
processor-specific options.

**Returns:**
- the processor-specific options passed to the tool

---

#### Messager
getMessager()

Returns the messager used to report errors, warnings, and other
notices.

**Returns:**
- the messager

---

#### Filer
getFiler()

Returns the filer used to create new source, class, or auxiliary
files.

**Returns:**
- the filer

---

#### Elements
getElementUtils()

Returns an implementation of some utility methods for
operating on elements

**Returns:**
- element utilities

---

#### Types
getTypeUtils()

Returns an implementation of some utility methods for
operating on types.

**Returns:**
- type utilities

---

#### SourceVersion
getSourceVersion()

Returns the source version that any generated

source

and

class

files should conform to.

**Returns:**
- the source version to which generated source and class
files should conform to

**See Also:**
- Processor.getSupportedSourceVersion()

---

#### Locale
getLocale()

Returns the current locale or

null

if no locale is in
effect. The locale can be be used to provide localized

messages

.

**Returns:**
- the current locale or

null

if no locale is in
effect

---

### Additional Sections

#### Interface ProcessingEnvironment

```java
public interface
ProcessingEnvironment
```

An annotation processing tool framework will

provide an annotation processor with an object
implementing this interface

so the processor can use facilities
provided by the framework to write new files, report error
messages, and find other utilities.

Third parties may wish to provide value-add wrappers around the
facility objects from this interface, for example a

Filer

extension that allows multiple processors to coordinate writing out
a single source file. To enable this, for processors running in a
context where their side effects via the API could be visible to
each other, the tool infrastructure must provide corresponding
facility objects that are

.equals

,

Filer

s that are

.equals

, and so on. In addition, the tool invocation must
be able to be configured such that from the perspective of the
running annotation processors, at least the chosen subset of helper
classes are viewed as being loaded by the same class loader.
(Since the facility objects manage shared state, the implementation
of a wrapper class must know whether or not the same base facility
object has been wrapped before.)

**Since:** 1.6

public interface

ProcessingEnvironment

An annotation processing tool framework will

provide an annotation processor with an object
implementing this interface

so the processor can use facilities
provided by the framework to write new files, report error
messages, and find other utilities.

Third parties may wish to provide value-add wrappers around the
facility objects from this interface, for example a

Filer

extension that allows multiple processors to coordinate writing out
a single source file. To enable this, for processors running in a
context where their side effects via the API could be visible to
each other, the tool infrastructure must provide corresponding
facility objects that are

.equals

,

Filer

s that are

.equals

, and so on. In addition, the tool invocation must
be able to be configured such that from the perspective of the
running annotation processors, at least the chosen subset of helper
classes are viewed as being loaded by the same class loader.
(Since the facility objects manage shared state, the implementation
of a wrapper class must know whether or not the same base facility
object has been wrapped before.)

Third parties may wish to provide value-add wrappers around the
facility objects from this interface, for example a

Filer

extension that allows multiple processors to coordinate writing out
a single source file. To enable this, for processors running in a
context where their side effects via the API could be visible to
each other, the tool infrastructure must provide corresponding
facility objects that are

.equals

,

Filer

s that are

.equals

, and so on. In addition, the tool invocation must
be able to be configured such that from the perspective of the
running annotation processors, at least the chosen subset of helper
classes are viewed as being loaded by the same class loader.
(Since the facility objects manage shared state, the implementation
of a wrapper class must know whether or not the same base facility
object has been wrapped before.)

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Elements

getElementUtils

()

Returns an implementation of some utility methods for
operating on elements

Filer

getFiler

()

Returns the filer used to create new source, class, or auxiliary
files.

Locale

getLocale

()

Returns the current locale or

null

if no locale is in
effect.

Messager

getMessager

()

Returns the messager used to report errors, warnings, and other
notices.

Map

<

String

,​

String

>

getOptions

()

Returns the processor-specific options passed to the annotation
processing tool.

SourceVersion

getSourceVersion

()

Returns the source version that any generated

source

and

class

files should conform to.

Types

getTypeUtils

()

Returns an implementation of some utility methods for
operating on types.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Elements

getElementUtils

()

Returns an implementation of some utility methods for
operating on elements

Filer

getFiler

()

Returns the filer used to create new source, class, or auxiliary
files.

Locale

getLocale

()

Returns the current locale or

null

if no locale is in
effect.

Messager

getMessager

()

Returns the messager used to report errors, warnings, and other
notices.

Map

<

String

,​

String

>

getOptions

()

Returns the processor-specific options passed to the annotation
processing tool.

SourceVersion

getSourceVersion

()

Returns the source version that any generated

source

and

class

files should conform to.

Types

getTypeUtils

()

Returns an implementation of some utility methods for
operating on types.

---

#### Method Summary

Returns an implementation of some utility methods for
operating on elements

Returns the filer used to create new source, class, or auxiliary
files.

Returns the current locale or

null

if no locale is in
effect.

Returns the messager used to report errors, warnings, and other
notices.

Returns the processor-specific options passed to the annotation
processing tool.

Returns the source version that any generated

source

and

class

files should conform to.

Returns an implementation of some utility methods for
operating on types.

============ METHOD DETAIL ==========

- Method Detail

- getOptions

```java
Map
<
String
,​
String
> getOptions()
```

Returns the processor-specific options passed to the annotation
processing tool. Options are returned in the form of a map from
option name to option value. For an option with no value, the
corresponding value in the map is

null

.

See documentation of the particular tool infrastructure
being used for details on how to pass in processor-specific
options. For example, a command-line implementation may
distinguish processor-specific options by prefixing them with a
known string like

"-A"

; other tool implementations may
follow different conventions or provide alternative mechanisms.
A given implementation may also provide implementation-specific
ways of finding options passed to the tool in addition to the
processor-specific options.

**Returns:** the processor-specific options passed to the tool

- getMessager

```java
Messager
getMessager()
```

Returns the messager used to report errors, warnings, and other
notices.

**Returns:** the messager

- getFiler

```java
Filer
getFiler()
```

Returns the filer used to create new source, class, or auxiliary
files.

**Returns:** the filer

- getElementUtils

```java
Elements
getElementUtils()
```

Returns an implementation of some utility methods for
operating on elements

**Returns:** element utilities

- getTypeUtils

```java
Types
getTypeUtils()
```

Returns an implementation of some utility methods for
operating on types.

**Returns:** type utilities

- getSourceVersion

```java
SourceVersion
getSourceVersion()
```

Returns the source version that any generated

source

and

class

files should conform to.

**Returns:** the source version to which generated source and class
files should conform to
**See Also:** Processor.getSupportedSourceVersion()

- getLocale

```java
Locale
getLocale()
```

Returns the current locale or

null

if no locale is in
effect. The locale can be be used to provide localized

messages

.

**Returns:** the current locale or

null

if no locale is in
effect

Method Detail

- getOptions

```java
Map
<
String
,​
String
> getOptions()
```

Returns the processor-specific options passed to the annotation
processing tool. Options are returned in the form of a map from
option name to option value. For an option with no value, the
corresponding value in the map is

null

.

See documentation of the particular tool infrastructure
being used for details on how to pass in processor-specific
options. For example, a command-line implementation may
distinguish processor-specific options by prefixing them with a
known string like

"-A"

; other tool implementations may
follow different conventions or provide alternative mechanisms.
A given implementation may also provide implementation-specific
ways of finding options passed to the tool in addition to the
processor-specific options.

**Returns:** the processor-specific options passed to the tool

- getMessager

```java
Messager
getMessager()
```

Returns the messager used to report errors, warnings, and other
notices.

**Returns:** the messager

- getFiler

```java
Filer
getFiler()
```

Returns the filer used to create new source, class, or auxiliary
files.

**Returns:** the filer

- getElementUtils

```java
Elements
getElementUtils()
```

Returns an implementation of some utility methods for
operating on elements

**Returns:** element utilities

- getTypeUtils

```java
Types
getTypeUtils()
```

Returns an implementation of some utility methods for
operating on types.

**Returns:** type utilities

- getSourceVersion

```java
SourceVersion
getSourceVersion()
```

Returns the source version that any generated

source

and

class

files should conform to.

**Returns:** the source version to which generated source and class
files should conform to
**See Also:** Processor.getSupportedSourceVersion()

- getLocale

```java
Locale
getLocale()
```

Returns the current locale or

null

if no locale is in
effect. The locale can be be used to provide localized

messages

.

**Returns:** the current locale or

null

if no locale is in
effect

---

#### Method Detail

getOptions

```java
Map
<
String
,​
String
> getOptions()
```

Returns the processor-specific options passed to the annotation
processing tool. Options are returned in the form of a map from
option name to option value. For an option with no value, the
corresponding value in the map is

null

.

See documentation of the particular tool infrastructure
being used for details on how to pass in processor-specific
options. For example, a command-line implementation may
distinguish processor-specific options by prefixing them with a
known string like

"-A"

; other tool implementations may
follow different conventions or provide alternative mechanisms.
A given implementation may also provide implementation-specific
ways of finding options passed to the tool in addition to the
processor-specific options.

**Returns:** the processor-specific options passed to the tool

---

#### getOptions

Map

<

String

,​

String

> getOptions()

Returns the processor-specific options passed to the annotation
processing tool. Options are returned in the form of a map from
option name to option value. For an option with no value, the
corresponding value in the map is

null

.

See documentation of the particular tool infrastructure
being used for details on how to pass in processor-specific
options. For example, a command-line implementation may
distinguish processor-specific options by prefixing them with a
known string like

"-A"

; other tool implementations may
follow different conventions or provide alternative mechanisms.
A given implementation may also provide implementation-specific
ways of finding options passed to the tool in addition to the
processor-specific options.

See documentation of the particular tool infrastructure
being used for details on how to pass in processor-specific
options. For example, a command-line implementation may
distinguish processor-specific options by prefixing them with a
known string like

"-A"

; other tool implementations may
follow different conventions or provide alternative mechanisms.
A given implementation may also provide implementation-specific
ways of finding options passed to the tool in addition to the
processor-specific options.

getMessager

```java
Messager
getMessager()
```

Returns the messager used to report errors, warnings, and other
notices.

**Returns:** the messager

---

#### getMessager

Messager

getMessager()

Returns the messager used to report errors, warnings, and other
notices.

getFiler

```java
Filer
getFiler()
```

Returns the filer used to create new source, class, or auxiliary
files.

**Returns:** the filer

---

#### getFiler

Filer

getFiler()

Returns the filer used to create new source, class, or auxiliary
files.

getElementUtils

```java
Elements
getElementUtils()
```

Returns an implementation of some utility methods for
operating on elements

**Returns:** element utilities

---

#### getElementUtils

Elements

getElementUtils()

Returns an implementation of some utility methods for
operating on elements

getTypeUtils

```java
Types
getTypeUtils()
```

Returns an implementation of some utility methods for
operating on types.

**Returns:** type utilities

---

#### getTypeUtils

Types

getTypeUtils()

Returns an implementation of some utility methods for
operating on types.

getSourceVersion

```java
SourceVersion
getSourceVersion()
```

Returns the source version that any generated

source

and

class

files should conform to.

**Returns:** the source version to which generated source and class
files should conform to
**See Also:** Processor.getSupportedSourceVersion()

---

#### getSourceVersion

SourceVersion

getSourceVersion()

Returns the source version that any generated

source

and

class

files should conform to.

getLocale

```java
Locale
getLocale()
```

Returns the current locale or

null

if no locale is in
effect. The locale can be be used to provide localized

messages

.

**Returns:** the current locale or

null

if no locale is in
effect

---

#### getLocale

Locale

getLocale()

Returns the current locale or

null

if no locale is in
effect. The locale can be be used to provide localized

messages

.

---

