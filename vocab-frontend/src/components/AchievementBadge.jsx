// src/components/AchievementBadge.jsx
export default function AchievementBadge({ title, description, unlocked }) {
    return (
      <div className={`p-4 rounded-lg ${
        unlocked ? 'bg-gradient-to-r from-yellow-400 to-orange-400' : 'bg-gray-200'
      }`}>
        <div className="flex items-center gap-3">
          <span className="text-2xl">{unlocked ? '🏆' : '🔒'}</span>
          <div>
            <h4 className="font-semibold">{title}</h4>
            <p className="text-sm">{description}</p>
          </div>
        </div>
      </div>
    );
  }