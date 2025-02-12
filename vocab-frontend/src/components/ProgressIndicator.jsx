export default function ProgressIndicator({ current, total }) {
    return (
      <div className="progress-indicator">
        Aufgabe {current} von {total}
      </div>
    );
  }