import { useState, useEffect } from 'react';
import { PxlKitIcon } from '@pxlkit/core';
import { Package, Robot, Search, Gear } from '@pxlkit/ui';
import { Trophy, Coin, Sword, Shield, Crown, Lightning } from '@pxlkit/gamification';
import { InfoCircle, WarningTriangle, CheckCircle, Bell } from '@pxlkit/feedback';
import {
  PixelButton,
  PixelCard,
  PixelBadge,
  PixelInput,
  PixelProgress,
  PixelAlert,
  PixelTabs,
  PixelTable,
  PxlKitButton,
  PixelPulse,
  PixelDivider,
  PixelAvatar,
  PixelStatCard,
  PixelChip
} from '@pxlkit/ui-kit';

function App() {
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState(45);

  useEffect(() => {
    const timer = setInterval(() => {
      setProgress(p => (p >= 100 ? 0 : p + 5));
    }, 1500);
    return () => clearInterval(timer);
  }, []);

  const handleAction = () => {
    setLoading(true);
    setTimeout(() => setLoading(false), 2000);
  };

  return (
    <div className="min-h-screen bg-retro-bg p-4 sm:p-8 flex flex-col items-center font-body text-retro-text">
      
      {/* Navigation */}
      <nav className="w-full max-w-5xl flex flex-col sm:flex-row justify-between items-center mb-8 bg-retro-surface p-4 border-2 border-retro-border rounded-lg shadow-retro-sm">
        <div className="flex items-center gap-3 mb-4 sm:mb-0">
          <PixelPulse>
            <PxlKitIcon icon={Package} size={32} color="#4F46E5" colorful={true} />
          </PixelPulse>
          <h1 className="font-pixel text-xl tracking-tighter text-retro-primary">PXL DASHBOARD</h1>
        </div>
        <div className="flex items-center gap-4">
          <PixelInput 
            placeholder="Search assets..." 
            icon={<PxlKitIcon icon={Search} size={16} />} 
          />
          <PxlKitButton icon={<PxlKitIcon icon={Bell} size={18} />} label="Notifications" tone="gold" />
          <PixelAvatar name="P1" tone="purple" />
        </div>
      </nav>

      {/* Main Content */}
      <main className="w-full max-w-5xl space-y-8">
        
        {/* Header Section */}
        <section className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
          <div>
            <h2 className="font-pixel text-2xl text-retro-text mb-2">Welcome Back, Player 1</h2>
            <p className="text-retro-muted font-mono text-sm">Manage your assets, quests, and inventory effortlessly.</p>
          </div>
          <div className="flex gap-3">
            <PixelButton tone="neutral" variant="ghost" iconLeft={<PxlKitIcon icon={Gear} size={16} />}>Settings</PixelButton>
            <PixelButton tone="green" iconLeft={<PxlKitIcon icon={Lightning} size={16} colorful={true} />} loading={loading} onClick={handleAction}>
              Quick Action
            </PixelButton>
          </div>
        </section>

        {/* Stats Row */}
        <section className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <PixelStatCard 
            label="Total XP" 
            value="12,450" 
            icon={<PxlKitIcon icon={Trophy} size={20} colorful={true} />} 
            tone="gold" 
          />
          <PixelStatCard 
            label="Gold Coins" 
            value="8,920" 
            icon={<PxlKitIcon icon={Coin} size={20} colorful={true} />} 
            tone="gold" 
          />
          <PixelStatCard 
            label="Quests Done" 
            value="45" 
            icon={<PxlKitIcon icon={CheckCircle} size={20} color="#10B981" colorful={true} />} 
            tone="green" 
          />
          <PixelStatCard 
            label="Rank" 
            value="Diamond" 
            icon={<PxlKitIcon icon={Crown} size={20} colorful={true} />} 
            tone="purple" 
          />
        </section>

        {/* Alerts & Progress */}
        <section className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div className="space-y-4">
             <h3 className="font-pixel text-sm text-retro-muted">LATEST ALERTS</h3>
             <PixelAlert 
               tone="red" 
               title="Critical Health" 
               icon={<PxlKitIcon icon={WarningTriangle} size={18} />} 
               message="Your shield durability is below 15%. Repair it immediately!"
             />
             <PixelAlert 
               tone="cyan" 
               title="System Update" 
               icon={<PxlKitIcon icon={InfoCircle} size={18} />}
               message="Version 2.0 is now live with enhanced retro capabilities."
             />
          </div>
          <div className="space-y-4">
             <h3 className="font-pixel text-sm text-retro-muted">CURRENT QUEST: THE CHOSEN ONE</h3>
             <PixelCard title="Defeat the UI Dragon">
                <div className="flex justify-between mb-2 font-mono text-sm">
                   <span className="text-retro-text font-bold">Progress</span>
                   <span className="text-retro-green">{progress}%</span>
                </div>
                <PixelProgress value={progress} tone="green" />
                <div className="mt-6 flex flex-wrap gap-2">
                   <PixelChip tone="gold" label="Combat" />
                   <PixelChip tone="purple" label="Epic Tier" />
                   <PixelChip tone="cyan" label="Defense" />
                </div>
             </PixelCard>
          </div>
        </section>

        <PixelDivider tone="neutral" spacing="lg" />

        {/* Inventory Interface */}
        <section className="space-y-6">
          <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
            <h3 className="font-pixel text-lg">Inventory System</h3>
            <PixelTabs 
              items={[
                { id: 'all', label: 'All Items', content: null },
                { id: 'weapons', label: 'Weapons', content: null },
                { id: 'potions', label: 'Potions', content: null }
              ]}
              defaultTab="all"
            />
          </div>

          <div className="overflow-x-auto">
            <PixelTable 
              columns={[
                { key: 'item', header: 'Item' },
                { key: 'type', header: 'Type' },
                { key: 'rarity', header: 'Rarity' },
                { key: 'action', header: 'Action' }
              ]}
              data={[
                {
                  item: <div className="flex items-center gap-3"><PxlKitIcon icon={Sword} size={32} colorful={true} /><span className="font-bold text-base">Excalibur</span></div>,
                  type: <span className="font-mono text-retro-muted">Weapon</span>,
                  rarity: <PixelBadge tone="gold">Legendary</PixelBadge>,
                  action: <PixelButton size="sm" tone="green" variant="ghost">Equip</PixelButton>
                },
                {
                  item: <div className="flex items-center gap-3"><PxlKitIcon icon={Shield} size={32} color="#4ECDC4" colorful={true} /><span className="font-bold text-base">Pixel Shield</span></div>,
                  type: <span className="font-mono text-retro-muted">Armor</span>,
                  rarity: <PixelBadge tone="cyan">Rare</PixelBadge>,
                  action: <PixelButton size="sm" tone="green" variant="ghost">Equip</PixelButton>
                },
                {
                  item: <div className="flex items-center gap-3"><PxlKitIcon icon={Robot} size={32} colorful={true} /><span className="font-bold text-base">Companion Bot</span></div>,
                  type: <span className="font-mono text-retro-muted">Pet</span>,
                  rarity: <PixelBadge tone="purple">Epic</PixelBadge>,
                  action: <PixelButton size="sm" tone="purple" variant="ghost">Summon</PixelButton>
                }
              ]}
            />
          </div>
        </section>

      </main>
    </div>
  );
}

export default App;
