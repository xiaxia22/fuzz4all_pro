# Interface Callback

**Source:** `java.base\javax\security\auth\callback\Callback.html`

### Class Description

```java
public interface
Callback
```

Implementations of this interface are passed to a

CallbackHandler

, allowing underlying security services
the ability to interact with a calling application to retrieve specific
authentication data such as usernames and passwords, or to display
certain information, such as error and warning messages.

Callback

implementations do not retrieve or
display the information requested by underlying security services.

Callback

implementations simply provide the means
to pass such requests to applications, and for applications,
if appropriate, to return requested information back to the
underlying security services.

**All Known Implementing Classes:** AuthorizeCallback

,

ChoiceCallback

,

ConfirmationCallback

,

LanguageCallback

,

NameCallback

,

PasswordCallback

,

RealmCallback

,

RealmChoiceCallback

,

TextInputCallback

,

TextOutputCallback

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface Callback

**All Known Implementing Classes:** AuthorizeCallback

,

ChoiceCallback

,

ConfirmationCallback

,

LanguageCallback

,

NameCallback

,

PasswordCallback

,

RealmCallback

,

RealmChoiceCallback

,

TextInputCallback

,

TextOutputCallback

```java
public interface
Callback
```

Implementations of this interface are passed to a

CallbackHandler

, allowing underlying security services
the ability to interact with a calling application to retrieve specific
authentication data such as usernames and passwords, or to display
certain information, such as error and warning messages.

Callback

implementations do not retrieve or
display the information requested by underlying security services.

Callback

implementations simply provide the means
to pass such requests to applications, and for applications,
if appropriate, to return requested information back to the
underlying security services.

**Since:** 1.4
**See Also:** CallbackHandler

,

ChoiceCallback

,

ConfirmationCallback

,

LanguageCallback

,

NameCallback

,

PasswordCallback

,

TextInputCallback

,

TextOutputCallback

public interface

Callback

Implementations of this interface are passed to a

CallbackHandler

, allowing underlying security services
the ability to interact with a calling application to retrieve specific
authentication data such as usernames and passwords, or to display
certain information, such as error and warning messages.

Callback

implementations do not retrieve or
display the information requested by underlying security services.

Callback

implementations simply provide the means
to pass such requests to applications, and for applications,
if appropriate, to return requested information back to the
underlying security services.

Callback

implementations do not retrieve or
display the information requested by underlying security services.

Callback

implementations simply provide the means
to pass such requests to applications, and for applications,
if appropriate, to return requested information back to the
underlying security services.

---

